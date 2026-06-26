import './ProblemSelector.css'

const PROBLEMS = [
    {
        id: 'tsp',
        name: 'Traveling Salesman Problem',
        icon: '🚗',
        description: 'Find the shortest route visiting all cities',
        color: '#6366f1'
    },
    {
        id: 'coloring',
        name: 'Graph Coloring',
        icon: '🎨',
        description: 'Color nodes so no adjacent nodes share colors',
        color: '#ec4899'
    },
    {
        id: 'max-clique',
        name: 'Maximum Clique',
        icon: '👥',
        description: 'Find the largest complete subgraph',
        color: '#10b981'
    },
    {
        id: 'vertex-cover',
        name: 'Vertex Cover',
        icon: '🛡️',
        description: 'Minimum nodes to cover all edges',
        color: '#f59e0b'
    },
    {
        id: 'hamiltonian',
        name: 'Hamiltonian Path',
        icon: '🔗',
        description: 'Find a path visiting each node exactly once',
        color: '#8b5cf6'
    }
]

function ProblemSelector({ selectedProblem, onSelectProblem }) {
    return (
        <div className="problem-selector">
            <h3 className="text-gradient">Choose an Optimization Problem</h3>
            <div className="problem-grid">
                {PROBLEMS.map(problem => (
                    <button
                        key={problem.id}
                        className={`problem-card ${selectedProblem === problem.id ? 'selected' : ''}`}
                        onClick={() => onSelectProblem(problem.id)}
                        style={{ '--problem-color': problem.color }}
                    >
                        <div className="problem-icon">{problem.icon}</div>
                        <h4>{problem.name}</h4>
                        <p>{problem.description}</p>
                    </button>
                ))}
            </div>
        </div>
    )
}

export default ProblemSelector
