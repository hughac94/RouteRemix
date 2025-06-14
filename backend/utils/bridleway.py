import os
import osmnx as ox

counties = [
    "Hertfordshire, England, United Kingdom",
    # ...add as many as you like
]

output_dir = "D:/osmnx_graphs_england_wales"
os.makedirs(output_dir, exist_ok=True)

# Custom filter for UK running (includes bridleways, permissive, byways, road, all surfaces)
custom_filter = (
    '["highway"~"bridleway"]'
    '["area"!~"yes"]'
    '["access"!~"private|no"]'
)

for county in counties:
    filename = county.replace(", ", "_").replace(" ", "_") + "_bridleway.graphml"
    filepath = os.path.join(output_dir, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {county}...")
        G = ox.graph_from_place(county, custom_filter=custom_filter, simplify=False)
        ox.save_graphml(G, filepath)
        print(f"Saved {filepath}")
    else:
        print(f"Already have {filepath}")
