import './LoadingAnimation.css'

function LoadingAnimation() {
    return (
        <div className="loading-container">
            <div className="loading-spinner">
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
                <div className="spinner-ring"></div>
            </div>
            <p className="loading-text">Computing optimal solution...</p>
        </div>
    )
}

export default LoadingAnimation
