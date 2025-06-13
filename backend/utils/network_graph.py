import osmnx as ox
import networkx as nx

def get_walkable_network(lat, lon, radius_km=5):
    """
    Extract a walkable networkx.MultiDiGraph from OpenStreetMap data
    around a point using osmnx.

    Args:
        lat (float): Latitude of center point
        lon (float): Longitude of center point
        radius_km (float): Search radius in kilometers

    Returns:
        G (networkx.MultiDiGraph): The OSM walking network graph
    """
    G = ox.graph_from_point(
        (lat, lon),
        dist=radius_km * 1000,      # convert km to meters
        network_type='walk',        # or 'all_private' for more trails
        simplify=True,
        retain_all=True,            # keep disconnected subgraphs
        truncate_by_edge=True       # keep edges that cross boundary
    )
    return G

# Example usage:
if __name__ == "__main__":
    # Central London, 3km radius
    lat, lon, r = 51.5074, -0.1278, 3
    G = get_walkable_network(lat, lon, r)
    print(f"Number of nodes: {len(G.nodes)}")
    print(f"Number of edges: {len(G.edges)}")
    # Optionally plot or save:
    ox.plot_graph(G)
    # ox.save_graphml(G, "network.graphml")

