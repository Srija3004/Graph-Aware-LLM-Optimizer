import { Link, useLocation } from 'react-router-dom'
import './Header.css'

function Header() {
    const location = useLocation()

    return (
        <header className="header">
            <div className="container">
                <div className="header-content">
                    <Link to="/" className="logo">
                        <div className="logo-icon">🧠</div>
                        <span className="logo-text">Graph-Aware LLM</span>
                    </Link>

                    <nav className="nav">
                        <Link
                            to="/"
                            className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
                        >
                            Home
                        </Link>
                        <Link
                            to="/solver"
                            className={`nav-link ${location.pathname === '/solver' ? 'active' : ''}`}
                        >
                            Solver
                        </Link>
                        <Link
                            to="/about"
                            className={`nav-link ${location.pathname === '/about' ? 'active' : ''}`}
                        >
                            About
                        </Link>
                    </nav>
                </div>
            </div>
        </header>
    )
}

export default Header
