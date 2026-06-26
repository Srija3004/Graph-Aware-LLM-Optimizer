"""
Prompt templates for Mistral LLM graph analysis.
"""

def get_graph_analysis_prompt(problem_type: str, graph_info: dict, solution: dict) -> str:
    """
    Generate prompt for graph analysis based on problem type.
    
    Args:
        problem_type: Type of optimization problem
        graph_info: Information about the graph
        solution: Solution details
        
    Returns:
        Formatted prompt string
    """
    base_context = f"""You are an expert in graph theory and combinatorial optimization. 
Analyze the following {problem_type} problem and solution.

Graph Information:
- Number of nodes: {graph_info.get('num_nodes', 0)}
- Number of edges: {graph_info.get('num_edges', 0)}
- Graph density: {graph_info.get('density', 0):.2f}
"""
    
    if problem_type == "TSP":
        return base_context + f"""
Problem: Traveling Salesman Problem (TSP)
Solution Found:
- Path: {' → '.join(solution.get('path', []))}
- Total cost: {solution.get('cost', 0)}
- Algorithm used: {solution.get('algorithm_used', 'unknown')}

Please provide:
1. A clear explanation of why this is a good solution
2. Analysis of the path structure and any patterns
3. Quality assessment compared to theoretical bounds
4. Suggestions for improvement or alternative approaches
"""
    
    elif problem_type == "COLORING":
        return base_context + f"""
Problem: Graph Coloring
Solution Found:
- Number of colors used: {solution.get('num_colors', 0)}
- Algorithm used: {solution.get('algorithm_used', 'unknown')}

Please provide:
1. Explanation of the coloring quality
2. Analysis of whether this is optimal or near-optimal
3. Assessment of the graph's chromatic properties
4. Suggestions for improvement
"""
    
    elif problem_type == "MAX_CLIQUE":
        return base_context + f"""
Problem: Maximum Clique
Solution Found:
- Clique size: {solution.get('clique_size', 0)}
- Nodes in clique: {', '.join(solution.get('clique', []))}
- Algorithm used: {solution.get('algorithm_used', 'unknown')}

Please provide:
1. Explanation of the clique significance
2. Analysis of whether this might be the maximum clique
3. Properties of the clique in this graph
4. Insights about the graph structure
"""
    
    elif problem_type == "VERTEX_COVER":
        return base_context + f"""
Problem: Minimum Vertex Cover
Solution Found:
- Cover size: {solution.get('cover_size', 0)}
- Nodes in cover: {', '.join(solution.get('vertex_cover', []))}
- Algorithm used: {solution.get('algorithm_used', 'unknown')}
- Approximation guarantee: {solution.get('approximation_guarantee', 'unknown')}

Please provide:
1. Explanation of the vertex cover quality
2. Analysis of optimality
3. Assessment of the approximation quality
4. Insights about critical vertices
"""
    
    elif problem_type == "HAMILTONIAN":
        return base_context + f"""
Problem: Hamiltonian Path
Solution Found:
- Path exists: {solution.get('success', False)}
- Path: {' → '.join(solution.get('path', [])) if solution.get('path') else 'No path found'}
- Algorithm used: {solution.get('algorithm_used', 'unknown')}

Please provide:
1. Explanation of the result
2. Analysis of why a path does/doesn't exist
3. Graph properties related to Hamiltonicity
4. Insights about the graph structure
"""
    
    return base_context + "\nPlease analyze this graph problem."


def get_explanation_format_prompt() -> str:
    """
    Get the formatting instructions for LLM responses.
    
    Returns:
        Formatting prompt
    """
    return """Format your response as a flat JSON object with exactly three string fields. Do NOT use nested objects or lists:
{
    "explanation": "Clear text explanation of the solution (combine all points into 2-3 sentences)",
    "quality_assessment": "Assessment of solution quality (1-2 sentences)",
    "suggestions": "Practical suggestions or insights (1-2 sentences)"
}

Be concise, technical, and insightful. Focus on actionable insights.
"""
