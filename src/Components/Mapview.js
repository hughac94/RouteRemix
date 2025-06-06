import React from "react";
import { MapContainer, TileLayer, Marker, useMapEvents } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";
import "leaflet-defaulticon-compatibility";

function LocationMarker({ onSelect }) {
  const [position, setPosition] = React.useState(null);

  useMapEvents({
    click(e) {
      setPosition(e.latlng);
      if (onSelect) onSelect(e.latlng);
    },
  });

  return position === null ? null : (
    <Marker position={position}></Marker>
  );
}

export default function MapView({ onSelectLocation }) {
  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: "70vh", width: "100%" }}>
      <TileLayer
        attribution='&copy; OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <LocationMarker onSelect={onSelectLocation} />
    </MapContainer>
  );
}
