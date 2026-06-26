"""
API routes for graph optimization problems.
"""
from fastapi import APIRouter, HTTPException
from api.models import (
    TSPRequest, ColoringRequest, MaxCliqueRequest, 
    VertexCoverRequest, HamiltonianRequest,
    OptimizationResponse, SolutionResult, LLMAnalysis, 
    VisualizationData, HealthResponse
)
from algorithms.graph_utils import create_graph_from_input, validate_graph, graph_to_visualization, generate_color_palette
from algorithms.tsp_solver import solve_tsp
from algorithms.graph_coloring import solve_graph_coloring
from algorithms.max_clique import solve_max_clique
from algorithms.vertex_cover import solve_vertex_cover
from algorithms.hamiltonian import solve_hamiltonian_path
from llm.mistral_client import mistral_client
from llm.prompts import get_graph_analysis_prompt, get_explanation_format_prompt


router = APIRouter(prefix="/api", tags=["optimization"])


@router.get("/health")
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        mistral_available=mistral_client.is_available()
    )


@router.post("/solve/tsp")
async def solve_tsp_endpoint(request: TSPRequest) -> OptimizationResponse:
    """Solve Traveling Salesman Problem."""
    try:
        # Create graph
        G = create_graph_from_input(request.nodes, request.edges, directed=False)
        
        # Validate
        is_valid, error = validate_graph(G, "tsp")
        if not is_valid:
            raise HTTPException(status_code=400, detail=error)
        
        # Solve TSP
        solution = solve_tsp(G, algorithm=request.algorithm)
        
        # Create visualization
        path = solution.get('path', [])
        highlighted_edges = [(path[i], path[i+1]) for i in range(len(path)-1)] if len(path) > 1 else []
        vis_nodes, vis_edges = graph_to_visualization(G, highlighted_nodes=path, highlighted_edges=highlighted_edges)
        
        # LLM analysis
        llm_analysis = None
        if request.use_llm_analysis:
            graph_info = {
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'density': 2 * G.number_of_edges() / (G.number_of_nodes() * (G.number_of_nodes() - 1)) if G.number_of_nodes() > 1 else 0
            }
            prompt = get_graph_analysis_prompt("TSP", graph_info, solution) + get_explanation_format_prompt()
            analysis = await mistral_client.analyze_graph_solution(prompt)
            
            if analysis:
                llm_analysis = LLMAnalysis(**analysis)
        
        return OptimizationResponse(
            solution=SolutionResult(**solution),
            llm_analysis=llm_analysis,
            visualization_data=VisualizationData(nodes=vis_nodes, edges=vis_edges)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/solve/coloring")
async def solve_coloring_endpoint(request: ColoringRequest) -> OptimizationResponse:
    """Solve Graph Coloring Problem."""
    try:
        # Create graph
        G = create_graph_from_input(request.nodes, request.edges, directed=False)
        
        # Solve coloring
        solution = solve_graph_coloring(G, algorithm=request.algorithm)
        
        # Create visualization with colors
        coloring = solution.get('coloring', {})
        num_colors = solution.get('num_colors', 0)
        color_palette = generate_color_palette(num_colors)
        
        node_colors = {node: color_palette[color] for node, color in coloring.items()}
        vis_nodes, vis_edges = graph_to_visualization(G, node_colors=node_colors)
        
        # LLM analysis
        llm_analysis = None
        if request.use_llm_analysis:
            graph_info = {
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'density': 2 * G.number_of_edges() / (G.number_of_nodes() * (G.number_of_nodes() - 1)) if G.number_of_nodes() > 1 else 0
            }
            prompt = get_graph_analysis_prompt("COLORING", graph_info, solution) + get_explanation_format_prompt()
            analysis = await mistral_client.analyze_graph_solution(prompt)
            
            if analysis:
                llm_analysis = LLMAnalysis(**analysis)
        
        return OptimizationResponse(
            solution=SolutionResult(**solution),
            llm_analysis=llm_analysis,
            visualization_data=VisualizationData(nodes=vis_nodes, edges=vis_edges)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/solve/max-clique")
async def solve_max_clique_endpoint(request: MaxCliqueRequest) -> OptimizationResponse:
    """Solve Maximum Clique Problem."""
    try:
        # Create graph
        G = create_graph_from_input(request.nodes, request.edges, directed=False)
        
        # Solve max clique
        solution = solve_max_clique(G, algorithm=request.algorithm)
        
        # Create visualization
        clique = solution.get('clique', [])
        clique_edges = [(u, v) for u in clique for v in clique if u != v and G.has_edge(u, v)]
        vis_nodes, vis_edges = graph_to_visualization(G, highlighted_nodes=clique, highlighted_edges=clique_edges)
        
        # LLM analysis
        llm_analysis = None
        if request.use_llm_analysis:
            graph_info = {
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'density': 2 * G.number_of_edges() / (G.number_of_nodes() * (G.number_of_nodes() - 1)) if G.number_of_nodes() > 1 else 0
            }
            prompt = get_graph_analysis_prompt("MAX_CLIQUE", graph_info, solution) + get_explanation_format_prompt()
            analysis = await mistral_client.analyze_graph_solution(prompt)
            
            if analysis:
                llm_analysis = LLMAnalysis(**analysis)
        
        return OptimizationResponse(
            solution=SolutionResult(**solution),
            llm_analysis=llm_analysis,
            visualization_data=VisualizationData(nodes=vis_nodes, edges=vis_edges)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/solve/vertex-cover")
async def solve_vertex_cover_endpoint(request: VertexCoverRequest) -> OptimizationResponse:
    """Solve Vertex Cover Problem."""
    try:
        # Create graph
        G = create_graph_from_input(request.nodes, request.edges, directed=False)
        
        # Solve vertex cover
        solution = solve_vertex_cover(G, algorithm=request.algorithm)
        
        # Create visualization
        vertex_cover = solution.get('vertex_cover', [])
        vis_nodes, vis_edges = graph_to_visualization(G, highlighted_nodes=vertex_cover)
        
        # LLM analysis
        llm_analysis = None
        if request.use_llm_analysis:
            graph_info = {
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'density': 2 * G.number_of_edges() / (G.number_of_nodes() * (G.number_of_nodes() - 1)) if G.number_of_nodes() > 1 else 0
            }
            prompt = get_graph_analysis_prompt("VERTEX_COVER", graph_info, solution) + get_explanation_format_prompt()
            analysis = await mistral_client.analyze_graph_solution(prompt)
            
            if analysis:
                llm_analysis = LLMAnalysis(**analysis)
        
        return OptimizationResponse(
            solution=SolutionResult(**solution),
            llm_analysis=llm_analysis,
            visualization_data=VisualizationData(nodes=vis_nodes, edges=vis_edges)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/solve/hamiltonian")
async def solve_hamiltonian_endpoint(request: HamiltonianRequest) -> OptimizationResponse:
    """Solve Hamiltonian Path Problem."""
    try:
        # Create graph
        G = create_graph_from_input(request.nodes, request.edges, directed=False)
        
        # Validate
        is_valid, error = validate_graph(G, "hamiltonian")
        if not is_valid:
            raise HTTPException(status_code=400, detail=error)
        
        # Solve Hamiltonian path
        solution = solve_hamiltonian_path(G, start_node=request.start_node)
        
        # Create visualization
        path = solution.get('path', [])
        highlighted_edges = [(path[i], path[i+1]) for i in range(len(path)-1)] if len(path) > 1 else []
        vis_nodes, vis_edges = graph_to_visualization(G, highlighted_nodes=path, highlighted_edges=highlighted_edges)
        
        # LLM analysis
        llm_analysis = None
        if request.use_llm_analysis:
            graph_info = {
                'num_nodes': G.number_of_nodes(),
                'num_edges': G.number_of_edges(),
                'density': 2 * G.number_of_edges() / (G.number_of_nodes() * (G.number_of_nodes() - 1)) if G.number_of_nodes() > 1 else 0
            }
            prompt = get_graph_analysis_prompt("HAMILTONIAN", graph_info, solution) + get_explanation_format_prompt()
            analysis = await mistral_client.analyze_graph_solution(prompt)
            
            if analysis:
                llm_analysis = LLMAnalysis(**analysis)
        
        return OptimizationResponse(
            solution=SolutionResult(**solution),
            llm_analysis=llm_analysis,
            visualization_data=VisualizationData(nodes=vis_nodes, edges=vis_edges)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
