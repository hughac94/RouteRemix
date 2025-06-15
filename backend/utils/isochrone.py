import osmnx as ox
import networkx as nx
from shapely.geometry import MultiPoint, mapping
from backend.utils.elevation import add_mapbox_elevations
from backend.utils.GAPmodel import add_travel_time_gap
from backend.utils.graphloader import load_cached_county_graph, get_subgraph_around_point
import matplotlib.pyplot as plt

def compute_isochrone(lat, lon, radius_km, time_sec, county_name):
    # 1. Load the cached county graph
    G_county = load_cached_county_graph(county_name)
    print("county graph loaded")
    # 2. Extract only relevant subgraph (within radius_km of (lat, lon))
    G = get_subgraph_around_point(G_county, lat, lon, radius_km)
    print("subgraph extracted")
    # 3. Annotate with elevation and grade
    G = add_mapbox_elevations(G)
    print("elevations added")
    G = ox.elevation.add_edge_grades(G)
    print("edge grades added")
    # 4. Add grade-adjusted travel times
    G = add_travel_time_gap(G)
    print("travel times added")
    # 5. Find nearest node
    start = ox.nearest_nodes(G, lon, lat)
    print("start node found")
    # 6. Dijkstra for nodes within time budget
    nodes_within_time = nx.single_source_dijkstra_path_length(G, start, cutoff=time_sec, weight="travel_time")
    reachable_nodes = list(nodes_within_time.keys())
    print("reachable nodes found")
    # 7. Polygonize (convex hull for simplicity)
    points = [(G.nodes[n]['x'], G.nodes[n]['y']) for n in reachable_nodes]
    polygon = MultiPoint(points).convex_hull 
    print("polygon created")
    # 8. Return GeoJSON
    print(f"Reachable nodes: {len(reachable_nodes)}")
    

    # testing

    # # node scatter plot if needed
    xs, ys = zip(*[(G.nodes[n]['x'], G.nodes[n]['y']) for n in reachable_nodes])
    plt.scatter(xs, ys, s=5)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Reachable Nodes for Isochrone")
    plt.show()
    ox.plot_graph(G_county, bgcolor='w', node_color='r', edge_color='gray')
   
    high_street_nodes = set()
    for u, v, k, data in G.edges(keys=True, data=True):
        if data.get('name') == 'High Street' and data.get('ref') == 'B197':
            high_street_nodes.add(u)
            high_street_nodes.add(v)

    print(f"Nodes on High Street: {len(high_street_nodes)}")
    for node in high_street_nodes:
        print(f"Node: {node}, neighbors: {list(G.neighbors(node))}")

    # Plot all nodes
    xs, ys = zip(*[(G.nodes[n]['x'], G.nodes[n]['y']) for n in G.nodes()])
    plt.scatter(xs, ys, c='lightgray', s=1, label='All nodes')

    # Plot reachable nodes
    xs_r, ys_r = zip(*[(G.nodes[n]['x'], G.nodes[n]['y']) for n in reachable_nodes])
    plt.scatter(xs_r, ys_r, c='blue', s=3, label='Reachable nodes')

   # Check in full county graph
    edges_full = [
        (u, v, k, data) for u, v, k, data in G_county.edges(keys=True, data=True)
        if (data.get('osmid') == 23611118) or
        (isinstance(data.get('osmid'), list) and 23611118 in data.get('osmid'))
    ]
    print(f"Way 23611118 in full graph: {len(edges_full)} edges found")
    for u, v, k, data in edges_full:
        print(f"Edge {u}->{v} | {data}")

    # Check in your subgraph
    edges_sub = [
        (u, v, k, data) for u, v, k, data in G.edges(keys=True, data=True)
        if (data.get('osmid') == 23611118) or
        (isinstance(data.get('osmid'), list) and 23611118 in data.get('osmid'))
    ]
    print(f"Way 23611118 in subgraph: {len(edges_sub)} edges found")
    for u, v, k, data in edges_sub:
        print(f"Edge {u}->{v} | {data}")


    

    return {"type": "Feature", "geometry": mapping(polygon), "properties": {}}
