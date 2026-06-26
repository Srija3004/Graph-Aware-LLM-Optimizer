"""
Vertex Cover algorithm implementations.
"""
import networkx as nx
import time
from typing import List, Set


def two_approximation_vertex_cover(G: nx.Graph) -> List[str]:
    """
    2-approximation algorithm for minimum vertex cover.
    Guarantees a solution at most twice the optimal size.
    
    Args:
        G: NetworkX graph
        
    Returns:
        List of nodes in the vertex cover
    """
    vertex_cover = set()
    edges = set(G.edges())
    
    while edges:
        # Pick an arbitrary edge
        u, v = edges.pop()
        
        # Add both endpoints to cover
        vertex_cover.add(u)
        vertex_cover.add(v)
        
        # Remove all edges incident to u or v
        edges = {(a, b) for a, b in edges if a not in {u, v} and b not in {u, v}}
    
    return list(vertex_cover)


def greedy_vertex_cover(G: nx.Graph) -> List[str]:
    """
    Greedy algorithm for vertex cover.
    Repeatedly selects the vertex with highest degree.
    
    Args:
        G: NetworkX graph
        
    Returns:
        List of nodes in the vertex cover
    """
    G_copy = G.copy()
    vertex_cover = []
    
    while G_copy.edges():
        # Select vertex with maximum degree
        max_degree_node = max(G_copy.nodes(), key=lambda n: G_copy.degree(n))
        vertex_cover.append(max_degree_node)
        
        # Remove the vertex and all its incident edges
        G_copy.remove_node(max_degree_node)
    
    return vertex_cover


def maximal_matching_vertex_cover(G: nx.Graph) -> List[str]:
    """
    Vertex cover using maximal matching approach.
    
    Args:
        G: NetworkX graph
        
    Returns:
        List of nodes in the vertex cover
    """
    try:
        # Find maximum matching
        matching = nx.max_weight_matching(G)
        
        # Vertex cover includes all matched vertices
        vertex_cover = set()
        for u, v in matching:
            vertex_cover.add(u)
            vertex_cover.add(v)
        
        return list(vertex_cover)
    except:
        # Fallback to 2-approximation
        return two_approximation_vertex_cover(G)


def solve_vertex_cover(G: nx.Graph, algorithm: str = "2approx") -> dict:
    """
    Solve minimum vertex cover problem using specified algorithm.
    
    Args:
        G: NetworkX graph
        algorithm: Algorithm choice (2approx, greedy, matching)
        
    Returns:
        Dictionary with solution details
    """
    start_time = time.time()
    
    # Choose algorithm
    if algorithm == "greedy":
        vertex_cover = greedy_vertex_cover(G)
    elif algorithm == "matching":
        vertex_cover = maximal_matching_vertex_cover(G)
    else:  # 2approx (default)
        vertex_cover = two_approximation_vertex_cover(G)
    
    execution_time = (time.time() - start_time) * 1000  # Convert to ms
    
    # Verify the cover is valid
    covered_edges = 0
    for u, v in G.edges():
        if u in vertex_cover or v in vertex_cover:
            covered_edges += 1
    
    is_valid = covered_edges == G.number_of_edges()
    
    return {
        "success": is_valid,
        "vertex_cover": vertex_cover,
        "cover_size": len(vertex_cover),
        "algorithm_used": algorithm,
        "execution_time_ms": round(execution_time, 2),
        "approximation_guarantee": "2x optimal" if algorithm == "2approx" else "heuristic",
    }
