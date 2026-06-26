"""
Maximum Clique algorithm implementations.
"""
import networkx as nx
import time
from typing import List, Set


def bron_kerbosch(G: nx.Graph) -> List[str]:
    """
    Bron-Kerbosch algorithm for finding maximum clique.
    
    Args:
        G: NetworkX graph
        
    Returns:
        List of nodes in the maximum clique
    """
    max_clique = []
    
    def bron_kerbosch_recursive(R: Set, P: Set, X: Set):
        """Recursive Bron-Kerbosch with pivoting."""
        nonlocal max_clique
        
        if not P and not X:
            # R is a maximal clique
            if len(R) > len(max_clique):
                max_clique = list(R)
            return
        
        # Choose pivot
        pivot = max(P.union(X), key=lambda node: len(P.intersection(set(G.neighbors(node)))), default=None)
        
        if pivot is None:
            return
        
        # Iterate over vertices not neighbors of pivot
        for v in P.difference(set(G.neighbors(pivot))):
            neighbors = set(G.neighbors(v))
            bron_kerbosch_recursive(
                R.union({v}),
                P.intersection(neighbors),
                X.intersection(neighbors)
            )
            P.remove(v)
            X.add(v)
    
    all_nodes = set(G.nodes())
    bron_kerbosch_recursive(set(), all_nodes, set())
    
    return max_clique


def greedy_max_clique(G: nx.Graph) -> List[str]:
    """
    Greedy approximation for maximum clique.
    
    Args:
        G: NetworkX graph
        
    Returns:
        List of nodes in an approximate maximum clique
    """
    if not G.nodes():
        return []
    
    # Start with the node of highest degree
    nodes_by_degree = sorted(G.nodes(), key=lambda n: G.degree(n), reverse=True)
    clique = {nodes_by_degree[0]}
    
    # Iteratively add nodes that are connected to all nodes in current clique
    for node in nodes_by_degree[1:]:
        # Check if node is connected to all nodes in clique
        if all(G.has_edge(node, clique_node) for clique_node in clique):
            clique.add(node)
    
    return list(clique)


def solve_max_clique(G: nx.Graph, algorithm: str = "bron_kerbosch") -> dict:
    """
    Solve maximum clique problem using specified algorithm.
    
    Args:
        G: NetworkX graph
        algorithm: Algorithm choice (bron_kerbosch, greedy)
        
    Returns:
        Dictionary with solution details
    """
    start_time = time.time()
    
    # Choose algorithm based on graph size
    if algorithm == "bron_kerbosch" and len(G.nodes()) <= 50:
        clique = bron_kerbosch(G)
    elif algorithm == "greedy" or len(G.nodes()) > 50:
        clique = greedy_max_clique(G)
        algorithm = "greedy"
    else:
        # Default to greedy for large graphs
        clique = greedy_max_clique(G)
        algorithm = "greedy"
    
    execution_time = (time.time() - start_time) * 1000  # Convert to ms
    
    return {
        "success": True,
        "clique": clique,
        "clique_size": len(clique),
        "algorithm_used": algorithm,
        "execution_time_ms": round(execution_time, 2),
    }
