export function getBoundingBox(lat, lon, radiusKm = 20) {
  const latRadius = radiusKm / 111; // degrees latitude
  const lonRadius = radiusKm / (111 * Math.cos(lat * Math.PI / 180)); // degrees longitude
  
  const south = lat - latRadius;
  const north = lat + latRadius;
  const west = lon - lonRadius;
  const east = lon + lonRadius;
  
  return [south, west, north, east];
}