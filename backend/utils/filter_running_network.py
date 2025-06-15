import osmnx as ox

# Path to your offline graph
G = ox.load_graphml("D:/osmnx_graphs_england_wales/Hertfordshire_England_United_Kingdom_ALL.graphml")

# List of highway values to include
running_highways = {
    "footway", "path", "bridleway", "cycleway", "residential", "living_street",
    "track", "service", "tertiary", "secondary", "unclassified", "primary_link",
    "tertiary_link", "secondary_link", "unclassified_link", "pedestrian"
}
# List of highway values to exclude (no running on these!)
exclude_highways = {
    "motorway", "motorway_link", "trunk", "trunk_link", "construction", "proposed"
}

# Build new filtered graph
edges_to_keep = []
for u, v, k, data in G.edges(keys=True, data=True):
    hwy = data.get('highway')
    # OSMnx sometimes stores 'highway' as a list, sometimes as a string
    if hwy is None:
        continue
    if isinstance(hwy, list):
        hwy_set = set(hwy)
    else:
        hwy_set = {hwy}
    # Exclude if any tag is in excluded, include if any tag is in desired
    if hwy_set & exclude_highways:
        continue
    if hwy_set & running_highways:
        edges_to_keep.append((u, v, k))

# Create a subgraph with only those edges
G_running = G.edge_subgraph(edges_to_keep).copy()

print(f"Original edges: {len(G.edges())}")
print(f"Filtered running edges: {len(G_running.edges())}")

target_osmid = 23611118
found = False
for u, v, k, data in G_running.edges(keys=True, data=True):
    osmid = data.get('osmid')
    if osmid == target_osmid or (isinstance(osmid, list) and target_osmid in osmid):
        print(f"FOUND: {u}, {v}, {k}, {data}")
        found = True
print("Found way 23611118 in running network?", found)

# Save if you want
ox.save_graphml(G_running, "D:/osmnx_graphs_england_wales/Hertfordshire_England_United_Kingdom_RUNNING.graphml")