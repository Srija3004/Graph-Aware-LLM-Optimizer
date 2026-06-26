import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Home from './pages/Home'
import Solver from './pages/Solver'
import About from './pages/About'

function App() {
    return (
        <div className="app">
            <Header />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/solver" element={<Solver />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </div>
    )
}

export default App
