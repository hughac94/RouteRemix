import { getBoundingBox } from './BoundingBox';

export function buildOverpassQuery(lat, lon) {
  const bbox = getBoundingBox(lat, lon, 20);
  return `
    [out:json][timeout:25];
    (
      way["highway"~"footway|path|track|cycleway|bridleway|residential|living_street|unclassified|tertiary|secondary|primary"]
        (${bbox[0]},${bbox[1]},${bbox[2]},${bbox[3]});
    );
    out body;
    >;
    out skel qt;
  `;
}