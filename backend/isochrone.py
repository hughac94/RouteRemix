def compute_isochrone(lat, lon, radius_km, time_sec):
    # TODO: Use osmnx to get network, annotate with elevation, pace model, etc.
    # For now, just return a dummy GeoJSON circle
    from shapely.geometry import Point, mapping
    from shapely.ops import transform
    import pyproj

    point = Point(lon, lat)
    proj_wgs84 = pyproj.CRS('EPSG:4326')
    proj_aeqd = pyproj.CRS.from_proj4(f"+proj=aeqd +lat_0={lat} +lon_0={lon}")
    transformer_to_aeqd = pyproj.Transformer.from_crs(proj_wgs84, proj_aeqd, always_xy=True)
    transformer_to_wgs84 = pyproj.Transformer.from_crs(proj_aeqd, proj_wgs84, always_xy=True)

    buffer = transform(transformer_to_aeqd.transform, point).buffer(radius_km * 1000)
    circle = transform(transformer_to_wgs84.transform, buffer)
    return mapping(circle)