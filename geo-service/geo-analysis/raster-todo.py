import rasterio
from osgeo import gdal
from osgeo import osr
from matplotlib import pyplot
import numpy as np

# dataset = rasterio.open(r"C:\data\Tiff\Tuson_satelite_level1_4326.tif")
# print(dataset.count)
# print(dataset.width)
# print(dataset.height)
# print(dataset.bounds)
# print(dataset.crs)
# band1 = dataset.read(1)
# print(band1)
# pyplot.imshow(dataset.read(2))
# pyplot.show()

nmtif = gdal.Open(r'C:\data\geoanalysis\nm_relief_color.tif')
#nmtif = gdal.Open(r'C:\data\Tiff\Tuson_satelite_level1_4326.tif')
print(nmtif.GetMetadata())
p=osr.SpatialReference()
p.ImportFromEPSG(26913)
nmtif.SetProjection(p.ExportToWkt())
nmtif.GetProjection()
print(nmtif.GetProjection())
print(nmtif.RasterCount)
band=nmtif.GetRasterBand(1)
values=band.ReadAsArray()
print(values)

one= nmtif.GetRasterBand(1).ReadAsArray()
two = nmtif.GetRasterBand(2).ReadAsArray()
three= nmtif.GetRasterBand(3).ReadAsArray()
print(str(one[1100,1100])+","+str(two[1100,1100])+","+str(three[1100,1100]))

one= nmtif.GetRasterBand(1)
two = nmtif.GetRasterBand(2)
three= nmtif.GetRasterBand(3)

print(one.ComputeBandStats())
print(two.ComputeBandStats())
print(three.ComputeBandStats())
print(str(one.GetMinimum())+","+str(one.GetMaximum()))
print(one.GetDescription())

data_array=nmtif.ReadAsArray()
# Bands are indexed 1-n, but once read in as an array, they become indexed at 0.
x=np.array(data_array[0])
# x.shape ---> 6652,6300
w, h =6652, 6300
image = x.reshape(x.shape[0],x.shape[1])
pyplot.imshow(image, cmap='gist_earth')
pyplot.show()

# Create Raster
a_raster=np.array([
[10,10,1,10,10,10,10],
[1,1,1,50,10,10,50],
[10,1,1,51,10,10,50],
[1,1,1,1,50,10,50]])
coord=(-106.629773,35.105389)
w=10
h=10
name="BigI.tif"

print(a_raster.shape)

d=gdal.GetDriverByName("GTiff")
output=d.Create(name,a_raster.shape[1],a_raster.shape[0],1,gdal.GDT_UInt16)
output.SetGeoTransform((coord[0],w,0,coord[1],0,h))
output.GetRasterBand(1).WriteArray(a_raster)
outsr=osr.SpatialReference()
outsr.ImportFromEPSG(4326)
output.SetProjection(outsr.ExportToWkt())
output.FlushCache()
# Display again 
data=output.ReadAsArray()
w, h =4, 7
image = data.reshape(w,h) 
pyplot.imshow(image, cmap='Blues')
pyplot.show()

print(data)

