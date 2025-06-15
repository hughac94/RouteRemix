import osmnx as ox

# Load filtered running network
# G_running = ox.load_graphml("D:/osmnx_graphs_england_wales/Hertfordshire_England_United_Kingdom_RUNNING.graphml")

# Check for the bridleway by OSM ID
# target_osmid = 23611118
# found = False
#for u, v, k, data in G_running.edges(keys=True, data=True):
#    osmid = data.get('osmid')
#    if osmid == target_osmid or (isinstance(osmid, list) and target_osmid in osmid):
#        print(f"FOUND: {u}, {v}, {k}, {data}")
#        found = True
# print("Found way 23611118 in running network?", found)