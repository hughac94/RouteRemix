import React from "react";
import MapView from "./Components/Mapview";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { MapPin, Navigation, Route } from "lucide-react";

// commment

function App() {
  const [selectedLocation, setSelectedLocation] = React.useState(null);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Route className="h-8 w-8 text-primary" />
            <h1 className="text-4xl font-bold bg-gradient-to-r from-slate-900 to-slate-600 dark:from-slate-100 dark:to-slate-400 bg-clip-text text-transparent">
              Route Remixer
            </h1>
          </div>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Discover new paths and optimize your journeys with intelligent route planning
          </p>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Map Card */}
          <Card className="lg:col-span-2 overflow-hidden border-0 shadow-2xl">
            <CardHeader className="bg-gradient-to-r from-primary/10 to-secondary/10 border-b">
              <CardTitle className="flex items-center gap-2">
                <MapPin className="h-5 w-5 text-primary" />
                Interactive Map
              </CardTitle>
              <CardDescription>
                Click anywhere on the map to set your starting location
              </CardDescription>
            </CardHeader>
            <CardContent className="p-0">
              <MapView onSelectLocation={setSelectedLocation} />
            </CardContent>
          </Card>

          {/* Info Panel */}
          <div className="space-y-6">
            {/* Location Info */}
            <Card className="border-0 shadow-xl">
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Navigation className="h-5 w-5 text-primary" />
                  Location Details
                </CardTitle>
              </CardHeader>
              <CardContent>
                {selectedLocation ? (
                  <div className="space-y-4">
                    <div className="flex items-center gap-2">
                      <Badge variant="secondary" className="px-3 py-1">
                        Selected
                      </Badge>
                      <Badge variant="outline">Start Point</Badge>
                    </div>
                    <div className="grid grid-cols-1 gap-3">
                      <div className="bg-slate-50 dark:bg-slate-800 rounded-lg p-3">
                        <div className="text-sm font-medium text-muted-foreground">Latitude</div>
                        <div className="text-lg font-mono">{selectedLocation.lat.toFixed(6)}</div>
                      </div>
                      <div className="bg-slate-50 dark:bg-slate-800 rounded-lg p-3">
                        <div className="text-sm font-medium text-muted-foreground">Longitude</div>
                        <div className="text-lg font-mono">{selectedLocation.lng.toFixed(6)}</div>
                      </div>
                    </div>
                    <Button className="w-full" size="lg">
                      <Route className="h-4 w-4 mr-2" />
                      Generate Route
                    </Button>
                  </div>
                ) : (
                  <div className="text-center py-8">
                    <MapPin className="h-12 w-12 text-muted-foreground/50 mx-auto mb-4" />
                    <p className="text-muted-foreground">
                      Select a location on the map to get started
                    </p>
                  </div>
                )}
              </CardContent>
            </Card>

            {/* Quick Stats */}
            <Card className="border-0 shadow-xl">
              <CardHeader>
                <CardTitle>Quick Stats</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-2 gap-4">
                  <div className="text-center p-3 bg-primary/10 rounded-lg">
                    <div className="text-2xl font-bold text-primary">0</div>
                    <div className="text-sm text-muted-foreground">Routes Created</div>
                  </div>
                  <div className="text-center p-3 bg-secondary/10 rounded-lg">
                    <div className="text-2xl font-bold text-secondary-foreground">0km</div>
                    <div className="text-sm text-muted-foreground">Distance Mapped</div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;