from math import radians, cos, sin, asin, sqrt

def cal_dist(vec1,
            vec2):
    """
    Calculate the distance between two places
    """
    lat1 = vec1[0]
    lon1 = vec1[1]
    lat2 = vec2[0]
    lon2 = vec2[1]
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    # haversine
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # the radius of earth
    return c * r * 1000 # return in meters