import { useState } from 'react'
import './GraphInput.css'

function GraphInput({ onGraphSubmit }) {
    const [nodes, setNodes] = useState('')
    const [edges, setEdges] = useState('')

    const handleGenerateRandom = () => {
        const numNodes = Math.floor(Math.random() * 5) + 5 // 5-9 nodes
        const nodesList = Array.from({ length: numNodes }, (_, i) => String.fromCharCode(65 + i))
        setNodes(nodesList.join(', '))

        // Generate random edges
        const edgesList = []
        for (let i = 0; i < nodesList.length; i++) {
            for (let j = i + 1; j < nodesList.length; j++) {
                if (Math.random() > 0.5) {
                    const weight = Math.floor(Math.random() * 20) + 5
                    edgesList.push(`${nodesList[i]}-${nodesList[j]}:${weight}`)
                }
            }
        }
        setEdges(edgesList.join(', '))
    }

    const handleSubmit = (e) => {
        e.preventDefault()

        // Parse nodes
        const nodesList = nodes
            .split(',')
            .map(n => n.trim())
            .filter(n => n.length > 0)

        // Parse edges
        const edgesList = edges
            .split(',')
            .map(e => e.trim())
            .filter(e => e.length > 0)
            .map(e => {
                const [pair, weight] = e.split(':')
                const [source, target] = pair.split('-')
                return {
                    source: source.trim(),
                    target: target.trim(),
                    weight: weight ? parseFloat(weight) : 1.0
                }
            })

        onGraphSubmit({ nodes: nodesList, edges: edgesList })
    }

    return (
        <div className="graph-input card">
            <h3>📊 Define Your Graph</h3>
            <form onSubmit={handleSubmit} className="graph-form">
                <div className="form-group">
                    <label htmlFor="nodes">Nodes (comma-separated)</label>
                    <input
                        id="nodes"
                        type="text"
                        value={nodes}
                        onChange={(e) => setNodes(e.target.value)}
                        placeholder="A, B, C, D, E"
                        required
                    />
                    <p className="help-text">Example: A, B, C, D</p>
                </div>

                <div className="form-group">
                    <label htmlFor="edges">Edges (format: A-B:weight)</label>
                    <textarea
                        id="edges"
                        value={edges}
                        onChange={(e) => setEdges(e.target.value)}
                        placeholder="A-B:10, B-C:15, C-A:20"
                        rows="4"
                        required
                    />
                    <p className="help-text">Example: A-B:10, B-C:15, C-D:8 (weight is optional)</p>
                </div>

                <div className="button-group">
                    <button type="button" onClick={handleGenerateRandom} className="btn-secondary">
                        🎲 Generate Random
                    </button>
                    <button type="submit" className="btn">
                        ✨ Create Graph
                    </button>
                </div>
            </form>
        </div>
    )
}

export default GraphInput
