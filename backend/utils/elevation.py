from dotenv import load_dotenv
import os
import math
import requests
from PIL import Image
from io import BytesIO
import osmnx as ox

# 1. Load Mapbox Token
load_dotenv()
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")

def latlon_to_tile(lat, lon, zoom):
    n = 2.0 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2.0 * n)
    return x, y

def latlon_to_pixel(lat, lon, zoom, xtile, ytile, tile_size=256):
    n = 2.0 ** zoom
    x = (lon + 180.0) / 360.0 * n
    y = (1.0 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2.0 * n
    px = int((x - xtile) * tile_size)
    py = int((y - ytile) * tile_size)
    return px, py

def get_tile(xtile, ytile, zoom):
    url = f"https://api.mapbox.com/v4/mapbox.terrain-rgb/{zoom}/{xtile}/{ytile}.pngraw?access_token={MAPBOX_TOKEN}"
    resp = requests.get(url)
    resp.raise_for_status()
    return Image.open(BytesIO(resp.content))

def decode_elevation(r, g, b):
    return -10000 + ((r * 256 * 256 + g * 256 + b) * 0.1)

def add_mapbox_elevations(G, zoom=15):
    # 1. Group nodes by tile
    node_tiles = {}
    for node, data in G.nodes(data=True):
        x, y = latlon_to_tile(data['y'], data['x'], zoom)
        node_tiles.setdefault((x, y), []).append((node, data['y'], data['x']))

    # 2. Download tile once, annotate all nodes in tile
    for (xtile, ytile), nodes in node_tiles.items():
        try:
            img = get_tile(xtile, ytile, zoom)
        except Exception as e:
            print(f"Failed to get tile {xtile},{ytile}: {e}")
            continue
        for node, lat, lon in nodes:
            px, py = latlon_to_pixel(lat, lon, zoom, xtile, ytile, tile_size=img.size[0])
            try:
                r, g, b, *_ = img.getpixel((px, py))
                elevation = decode_elevation(r, g, b)
            except Exception:
                elevation = None
            G.nodes[node]['elevation'] = elevation
    return G

if __name__ == "__main__":
    # Build network (small radius for test)
    lat, lon, r = 51.5074, -0.1278, 0.5
    G = ox.graph_from_point((lat, lon), dist=r * 1000, network_type='walk')
    print("Extracted network.")
    G = add_mapbox_elevations(G)
    print("Added node elevations.")
    G = ox.elevation.add_edge_grades(G)
    print("Added edge grades.")
    # Example: print node and edge
    node = list(G.nodes())[0]
    print(f"Sample node {node}: {G.nodes[node]}")
    u, v, k = list(G.edges(keys=True))[0]
    print(f"Sample edge {(u, v, k)}: {G.edges[u, v, k]}")