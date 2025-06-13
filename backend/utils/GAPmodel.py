def gap_multiplier(grade):
    """Returns grade-adjusted pace multiplier for a given grade (slope)."""
    a = -5.294439830640173e-7
    b = -0.000003989571857841264
    c = 0.0020535661142752205
    d = 0.03265674125152065
    e = 1
    return a * grade**4 + b * grade**3 + c * grade**2 + d * grade + e

def add_travel_time_gap(G, flat_speed=1.4):
    """
    Adds 'travel_time' (seconds) to each edge using length, grade, and GAP model.
    flat_speed: walking speed on flat ground, in m/s.
    """
    for u, v, k, data in G.edges(keys=True, data=True):
        length = data.get('length', 1)  # meters
        grade = data.get('grade', 0.0)
        multiplier = gap_multiplier(grade)
        adjusted_speed = flat_speed * multiplier
        # Avoid division by zero or negative speeds
        if adjusted_speed > 0:
            travel_time = length / adjusted_speed  # seconds
        else:
            travel_time = float('inf')
        G.edges[u, v, k]['travel_time'] = travel_time
    return G