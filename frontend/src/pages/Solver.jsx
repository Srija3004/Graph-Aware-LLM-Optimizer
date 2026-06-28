import { useState } from 'react'
import axios from 'axios'
import ProblemSelector from '../components/ProblemSelector'
import GraphInput from '../components/GraphInput'
import GraphVisualizer from '../components/GraphVisualizer'
import ResultsPanel from '../components/ResultsPanel'
import LoadingAnimation from '../components/LoadingAnimation'
import './Solver.css'

function Solver() {
    const [selectedProblem, setSelectedProblem] = useState('tsp')
    const [graphData, setGraphData] = useState(null)
    const [visualizationData, setVisualizationData] = useState(null)
    const [result, setResult] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const handleGraphSubmit = (data) => {
        setGraphData(data)
        setResult(null)
        setError(null)

        // Create initial visualization
        const visNodes = data.nodes.map(node => ({
            id: node,
            label: node,
            highlighted: false
        }))

        const visEdges = data.edges.map(edge => ({
            source: edge.source,
            target: edge.target,
            weight: edge.weight,
            highlighted: false
        }))

        setVisualizationData({ nodes: visNodes, edges: visEdges })
    }

    const handleSolve = async () => {
        if (!graphData) return

        setLoading(true)
        setError(null)

        try {
            // const endpoint = `/api/solve/${selectedProblem}`
            const endpoint = `https://graph-aware-llm-backend.onrender.com/api/solve/${selectedProblem}`
            const response = await axios.post(endpoint, {
                nodes: graphData.nodes,
                edges: graphData.edges,
                use_llm_analysis: true,
                algorithm: 'auto'
            })

            setResult(response.data)

            // Update visualization with results
            if (response.data.visualization_data) {
                setVisualizationData(response.data.visualization_data)
            }
        } catch (err) {
            setError(err.response?.data?.detail || 'Failed to solve. Make sure the backend is running.')
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="solver-page">
            <div className="container">
                <div className="solver-header">
                    <h1>🧮 Graph Optimization Solver</h1>
                    <p>Create a graph, choose a problem, and let AI-powered algorithms find the optimal solution.</p>
                </div>

                <ProblemSelector
                    selectedProblem={selectedProblem}
                    onSelectProblem={setSelectedProblem}
                />

                <div className="solver-layout">
                    <div className="solver-input">
                        <GraphInput onGraphSubmit={handleGraphSubmit} />

                        {graphData && !loading && (
                            <button onClick={handleSolve} className="btn btn-solve">
                                ✨ Solve {selectedProblem.toUpperCase().replace('-', ' ')}
                            </button>
                        )}

                        {error && (
                            <div className="error-message card">
                                <h4>❌ Error</h4>
                                <p>{error}</p>
                            </div>
                        )}
                    </div>

                    <div className="solver-output">
                        {visualizationData && !loading && (
                            <div className="visualization-container card">
                                <h3>📊 Graph Visualization</h3>
                                <GraphVisualizer
                                    nodes={visualizationData.nodes}
                                    edges={visualizationData.edges}
                                    width={700}
                                    height={500}
                                />
                            </div>
                        )}

                        {loading && (
                            <div className="card">
                                <LoadingAnimation />
                            </div>
                        )}

                        {result && !loading && (
                            <ResultsPanel result={result} />
                        )}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Solver
