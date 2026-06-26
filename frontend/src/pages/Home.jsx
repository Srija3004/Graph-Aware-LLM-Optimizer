import { Link } from 'react-router-dom'
import './Home.css'

function Home() {
    return (
        <div className="home-page">
            {/* Hero Section */}
            <section className="hero">
                <div className="container">
                    <div className="hero-content fade-in">
                        <h1 className="hero-title">
                            Solve NP-Hard Problems with
                            <br />
                            <span className="text-gradient">Graph-Aware AI</span>
                        </h1>
                        <p className="hero-description">
                            Harness the power of Mistral LLM and advanced graph algorithms to tackle
                            the most challenging combinatorial optimization problems.
                        </p>
                        <div className="hero-buttons">
                            <Link to="/solver" className="btn btn-large">
                                🚀 Start Solving
                            </Link>
                            <Link to="/about" className="btn btn-outline btn-large">
                                📚 Learn More
                            </Link>
                        </div>
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="features">
                <div className="container">
                    <h2 className="text-center">Powerful Optimization Solutions</h2>
                    <div className="features-grid">
                        <div className="feature-card card">
                            <div className="feature-icon">🚗</div>
                            <h3>Traveling Salesman</h3>
                            <p>Find optimal routes through multiple points with advanced heuristics and 2-opt optimization.</p>
                        </div>

                        <div className="feature-card card">
                            <div className="feature-icon">🎨</div>
                            <h3>Graph Coloring</h3>
                            <p>Minimize colors needed using DSatur algorithm and intelligent greedy strategies.</p>
                        </div>

                        <div className="feature-card card">
                            <div className="feature-icon">👥</div>
                            <h3>Maximum Clique</h3>
                            <p>Discover complete subgraphs with Bron-Kerbosch algorithm and approximations.</p>
                        </div>

                        <div className="feature-card card">
                            <div className="feature-icon">🛡️</div>
                            <h3>Vertex Cover</h3>
                            <p>Cover all edges efficiently with 2-approximation guarantees.</p>
                        </div>

                        <div className="feature-card card">
                            <div className="feature-icon">🔗</div>
                            <h3>Hamiltonian Path</h3>
                            <p>Find paths visiting each vertex exactly once using backtracking.</p>
                        </div>

                        <div className="feature-card card">
                            <div className="feature-icon">🤖</div>
                            <h3>AI Analysis</h3>
                            <p>Get intelligent insights and explanations powered by Mistral LLM.</p>
                        </div>
                    </div>
                </div>
            </section>

            {/* Visualization Section */}
            <section className="visualization-preview">
                <div className="container">
                    <div className="preview-content">
                        <div className="preview-text">
                            <h2>Interactive Graph Visualization</h2>
                            <p>
                                See your optimization problems come to life with our beautiful,
                                interactive D3.js visualizations. Drag nodes, zoom, and explore
                                solutions in real-time.
                            </p>
                            <ul className="feature-list">
                                <li>✨ Real-time force-directed layouts</li>
                                <li>🎯 Highlighted solution paths</li>
                                <li>🔍 Zoom and pan controls</li>
                                <li>🎨 Beautiful color-coded results</li>
                            </ul>
                        </div>
                        <div className="preview-image">
                            <div className="preview-placeholder">
                                <div className="preview-graph">
                                    <div className="preview-node" style={{ top: '20%', left: '30%' }}></div>
                                    <div className="preview-node" style={{ top: '40%', left: '60%' }}></div>
                                    <div className="preview-node" style={{ top: '70%', left: '35%' }}></div>
                                    <div className="preview-node highlighted" style={{ top: '60%', left: '70%' }}></div>
                                    <svg className="preview-edges">
                                        <line x1="30%" y1="20%" x2="60%" y2="40%" />
                                        <line x1="60%" y1="40%" x2="70%" y2="60%" className="highlighted" />
                                        <line x1="70%" y1="60%" x2="35%" y2="70%" className="highlighted" />
                                        <line x1="35%" y1="70%" x2="30%" y2="20%" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="cta">
                <div className="container">
                    <div className="cta-card glass-card">
                        <h2>Ready to Optimize?</h2>
                        <p>Start solving NP-hard problems with AI-powered insights today.</p>
                        <Link to="/solver" className="btn btn-large">
                            Get Started →
                        </Link>
                    </div>
                </div>
            </section>
        </div>
    )
}

export default Home
