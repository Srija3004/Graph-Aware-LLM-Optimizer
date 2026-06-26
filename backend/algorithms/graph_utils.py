"""
Utility functions for graph creation, validation, and conversion.
"""
import networkx as nx
from typing import List, Dict, Tuple
from api.models import Edge, VisualizationNode, VisualizationEdge


def create_graph_from_input(nodes: List[str], edges: List[Edge], directed: bool = False) -> nx.Graph:
    """
    Create a NetworkX graph from input data.
    
    Args:
        nodes: List of node identifiers
        edges: List of Edge objects
        directed: Whether to create a directed graph
        
    Returns:
        NetworkX Graph or DiGraph
    """
    G = nx.DiGraph() if directed else nx.Graph()
    
    # Add nodes
    G.add_nodes_from(nodes)
    
    # Add edges with weights
    for edge in edges:
        G.add_edge(edge.source, edge.target, weight=edge.weight)
    
    return G


def validate_graph(G: nx.Graph, problem_type: str) -> Tuple[bool, str]:
    """
    Validate graph for specific problem requirements.
    
    Args:
        G: NetworkX graph
        problem_type: Type of optimization problem
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if G.number_of_nodes() == 0:
        return False, "Graph must have at least one node"
    
    if problem_type == "tsp":
        # TSP requires a complete graph or at least connected
        if not nx.is_connected(G):
            return False, "TSP requires a connected graph"
    
    elif problem_type == "hamiltonian":
        # Check basic connectivity
        if not nx.is_connected(G):
            return False, "Graph must be connected for Hamiltonian path"
    
    return True, ""


def graph_to_visualization(G: nx.Graph, highlighted_nodes: List[str] = None, 
                          highlighted_edges: List[Tuple[str, str]] = None,
                          node_colors: Dict[str, str] = None) -> Tuple[List[VisualizationNode], List[VisualizationEdge]]:
    """
    Convert NetworkX graph to visualization format.
    
    Args:
        G: NetworkX graph
        highlighted_nodes: List of node IDs to highlight
        highlighted_edges: List of edge tuples to highlight
        node_colors: Dictionary mapping node IDs to colors
        
    Returns:
        Tuple of (visualization_nodes, visualization_edges)
    """
    highlighted_nodes = highlighted_nodes or []
    highlighted_edges = highlighted_edges or []
    node_colors = node_colors or {}
    
    # Convert nodes
    vis_nodes = [
        VisualizationNode(
            id=str(node),
            label=str(node),
            highlighted=str(node) in highlighted_nodes,
            color=node_colors.get(str(node))
        )
        for node in G.nodes()
    ]
    
    # Convert edges
    vis_edges = []
    for source, target, data in G.edges(data=True):
        weight = data.get('weight', 1.0)
        edge_tuple = (str(source), str(target))
        reverse_tuple = (str(target), str(source))
        
        is_highlighted = edge_tuple in highlighted_edges or reverse_tuple in highlighted_edges
        
        vis_edges.append(
            VisualizationEdge(
                source=str(source),
                target=str(target),
                weight=weight,
                highlighted=is_highlighted
            )
        )
    
    return vis_nodes, vis_edges


def generate_color_palette(num_colors: int) -> List[str]:
    """
    Generate a visually distinct color palette.
    
    Args:
        num_colors: Number of colors needed
        
    Returns:
        List of hex color strings
    """
    # Premium color palette for graph visualization
    base_colors = [
        "#6366f1",  # Indigo
        "#ec4899",  # Pink
        "#10b981",  # Emerald
        "#f59e0b",  # Amber
        "#8b5cf6",  # Violet
        "#06b6d4",  # Cyan
        "#f97316",  # Orange
        "#14b8a6",  # Teal
        "#a855f7",  # Purple
        "#84cc16",  # Lime
    ]
    
    # Repeat colors if needed
    colors = []
    while len(colors) < num_colors:
        colors.extend(base_colors)
    
    return colors[:num_colors]
