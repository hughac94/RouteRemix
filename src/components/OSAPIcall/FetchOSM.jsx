import { buildOverpassQuery } from './buildOverpassQuery';

export async function fetchOSMNetwork(lat, lon) {
  const query = buildOverpassQuery(lat, lon);
  const response = await fetch('https://overpass-api.de/api/interpreter', {
    method: 'POST',
    body: query,
  });
  if (!response.ok) throw new Error('Overpass API error');
  return await response.json();
}