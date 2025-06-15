import os
import osmnx as ox

counties = [
    "Hertfordshire, England, United Kingdom",
    # ...add as many as you like
]

output_dir = "D:/osmnx_graphs_england_wales"
os.makedirs(output_dir, exist_ok=True)

for county in counties:
    filename = county.replace(", ", "_").replace(" ", "_") + "_ALL.graphml"
    filepath = os.path.join(output_dir, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {county} (all network)...")
        G = ox.graph_from_place(county, network_type="all", simplify=False)
        ox.save_graphml(G, filepath)
        print(f"Saved {filepath}")
    else:
        print(f"Already have {filepath}")