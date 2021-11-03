# -*- coding: utf-8 -*-
from shapely.geometry import MultiPolygon, Polygon, MultiLineString, LineString, MultiPoint, Point
from shapely.geometry.polygon import LinearRing
import json
from shapely.geometry import mapping, shape
import fiona
import pprint

p1 = Polygon(((1, 2), (5, 3), (5, 7), (1, 9), (1, 2)))
p2 = Polygon(((6,6), (7,6), (10,4), (11,8), (6,6)))


point = Point(2.0, 2.0)
q = Point((2.0, 2.0))
line = LineString([(0, 0), (10,10)])
ring = LinearRing([(0,0), (3,3), (3,0)])
points = MultiPoint([(0.0, 0.0), (3.0, 3.0)])
coords = MultiLineString([((0, 0), (1, 1)), ((-1, 0), (1, 0))])
polygons = MultiPolygon([p1, p2,])

print(polygons, coords, points)
print(p1.area)
print(p1.bounds)
print(p1.length)
print(p1.geom_type)

p = shape(json.loads('{"type": "Polygon", "coordinates": [[[1,1], [1,3 ], [3,3]]]}'))
print(json.dumps(mapping(p)))
print(p.area)

c = fiona.open(r"ne_110m_admin_1_states_provinces.shp")
rec = next(iter(c))
print(rec.keys())

print(len(c)) # prints total amount of features
print(c.driver) # prints driver name
print(c.crs)

pprint.pprint(rec['type'])
pprint.pprint(rec['id'])
pprint.pprint(rec['properties'])
pprint.pprint(rec['geometry'])

with fiona.open(r"ne_110m_admin_1_states_provinces.shp", encoding='utf-8') as src:
    pprint.pprint(src[0])