from geopy.distance import distance
from geopy.point import Point


def calc_distance_between_airports(lat1, lon1, alt1, lat2, lon2, alt2):
    airport1 = Point(lat1, lon1, alt1)
    airport2 = Point(lat2, lon2, alt2)
    return distance(airport1, airport2).miles


def calc_distance_between(lat1, lon1, lat2, lon2):
    pos1 = Point(lat1, lon1)
    pos2 = Point(lat2, lon2)
    return distance(pos1, pos2).miles
