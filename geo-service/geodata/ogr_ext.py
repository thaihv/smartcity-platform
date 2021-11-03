from osgeo import ogr, osr
import os
r = ogr.Geometry(ogr.wkbLinearRing)
r.AddPoint(1,1)
r.AddPoint(5,1)
r.AddPoint(5,5)
r.AddPoint(1,5)
r.AddPoint(1,1)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(r)
print(poly.ExportToWkt())

geojson = """{"type":"Polygon","coordinates":[[[1,1],[5,1],[5,5],[1,5], [1,1]]]}"""
polygon = ogr.CreateGeometryFromJson(geojson)
print(polygon)
print("The area of our polygon is %d" % polygon.Area())
print("The centroid of our polygon is %s" % polygon.Centroid())
print("The boundary of our polygon is %s" % polygon.GetBoundary())
print("The convex hull of our polygon is %s" % polygon.ConvexHull())
print("The buffer of our polygon is %s" % polygon.Buffer(0))
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10, 10)
print("The polygon is containing point ?  %s" % polygon.Contains(point))

# 1 set the spatial reference
spatialReference = osr.SpatialReference()
#spatialReference.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
spatialReference.ImportFromEPSG(4326)
# 2 create a new shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')
shapeData = driver.CreateDataSource('my_polygon.shp')

# 3 create the layer
layer = shapeData.CreateLayer('polygon_layer', spatialReference, ogr.wkbPolygon)
#layerDefinition = layer.GetLayerDefn()
# 4 geometry is put inside feature
#featureIndex = 0
#feature = ogr.Feature(layerDefinition)
# feature.SetGeometry(polygon)
# feature.SetFID(featureIndex)
# 5 feature is put into layer
#layer.CreateFeature(feature)

shapefile = r"C:\data\MySHPLocal\VNM_adm\VNM_adm2.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layerSrc = dataSource.GetLayer()
feature  = layerSrc.GetFeature(0)
[layer.CreateField(feature.GetFieldDefnRef(i)) for i in range(feature.GetFieldCount())]
for featureSrc in layerSrc:
    layer.CreateFeature(featureSrc)


shapefile = r"C:\data\geoanalysis\ne_10m_populated_places.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
# open the data source with driver, zero means open in readonly mode
dataSource = driver.Open(shapefile, 0)
# use the GetLayer() function for referencing the layer that holds the data
layer = dataSource.GetLayer()
layer.SetSpatialFilterRect(-102, 26, -94, 36)
for feature in layer:
    if feature.GetField("ADM0NAME") != "United States of America":
        continue
    else:
        print(feature.GetField("NAME"))