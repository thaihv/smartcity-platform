import requests
import json
from qgis.core import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtCore import *
import psycopg2


#from PyQt5.QtCore import  QVariant


# ADD LAYERS
# using QgsProject to add
provinces = QgsVectorLayer(r'C:\data\MySHPLocal\SPC_PRV_ADMZONE.shp', "Provinces","ogr")
QgsProject.instance().addMapLayers([provinces])
# use iface to add
bau = iface.addVectorLayer(r'C:\data\MySHPLocal\VNM_adm\VNM_adm3.shp', "Administratives","ogr")
#remove layer
QgsProject.instance().removeMapLayer(provinces.id())


# Add feature
theLayer=QgsVectorLayer('Point?crs=epsg:4326','SomePoints','memory')
theFeatures=theLayer.dataProvider()
theFeatures.addAttributes([QgsField("ID", QVariant.Int),QgsField("Name", QVariant.String)])
p=QgsFeature()
point=QgsPoint(107.5855,16.2543)
p.setGeometry(point)
p.setAttributes([123,"Paul"])
theFeatures.addFeatures([p])
theLayer.updateExtents()
theLayer.updateFields()
QgsProject.instance().addMapLayers([theLayer])

# Draw from PostGIS
connection = psycopg2.connect(database="geospatial",user="postgres", password="postgres")
cursor = connection.cursor()
cursor.execute("SELECT ID, ST_AsTexT(location) from lines")
c=cursor.fetchall()
theLayer=QgsVectorLayer('LineString?crs=epsg:4326','myLines','memory')
theFeatures=theLayer.dataProvider()
theFeatures.addAttributes([QgsField("ID",QVariant.Int)])
for f in c:
    g=QgsGeometry()
    g=QgsGeometry.fromWkt(f[1])
    p=QgsFeature()
    print(g)
    print(f[0])
    p.setGeometry(g)
    p.setAttributes([str(f[0])])
    theFeatures.addFeatures([p])
    theLayer.updateExtents()
    theLayer.updateFields()

QgsProject.instance().addMapLayers([theLayer])

print(theLayer.dataProvider().capabilitiesString())

# Add new Feature
feat = QgsFeature()
feat.setAttributes([4])
g=QgsGeometry.fromWkt('LineString (-106.645213 35.086822,-106.621334 35.124987 )')
feat.setGeometry(g)
theLayer.dataProvider().addFeatures([feat])


# Delete Feature
#for x in theLayer.getFeatures():
#    if x["ID"]==4:
#        theLayer.dataProvider().deleteFeatures([x.id()])

key = []
for x in theLayer.getFeatures():
    if x["ID"]==4:
        key.append(x.id())
    theLayer.dataProvider().deleteFeatures(key)   
# Change attr of index 2 with oder {0: new value, 1: new value, ...}      
theLayer.dataProvider().changeAttributeValues({2: {0:123} })

# Select feature
iface.mapCanvas().setSelectionColor( QColor("blue") )
#theLayer.selectByIds([1])
request = QgsFeatureRequest(QgsExpression(' "ID"  = 1'))
selection = theLayer.getFeatures(request)
theLayer.selectByIds([s.id() for s in selection])
