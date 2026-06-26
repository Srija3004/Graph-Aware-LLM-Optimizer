import { useEffect, useRef } from 'react'
import * as d3 from 'd3'
import './GraphVisualizer.css'

function GraphVisualizer({ nodes, edges, width = 800, height = 600 }) {
    const svgRef = useRef()

    useEffect(() => {
        if (!nodes || nodes.length === 0) return

        // Clear previous visualization
        d3.select(svgRef.current).selectAll('*').remove()

        const svg = d3.select(svgRef.current)
            .attr('width', width)
            .attr('height', height)

        // Create container group for zoom
        const container = svg.append('g')

        // Add zoom behavior
        const zoom = d3.zoom()
            .scaleExtent([0.5, 3])
            .on('zoom', (event) => {
                container.attr('transform', event.transform)
            })

        svg.call(zoom)

        // Create force simulation
        const simulation = d3.forceSimulation(nodes)
            .force('link', d3.forceLink(edges)
                .id(d => d.id)
                .distance(100))
            .force('charge', d3.forceManyBody().strength(-300))
            .force('center', d3.forceCenter(width / 2, height / 2))
            .force('collision', d3.forceCollide().radius(40))

        // Draw edges
        const link = container.append('g')
            .selectAll('line')
            .data(edges)
            .enter()
            .append('line')
            .attr('class', d => d.highlighted ? 'edge highlighted' : 'edge')
            .attr('stroke-width', d => d.highlighted ? 4 : 2)

        // Draw edge labels (weights)
        const linkLabel = container.append('g')
            .selectAll('text')
            .data(edges)
            .enter()
            .append('text')
            .attr('class', 'edge-label')
            .text(d => d.weight !== 1.0 ? d.weight.toFixed(1) : '')

        // Draw nodes
        const node = container.append('g')
            .selectAll('circle')
            .data(nodes)
            .enter()
            .append('circle')
            .attr('class', d => d.highlighted ? 'node highlighted' : 'node')
            .attr('r', d => d.highlighted ? 18 : 15)
            .attr('fill', d => d.color || (d.highlighted ? '#ec4899' : '#6366f1'))
            .call(d3.drag()
                .on('start', dragStarted)
                .on('drag', dragged)
                .on('end', dragEnded))

        // Add node labels
        const nodeLabel = container.append('g')
            .selectAll('text')
            .data(nodes)
            .enter()
            .append('text')
            .attr('class', 'node-label')
            .text(d => d.label)

        // Update positions on tick
        simulation.on('tick', () => {
            link
                .attr('x1', d => d.source.x)
                .attr('y1', d => d.source.y)
                .attr('x2', d => d.target.x)
                .attr('y2', d => d.target.y)

            linkLabel
                .attr('x', d => (d.source.x + d.target.x) / 2)
                .attr('y', d => (d.source.y + d.target.y) / 2)

            node
                .attr('cx', d => d.x)
                .attr('cy', d => d.y)

            nodeLabel
                .attr('x', d => d.x)
                .attr('y', d => d.y + 4)
        })

        // Drag functions
        function dragStarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart()
            d.fx = d.x
            d.fy = d.y
        }

        function dragged(event, d) {
            d.fx = event.x
            d.fy = event.y
        }

        function dragEnded(event, d) {
            if (!event.active) simulation.alphaTarget(0)
            d.fx = null
            d.fy = null
        }

        return () => {
            simulation.stop()
        }
    }, [nodes, edges, width, height])

    return (
        <div className="graph-visualizer">
            <svg ref={svgRef}></svg>
            <div className="graph-controls">
                <p className="text-muted">💡 Drag nodes to reposition • Scroll to zoom</p>
            </div>
        </div>
    )
}

export default GraphVisualizer
