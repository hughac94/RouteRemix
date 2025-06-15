import os
import osmnx as ox
import networkx as nx

def load_cached_county_graph(county_name, graph_dir="D:/osmnx_graphs_england_wales", network="RUNNING"):
    """Load a pre-cached county graph, defaulting to the filtered running network."""
    filename = county_name.replace(", ", "_").replace(" ", "_") + f"_{network.upper()}.graphml"
    path = os.path.join(graph_dir, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Graph for {county_name} not found: {path}")
    return ox.load_graphml(path)

def get_subgraph_around_point(G, lat, lon, radius_km):
    """Extract a subgraph within radius_km of (lat, lon)."""
    center_node = ox.nearest_nodes(G, lon, lat)
    nodes = nx.single_source_dijkstra_path_length(G, center_node, cutoff=radius_km*1000, weight="length")
    sub_nodes = list(nodes.keys())
    SG = G.subgraph(sub_nodes).copy()
    return SG