import React from "react";
import MapView from "./components/Mapview";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card.tsx";
import { Badge } from "@/components/ui/badge.tsx";
import { Button } from "@/components/ui/button.tsx";
import { MapPin, Navigation, Route, ExternalLink } from "lucide-react";

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
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
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

        {/* Attributions Footer */}
        <Card className="border-0 shadow-lg bg-white/80 backdrop-blur-sm">
          <CardHeader className="pb-3">
            <CardTitle className="text-lg">Attributions & Credits</CardTitle>
          </CardHeader>
          <CardContent className="pt-0">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-sm">
              <div className="space-y-2">
                <h4 className="font-semibold text-primary">Maps & Data</h4>
                <div className="space-y-1">
                  <a 
                    href="https://www.mapbox.com/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    Mapbox <ExternalLink className="h-3 w-3" />
                  </a>
                  <a 
                    href="https://www.openstreetmap.org/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    OpenStreetMap <ExternalLink className="h-3 w-3" />
                  </a>
                </div>
              </div>
              
              <div className="space-y-2">
                <h4 className="font-semibold text-primary">UI Components</h4>
                <div className="space-y-1">
                  <a 
                    href="https://ui.shadcn.com/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    shadcn/ui <ExternalLink className="h-3 w-3" />
                  </a>
                  <a 
                    href="https://tailwindcss.com/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    Tailwind CSS <ExternalLink className="h-3 w-3" />
                  </a>
                </div>
              </div>
              
              <div className="space-y-2">
                <h4 className="font-semibold text-primary">Libraries</h4>
                <div className="space-y-1">
                  <a 
                    href="https://react-leaflet.js.org/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    React Leaflet <ExternalLink className="h-3 w-3" />
                  </a>
                  <a 
                    href="https://lucide.dev/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    Lucide Icons <ExternalLink className="h-3 w-3" />
                  </a>
                </div>
              </div>
              
              <div className="space-y-2">
                <h4 className="font-semibold text-primary">Development</h4>
                <div className="space-y-1">
                  <a 
                    href="https://vitejs.dev/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    Vite <ExternalLink className="h-3 w-3" />
                  </a>
                  <a 
                    href="https://reactjs.org/" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-muted-foreground hover:text-primary flex items-center gap-1 transition-colors"
                  >
                    React <ExternalLink className="h-3 w-3" />
                  </a>
                </div>
              </div>
            </div>
            
            <div className="mt-6 pt-4 border-t border-border">
              <p className="text-xs text-muted-foreground text-center">
                Built with ❤️ using modern web technologies. 
                <a 
                  href="https://github.com/yourusername/RouteRemix" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-primary hover:underline ml-1"
                >
                  View source on GitHub
                </a>
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

export default App;