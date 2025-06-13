import React from "react";
import { MapContainer, TileLayer, Marker, Polyline, useMapEvents } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";
import "leaflet-defaulticon-compatibility";

const MAPBOX_TOKEN = import.meta.env.VITE_MAPBOX_TOKEN;

function LocationMarker({ onSelect }) {
  const [position, setPosition] = React.useState(null);

  useMapEvents({
    click(e) {
      setPosition(e.latlng);
      if (onSelect) onSelect(e.latlng);
    },
  });

  return position === null ? null : <Marker position={position}></Marker>;
}

export default function MapView({ onSelectLocation, route, startLocation }) {
  

  return (
    <MapContainer center={startLocation || [51.505, -0.09]} zoom={13} style={{ height: "70vh", width: "100%" }}>
      <TileLayer
        url={`https://api.mapbox.com/styles/v1/mapbox/streets-v12/tiles/{z}/{x}/{y}?access_token=${MAPBOX_TOKEN}`}
        attribution='&copy; <a href="https://www.mapbox.com/about/maps/" target="_blank">Mapbox</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>'
        tileSize={512}
        zoomOffset={-1}
      />
      <LocationMarker onSelect={onSelectLocation} />
      {route && <Polyline positions={route} color="blue" />}
    </MapContainer>
  );
}