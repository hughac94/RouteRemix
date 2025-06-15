import osmnx as ox
import networkx as nx
from shapely.geometry import MultiPoint, mapping
from backend.utils.elevation import add_mapbox_elevations
from backend.utils.GAPmodel import add_travel_time_gap
from backend.utils.graphloader import load_cached_county_graph, get_subgraph_around_point


def debug_find_way_edges(G, osmid_target):
    matches = []
    for u, v, k, data in G.edges(keys=True, data=True):
        osmid = data.get('osmid')
        if (osmid == osmid_target) or (isinstance(osmid, list) and osmid_target in osmid):
            matches.append((u, v, k, data))
    return matches

def compute_isochrone(lat, lon, radius_km, time_sec, county_name, network="RUNNING", flat_speed=1.4):
    # 1. Load the filtered running or all graph
    G_county = load_cached_county_graph(county_name, network=network)
    print(f"{network} county graph loaded")


    # 2. Extract only relevant subgraph (within radius_km of (lat, lon))
    G = get_subgraph_around_point(G_county, lat, lon, radius_km)
    print("subgraph extracted")
    print("Requested lat/lon:", lat, lon)
    xs = [G.nodes[n]['x'] for n in G.nodes]
    ys = [G.nodes[n]['y'] for n in G.nodes]
    print("Subgraph node bounds: x(min,max)", min(xs), max(xs), "y(min,max)", min(ys), max(ys))


    # 3. Annotate with elevation and grade
    G = add_mapbox_elevations(G)
    print("elevations added")
    G = ox.elevation.add_edge_grades(G)
    print("edge grades added")

    # 4. Add grade-adjusted travel times
    G = add_travel_time_gap(G, flat_speed=flat_speed)
    print("travel times added")

    # 5. Find nearest node
    start = ox.nearest_nodes(G, lon, lat)
    print("start node found")
    start_x = G.nodes[start]['x']
    start_y = G.nodes[start]['y']
    from math import sqrt
    dist = sqrt((start_x - lon)**2 + (start_y - lat)**2)
    print("Start node x/y:", start_x, start_y)
    print("Distance from requested point to start node:", dist)
    # 6. Dijkstra for nodes within time budget
    nodes_within_time = nx.single_source_dijkstra_path_length(G, start, cutoff=time_sec, weight="travel_time")
    reachable_nodes = list(nodes_within_time.keys())
    print("reachable nodes found")
    # 7. Polygonize (convex hull for simplicity)
    points = [(G.nodes[n]['x'], G.nodes[n]['y']) for n in reachable_nodes]
    polygon = MultiPoint(points).convex_hull 
    print("polygon created")
    print(f"Reachable nodes: {len(reachable_nodes)}")



    return {"type": "Feature", "geometry": mapping(polygon), "properties": {}}