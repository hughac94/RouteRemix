from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from isochrone import compute_isochrone

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, restrict in prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/isochrone")
def get_isochrone(lat: float, lon: float, radius_km: float = 20, time_sec: int = 3600):
    geojson = compute_isochrone(lat, lon, radius_km, time_sec)
    return geojson 
