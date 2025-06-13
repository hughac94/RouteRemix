import osmnx as ox
import networkx as nx
from shapely.geometry import MultiPoint, mapping
from backend.utils.network_graph import get_walkable_network
from backend.utils.elevation import add_mapbox_elevations
from backend.utils.GAPmodel import add_travel_time_gap

def compute_isochrone(lat, lon, radius_km, time_sec):
    # 1. Build the graph
    G = get_walkable_network(lat, lon, radius_km * 1000)
    print ("graph loaded")
    # 2. Annotate with elevation and grade
    G = add_mapbox_elevations(G)
    print ("elevations added")
    G = ox.elevation.add_edge_grades(G)
    print ("edge grades added")
    # 3. Add grade-adjusted travel times
    G = add_travel_time_gap(G)
    print ("travel times added")
    # 4. Find nearest node
    start = ox.nearest_nodes(G, lon, lat)
    print ("start node found")
    # 5. Dijkstra for nodes within time budget
    nodes_within_time = nx.single_source_dijkstra_path_length(G, start, cutoff=time_sec, weight="travel_time")
    reachable_nodes = list(nodes_within_time.keys())
    print ("reachable nodes found")
    # 6. Polygonize (convex hull for simplicity)
    points = [(G.nodes[n]['x'], G.nodes[n]['y']) for n in reachable_nodes]
    polygon = MultiPoint(points).convex_hull
    print ("polygon created")
    # 7. Return GeoJSON
    return {"type": "Feature", "geometry": mapping(polygon), "properties": {}}