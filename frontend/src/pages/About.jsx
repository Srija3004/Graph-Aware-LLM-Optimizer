import './About.css'

function About() {
    return (
        <div className="about-page">
            <div className="container">
                <div className="about-header">
                    <h1>About Graph-Aware LLM</h1>
                    <p>Bridging classical algorithms with modern AI</p>
                </div>

                <div className="about-content">
                    <section className="card">
                        <h2>🎯 Project Overview</h2>
                        <p>
                            This project combines cutting-edge graph algorithms with the power of
                            Mistral AI to solve NP-hard combinatorial optimization problems. By
                            leveraging both classical computational techniques and modern language
                            models, we provide not just solutions, but deep insights into complex
                            graph problems.
                        </p>
                    </section>

                    <section className="card">
                        <h2>🧮 Supported Problems</h2>
                        <div className="problem-list">
                            <div className="problem-item">
                                <h3>🚗 Traveling Salesman Problem (TSP)</h3>
                                <p>
                                    Find the shortest possible route that visits each city exactly once
                                    and returns to the origin. We use advanced heuristics including
                                    nearest neighbor, 2-opt optimization, and Christofides algorithm.
                                </p>
                            </div>

                            <div className="problem-item">
                                <h3>🎨 Graph Coloring</h3>
                                <p>
                                    Assign colors to graph vertices such that no two adjacent vertices
                                    share the same color, minimizing the total number of colors.
                                    Implemented using greedy, DSatur, and backtracking algorithms.
                                </p>
                            </div>

                            <div className="problem-item">
                                <h3>👥 Maximum Clique</h3>
                                <p>
                                    Find the largest complete subgraph where every pair of vertices is
                                    connected. Uses the Bron-Kerbosch algorithm with pivoting for exact
                                    solutions and greedy approximations for larger graphs.
                                </p>
                            </div>

                            <div className="problem-item">
                                <h3>🛡️ Minimum Vertex Cover</h3>
                                <p>
                                    Select the smallest set of vertices such that every edge is incident
                                    to at least one selected vertex. Provides 2-approximation guarantee
                                    and greedy heuristics.
                                </p>
                            </div>

                            <div className="problem-item">
                                <h3>🔗 Hamiltonian Path</h3>
                                <p>
                                    Determine if a path exists that visits each vertex exactly once.
                                    Uses backtracking for exact solutions on smaller graphs and heuristics
                                    for larger instances.
                                </p>
                            </div>
                        </div>
                    </section>

                    <section className="card">
                        <h2>🤖 AI-Powered Analysis</h2>
                        <p>
                            Powered by <strong>Mistral AI</strong>, our system provides intelligent
                            analysis of each solution:
                        </p>
                        <ul>
                            <li>Detailed explanations of the solution approach</li>
                            <li>Quality assessment compared to theoretical bounds</li>
                            <li>Suggestions for improvement and alternative strategies</li>
                            <li>Insights into graph structure and properties</li>
                        </ul>
                    </section>

                    <section className="card">
                        <h2>🛠️ Technology Stack</h2>
                        <div className="tech-grid">
                            <div className="tech-item">
                                <h4>Backend</h4>
                                <ul>
                                    <li>FastAPI (Python)</li>
                                    <li>NetworkX (Graph algorithms)</li>
                                    <li>Mistral AI API</li>
                                </ul>
                            </div>

                            <div className="tech-item">
                                <h4>Frontend</h4>
                                <ul>
                                    <li>React + Vite</li>
                                    <li>D3.js (Visualization)</li>
                                    <li>Modern CSS</li>
                                </ul>
                            </div>

                            <div className="tech-item">
                                <h4>Algorithms</h4>
                                <ul>
                                    <li>Exact solutions</li>
                                    <li>Approximation algorithms</li>
                                    <li>Heuristic methods</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <section className="card glass-card cta-section">
                        <h2>🚀 Get Started</h2>
                        <p>
                            Ready to solve complex optimization problems? Head over to the solver
                            and start experimenting with different graph structures and algorithms.
                        </p>
                        <a href="/solver" className="btn btn-large">
                            Try the Solver →
                        </a>
                    </section>
                </div>
            </div>
        </div>
    )
}

export default About
