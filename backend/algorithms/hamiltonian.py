"""
Hamiltonian Path algorithm implementations.
"""
import networkx as nx
import time
from typing import List, Optional


def backtracking_hamiltonian(G: nx.Graph, start_node: str = None) -> Optional[List[str]]:
    """
    Find Hamiltonian path using backtracking.
    
    Args:
        G: NetworkX graph
        start_node: Starting node (optional)
        
    Returns:
        List of nodes representing Hamiltonian path, or None if no path exists
    """
    nodes = list(G.nodes())
    if not nodes:
        return None
    
    start = start_node if start_node and start_node in nodes else nodes[0]
    n = len(nodes)
    path = [start]
    visited = {start}
    
    def backtrack():
        """Recursive backtracking to find Hamiltonian path."""
        if len(path) == n:
            return True
        
        current = path[-1]
        
        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                
                if backtrack():
                    return True
                
                path.pop()
                visited.remove(neighbor)
        
        return False
    
    if backtrack():
        return path
    return None


def hamiltonian_cycle_check(G: nx.Graph) -> Optional[List[str]]:
    """
    Check for Hamiltonian cycle and return it if found.
    
    Args:
        G: NetworkX graph
        
    Returns:
        List of nodes representing Hamiltonian cycle, or None if no cycle exists
    """
    nodes = list(G.nodes())
    if len(nodes) < 3:
        return None
    
    # Try from each node as starting point
    for start_node in nodes:
        path = backtracking_hamiltonian(G, start_node)
        
        if path and G.has_edge(path[-1], path[0]):
            # Found Hamiltonian cycle
            return path + [path[0]]
    
    return None


def heuristic_hamiltonian(G: nx.Graph, start_node: str = None) -> Optional[List[str]]:
    """
    Heuristic approach to find Hamiltonian path.
    Uses greedy strategy - not guaranteed to find path even if it exists.
    
    Args:
        G: NetworkX graph
        start_node: Starting node (optional)
        
    Returns:
        List of nodes representing path (may not be Hamiltonian)
    """
    nodes = list(G.nodes())
    if not nodes:
        return None
    
    start = start_node if start_node and start_node in nodes else nodes[0]
    path = [start]
    visited = {start}
    current = start
    
    while len(path) < len(nodes):
        # Find unvisited neighbor with minimum degree (more constrained)
        unvisited_neighbors = [n for n in G.neighbors(current) if n not in visited]
        
        if not unvisited_neighbors:
            break
        
        # Choose neighbor with minimum degree among unvisited
        next_node = min(unvisited_neighbors, key=lambda n: G.degree(n))
        path.append(next_node)
        visited.add(next_node)
        current = next_node
    
    return path if len(path) == len(nodes) else None


def solve_hamiltonian_path(G: nx.Graph, start_node: str = None, find_cycle: bool = False) -> dict:
    """
    Solve Hamiltonian path/cycle problem.
    
    Args:
        G: NetworkX graph
        start_node: Starting node (optional)
        find_cycle: Whether to find Hamiltonian cycle instead of path
        
    Returns:
        Dictionary with solution details
    """
    start_time = time.time()
    
    # Try different approaches based on graph size
    if len(G.nodes()) <= 15:
        # Use exact backtracking for small graphs
        if find_cycle:
            path = hamiltonian_cycle_check(G)
        else:
            path = backtracking_hamiltonian(G, start_node)
        algorithm = "backtracking"
    else:
        # Use heuristic for larger graphs
        path = heuristic_hamiltonian(G, start_node)
        algorithm = "heuristic"
        
        # If heuristic fails, try backtracking with timeout-like behavior
        if not path and len(G.nodes()) <= 20:
            path = backtracking_hamiltonian(G, start_node)
            algorithm = "backtracking"
    
    execution_time = (time.time() - start_time) * 1000  # Convert to ms
    
    success = path is not None
    path_length = len(path) if path else 0
    
    return {
        "success": success,
        "path": path if path else [],
        "path_length": path_length,
        "is_hamiltonian": path_length == len(G.nodes()) if not find_cycle else path_length == len(G.nodes()) + 1,
        "algorithm_used": algorithm,
        "execution_time_ms": round(execution_time, 2),
    }
