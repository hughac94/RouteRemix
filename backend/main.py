

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.utils.isochrone import compute_isochrone
from fastapi.responses import JSONResponse
import os
print("main.py loaded from:", os.path.abspath(__file__))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, restrict in prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/isochrone")
def get_isochrone(
    lat: float = 51.940973,
    lon: float = -0.230705,
    radius_km: float = 15,
    time_sec: int = 5400,
    countyname: str = Query("Hertfordshire, England, United Kingdom"),
    flat_speed: float = Query(1.4)  # <-- Add this line
):
    try:
        geojson = compute_isochrone(lat, lon, radius_km, time_sec, countyname, flat_speed)
        return geojson
    except Exception as e:
        import traceback
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "traceback": traceback.format_exc()},
        )