"""
Graph Coloring algorithm implementations.
"""
import networkx as nx
import time
from typing import Dict, List


def greedy_coloring(G: nx.Graph) -> Dict[str, int]:
    """
    Greedy graph coloring algorithm.
    
    Args:
        G: NetworkX graph
        
    Returns:
        Dictionary mapping nodes to colors (integers)
    """
    coloring = {}
    
    for node in G.nodes():
        # Get colors of neighbors
        neighbor_colors = {coloring[neighbor] for neighbor in G.neighbors(node) if neighbor in coloring}
        
        # Assign smallest available color
        color = 0
        while color in neighbor_colors:
            color += 1
        
        coloring[node] = color
    
    return coloring


def dsatur_coloring(G: nx.Graph) -> Dict[str, int]:
    """
    DSatur (Degree of Saturation) graph coloring algorithm.
    More sophisticated than greedy - often produces better results.
    
    Args:
        G: NetworkX graph
        
    Returns:
        Dictionary mapping nodes to colors (integers)
    """
    coloring = {}
    uncolored = set(G.nodes())
    
    while uncolored:
        # Calculate saturation degree for each uncolored node
        max_saturation = -1
        max_degree = -1
        next_node = None
        
        for node in uncolored:
            # Saturation = number of different colors in neighbors
            neighbor_colors = {coloring[neighbor] for neighbor in G.neighbors(node) if neighbor in coloring}
            saturation = len(neighbor_colors)
            degree = G.degree(node)
            
            if saturation > max_saturation or (saturation == max_saturation and degree > max_degree):
                max_saturation = saturation
                max_degree = degree
                next_node = node
        
        # Color the selected node with smallest available color
        neighbor_colors = {coloring[neighbor] for neighbor in G.neighbors(next_node) if neighbor in coloring}
        color = 0
        while color in neighbor_colors:
            color += 1
        
        coloring[next_node] = color
        uncolored.remove(next_node)
    
    return coloring


def backtracking_coloring(G: nx.Graph, max_colors: int = None) -> Dict[str, int]:
    """
    Backtracking algorithm for optimal graph coloring.
    Warning: Exponential time complexity - only use for small graphs!
    
    Args:
        G: NetworkX graph
        max_colors: Maximum number of colors to try
        
    Returns:
        Dictionary mapping nodes to colors (integers) or empty dict if no solution
    """
    nodes = list(G.nodes())
    n = len(nodes)
    
    if max_colors is None:
        max_colors = n
    
    coloring = {}
    
    def is_safe(node, color):
        """Check if color assignment is valid."""
        for neighbor in G.neighbors(node):
            if neighbor in coloring and coloring[neighbor] == color:
                return False
        return True
    
    def backtrack(node_idx):
        """Recursive backtracking."""
        if node_idx == n:
            return True
        
        node = nodes[node_idx]
        
        for color in range(max_colors):
            if is_safe(node, color):
                coloring[node] = color
                
                if backtrack(node_idx + 1):
                    return True
                
                del coloring[node]
        
        return False
    
    # Try to find coloring
    backtrack(0)
    return coloring


def solve_graph_coloring(G: nx.Graph, algorithm: str = "dsatur") -> Dict:
    """
    Solve graph coloring using specified algorithm.
    
    Args:
        G: NetworkX graph
        algorithm: Algorithm choice (greedy, dsatur, backtracking)
        
    Returns:
        Dictionary with solution details
    """
    start_time = time.time()
    
    # Choose algorithm
    if algorithm == "greedy":
        coloring = greedy_coloring(G)
    elif algorithm == "backtracking" and len(G.nodes()) <= 15:
        # Only use backtracking for small graphs
        coloring = backtracking_coloring(G)
        if not coloring:
            # Fallback to DSatur if backtracking fails
            coloring = dsatur_coloring(G)
    else:  # dsatur (default)
        coloring = dsatur_coloring(G)
    
    execution_time = (time.time() - start_time) * 1000  # Convert to ms
    
    num_colors = max(coloring.values()) + 1 if coloring else 0
    
    return {
        "success": True,
        "coloring": {str(k): v for k, v in coloring.items()},
        "num_colors": num_colors,
        "algorithm_used": algorithm,
        "execution_time_ms": round(execution_time, 2),
        "chromatic_number_bound": num_colors,
    }
