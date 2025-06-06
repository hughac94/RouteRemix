import React from "react";
import MapView from "./components/MapView";

function App() {
  const [selectedLocation, setSelectedLocation] = React.useState(null);

  return (
    <div>
      <h1>Route Remixer</h1>
      <p>Click the map to select your route start location.</p>
      <MapView onSelectLocation={setSelectedLocation} />
      {selectedLocation && (
        <div>
          <p>
            Selected Start: Latitude {selectedLocation.lat.toFixed(5)}, Longitude {selectedLocation.lng.toFixed(5)}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;