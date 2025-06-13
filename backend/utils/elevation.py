import osmnx as ox

def add_node_elevations_and_grades(G):
    # Annotate nodes with elevation (meters)
    G = ox.elevation.add_node_elevations_raster(G, max_locations_per_batch=100)
    # Annotate edges with grade (rise/run fraction)
    G = ox.elevation.add_edge_grades(G)
    return G

if __name__ == "__main__":
    lat, lon, r = 51.5074, -0.1278, 3
    G = ox.graph_from_point((lat, lon), dist=r * 1000, network_type='walk')
    print("Extracted network.")
    G = add_node_elevations_and_grades(G)
    print("Added elevation and grades.")
    # Show sample node and edge
    node = list(G.nodes())[0]
    print(f"Sample node {node}: {G.nodes[node]}")
    u, v, k = list(G.edges(keys=True))[0]
    print(f"Sample edge {(u, v, k)}: {G.edges[u, v, k]}") 
