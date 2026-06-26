import './ResultsPanel.css'

function ResultsPanel({ result }) {
    if (!result) return null

    const { solution, llm_analysis } = result

    return (
        <div className="results-panel fade-in">
            <div className="card glass-card">
                <h3>🎯 Solution Results</h3>

                <div className="result-stats">
                    <div className="stat-card">
                        <div className="stat-icon">⚡</div>
                        <div className="stat-content">
                            <div className="stat-label">Execution Time</div>
                            <div className="stat-value">{solution.execution_time_ms}ms</div>
                        </div>
                    </div>

                    <div className="stat-card">
                        <div className="stat-icon">🧮</div>
                        <div className="stat-content">
                            <div className="stat-label">Algorithm</div>
                            <div className="stat-value">{solution.algorithm_used}</div>
                        </div>
                    </div>

                    {solution.cost !== undefined && (
                        <div className="stat-card">
                            <div className="stat-icon">💰</div>
                            <div className="stat-content">
                                <div className="stat-label">Total Cost</div>
                                <div className="stat-value">{solution.cost}</div>
                            </div>
                        </div>
                    )}

                    {solution.num_colors !== undefined && (
                        <div className="stat-card">
                            <div className="stat-icon">🎨</div>
                            <div className="stat-content">
                                <div className="stat-label">Colors Used</div>
                                <div className="stat-value">{solution.num_colors}</div>
                            </div>
                        </div>
                    )}

                    {solution.clique_size !== undefined && (
                        <div className="stat-card">
                            <div className="stat-icon">👥</div>
                            <div className="stat-content">
                                <div className="stat-label">Clique Size</div>
                                <div className="stat-value">{solution.clique_size}</div>
                            </div>
                        </div>
                    )}

                    {solution.cover_size !== undefined && (
                        <div className="stat-card">
                            <div className="stat-icon">🛡️</div>
                            <div className="stat-content">
                                <div className="stat-label">Cover Size</div>
                                <div className="stat-value">{solution.cover_size}</div>
                            </div>
                        </div>
                    )}
                </div>

                {solution.path && solution.path.length > 0 && (
                    <div className="solution-detail">
                        <h4>Path</h4>
                        <div className="path-display">
                            {solution.path.map((node, idx) => (
                                <span key={idx}>
                                    <span className="path-node">{node}</span>
                                    {idx < solution.path.length - 1 && <span className="path-arrow">→</span>}
                                </span>
                            ))}
                        </div>
                    </div>
                )}
            </div>

            {llm_analysis && (
                <div className="card glass-card llm-section">
                    <h3>🤖 AI Analysis</h3>

                    <div className="llm-content">
                        <div className="llm-block">
                            <div className="llm-label">Explanation</div>
                            <p>{llm_analysis.explanation}</p>
                        </div>

                        <div className="llm-block">
                            <div className="llm-label">Quality Assessment</div>
                            <p>{llm_analysis.quality_assessment}</p>
                        </div>

                        <div className="llm-block">
                            <div className="llm-label">Suggestions</div>
                            <p>{llm_analysis.suggestions}</p>
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}

export default ResultsPanel
