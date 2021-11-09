from osgeo import ogr
import os
source = ogr.Open(r"C:\data\geoanalysis\mtbs_FODpoints_DD.shp")
#source = ogr.Open(r"C:\data\MySHPLocal\SPC_PRV_ADMZONE.shp")
layer = source.GetLayer()
schema = []
ldefn = layer.GetLayerDefn()
for n in range(ldefn.GetFieldCount()):
    fdefn = ldefn.GetFieldDefn(n)
    schema.append(fdefn.name)
print(schema)

shapefile = r"C:\data\MySHPLocal\SPC_PRV_ADMZONE.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()

# Option 1: from Layer
spatialRef_1 = layer.GetSpatialRef()
print(spatialRef_1)
# Option 2: from Geometry
feature = layer.GetNextFeature()
geom = feature.GetGeometryRef()
spatialRef2 = geom.GetSpatialReference()
print(spatialRef2)

featureCount = layer.GetFeatureCount()
print("Number of features in %s: %d" % (os.path.basename(shapefile), featureCount))

for feature in layer:
    #print(feature.GetField(schema[0]), feature.GetField(schema[1]),feature.GetField(schema[2]),feature.GetField(schema[3]), sep="---", end = '\n')
    geom = feature.GetGeometryRef()
    print(geom.ExportToWkt())
    #print(geom.Centroid().ExportToWkt())

