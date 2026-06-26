"""
Traveling Salesman Problem (TSP) solver implementations.
"""
import networkx as nx
import time
from typing import List, Tuple, Dict
from itertools import permutations
import math


def nearest_neighbor_tsp(G: nx.Graph, start_node: str = None) -> Tuple[List[str], float]:
    """
    Solve TSP using nearest neighbor heuristic.
    
    Args:
        G: NetworkX graph
        start_node: Starting node (optional)
        
    Returns:
        Tuple of (path, total_cost)
    """
    nodes = list(G.nodes())
    if not nodes:
        return [], 0.0
    
    start = start_node if start_node else nodes[0]
    unvisited = set(nodes)
    path = [start]
    current = start
    total_cost = 0.0
    
    unvisited.remove(current)
    
    while unvisited:
        # Find nearest unvisited neighbor
        nearest = None
        min_distance = float('inf')
        
        for node in unvisited:
            if G.has_edge(current, node):
                distance = G[current][node].get('weight', 1.0)
            else:
                distance = float('inf')
            
            if distance < min_distance:
                min_distance = distance
                nearest = node
        
        if nearest is None:
            # No path exists
            break
        
        path.append(nearest)
        total_cost += min_distance
        current = nearest
        unvisited.remove(current)
    
    # Return to start
    if G.has_edge(current, start):
        total_cost += G[current][start].get('weight', 1.0)
        path.append(start)
    
    return path, total_cost


def two_opt_improve(G: nx.Graph, path: List[str]) -> Tuple[List[str], float]:
    """
    Improve TSP solution using 2-opt local search.
    
    Args:
        G: NetworkX graph
        path: Initial tour path
        
    Returns:
        Tuple of (improved_path, total_cost)
    """
    def get_path_cost(p: List[str]) -> float:
        cost = 0.0
        for i in range(len(p) - 1):
            if G.has_edge(p[i], p[i + 1]):
                cost += G[p[i]][p[i + 1]].get('weight', 1.0)
            else:
                cost += float('inf')
        return cost
    
    improved = True
    best_path = path[:]
    
    while improved:
        improved = False
        for i in range(1, len(best_path) - 2):
            for j in range(i + 1, len(best_path) - 1):
                # Try reversing the segment between i and j
                new_path = best_path[:i] + best_path[i:j+1][::-1] + best_path[j+1:]
                
                if get_path_cost(new_path) < get_path_cost(best_path):
                    best_path = new_path
                    improved = True
    
    return best_path, get_path_cost(best_path)


def christofides_tsp(G: nx.Graph) -> Tuple[List[str], float]:
    """
    Christofides algorithm for metric TSP (provides 1.5-approximation).
    
    Args:
        G: NetworkX graph
        
    Returns:
        Tuple of (path, total_cost)
    """
    try:
        # This is a simplified version - full Christofides is complex
        # Using NetworkX's built-in approximation
        if len(G.nodes()) < 3:
            return list(G.nodes()), 0.0
        
        # Use NetworkX approximation
        try:
            cycle = nx.approximation.traveling_salesman_problem(G, cycle=True)
            cost = sum(G[cycle[i]][cycle[i+1]].get('weight', 1.0) for i in range(len(cycle)-1))
            return cycle, cost
        except:
            # Fallback to nearest neighbor
            return nearest_neighbor_tsp(G)
    except Exception as e:
        # Fallback to nearest neighbor
        return nearest_neighbor_tsp(G)


def solve_tsp(G: nx.Graph, algorithm: str = "auto", start_node: str = None) -> Dict:
    """
    Solve TSP using specified algorithm.
    
    Args:
        G: NetworkX graph
        algorithm: Algorithm choice (auto, nearest_neighbor, christofides)
        start_node: Starting node for the tour
        
    Returns:
        Dictionary with solution details
    """
    start_time = time.time()
    
    # Choose algorithm
    if algorithm == "auto":
        # Use christofides for smaller graphs, nearest neighbor for larger
        if len(G.nodes()) <= 20:
            algorithm = "christofides"
        else:
            algorithm = "nearest_neighbor"
    
    # Solve
    if algorithm == "christofides":
        path, cost = christofides_tsp(G)
        # Apply 2-opt improvement
        path, cost = two_opt_improve(G, path)
    else:  # nearest_neighbor
        path, cost = nearest_neighbor_tsp(G, start_node)
        # Apply 2-opt improvement
        path, cost = two_opt_improve(G, path)
    
    execution_time = (time.time() - start_time) * 1000  # Convert to ms
    
    return {
        "success": True,
        "path": path,
        "cost": round(cost, 2),
        "algorithm_used": algorithm,
        "execution_time_ms": round(execution_time, 2),
        "num_nodes": len(G.nodes()),
    }
