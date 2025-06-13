import osmnx as ox
import os

# List of counties in England and Wales (example subset for demo)
counties = [
    "Greater London, England, United Kingdom",
    "Hertfordshire, England, United Kingdom",
    # ...add as many as you like
]

output_dir = "D:/osmnx_graphs_england_wales"
os.makedirs(output_dir, exist_ok=True)

for county in counties:
    filename = county.replace(", ", "_").replace(" ", "_") + "_walk.graphml"
    filepath = os.path.join(output_dir, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {county}...")
        G = ox.graph_from_place(county, network_type="walk", simplify=True)
        ox.save_graphml(G, filepath)
        print(f"Saved {filepath}")
    else:
        print(f"Already have {filepath}")