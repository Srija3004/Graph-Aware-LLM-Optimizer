"""
Pydantic models for API request and response validation.
"""
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Any, Optional


class Edge(BaseModel):
    """Represents an edge in the graph."""
    source: str = Field(..., description="Source node identifier")
    target: str = Field(..., description="Target node identifier")
    weight: float = Field(default=1.0, description="Edge weight", ge=0)


class GraphInput(BaseModel):
    """Input model for graph-based problems."""
    nodes: List[str] = Field(..., description="List of node identifiers", min_items=2)
    edges: List[Edge] = Field(..., description="List of edges")
    use_llm_analysis: bool = Field(default=True, description="Whether to use LLM for analysis")
    
    @validator('nodes')
    def validate_unique_nodes(cls, v):
        if len(v) != len(set(v)):
            raise ValueError("Node identifiers must be unique")
        return v


class TSPRequest(GraphInput):
    """Request model for Traveling Salesman Problem."""
    algorithm: str = Field(default="auto", description="Algorithm choice: auto, nearest_neighbor, christofides")


class ColoringRequest(GraphInput):
    """Request model for Graph Coloring."""
    algorithm: str = Field(default="dsatur", description="Algorithm choice: greedy, dsatur, backtracking")


class MaxCliqueRequest(GraphInput):
    """Request model for Maximum Clique."""
    algorithm: str = Field(default="bron_kerbosch", description="Algorithm choice: bron_kerbosch, greedy")


class VertexCoverRequest(GraphInput):
    """Request model for Vertex Cover."""
    algorithm: str = Field(default="2approx", description="Algorithm choice: 2approx, greedy")


class HamiltonianRequest(GraphInput):
    """Request model for Hamiltonian Path."""
    start_node: Optional[str] = Field(None, description="Starting node for Hamiltonian path")


class SolutionResult(BaseModel):
    """Generic solution result."""
    success: bool
    algorithm_used: str
    execution_time_ms: float
    
    class Config:
        extra = 'allow'  # Allow additional fields


class LLMAnalysis(BaseModel):
    """LLM-generated analysis."""
    explanation: str
    quality_assessment: str
    suggestions: str


class VisualizationNode(BaseModel):
    """Node data for visualization."""
    id: str
    label: str
    highlighted: bool = False
    color: Optional[str] = None


class VisualizationEdge(BaseModel):
    """Edge data for visualization."""
    source: str
    target: str
    weight: float
    highlighted: bool = False


class VisualizationData(BaseModel):
    """Complete visualization data."""
    nodes: List[VisualizationNode]
    edges: List[VisualizationEdge]


class OptimizationResponse(BaseModel):
    """Complete optimization response."""
    solution: SolutionResult
    llm_analysis: Optional[LLMAnalysis] = None
    visualization_data: VisualizationData


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    mistral_available: bool
