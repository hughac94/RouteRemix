import os
import osmnx as ox

counties = [
    "Greater London, England, United Kingdom",
    "Hertfordshire, England, United Kingdom",
    # ...add as many as you like
]

output_dir = "D:/osmnx_graphs_england_wales"
os.makedirs(output_dir, exist_ok=True)

# Custom filter for UK running (includes bridleways, permissive, byways, road, all surfaces)
custom_filter = (
    '["highway"~"footway|path|pedestrian|residential|living_street|track|unclassified|service|tertiary|secondary|primary|bridleway|cycleway|steps|byway|restricted_byway|road"]'
    '["area"!~"yes"]'
    '["access"!~"private|no"]'
)

for county in counties:
    filename = county.replace(", ", "_").replace(" ", "_") + "_run.graphml"
    filepath = os.path.join(output_dir, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {county}...")
        G = ox.graph_from_place(county, custom_filter=custom_filter, simplify=True)
        ox.save_graphml(G, filepath)
        print(f"Saved {filepath}")
    else:
        print(f"Already have {filepath}")
