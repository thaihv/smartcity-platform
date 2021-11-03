import geopandas as gpd
import fiona
import matplotlib.pyplot as plt
#df = gpd.read_file(r'C:\data\MySHPLocal\SPC_PRV_ADMZONE.shp')
df = gpd.read_file(r'C:\data\geoanalysis\ne_110m_admin_1_states_provinces.shp')
# print(df.head())
# print(df.geom_type.head())
# print(df.crs)
# print(df.shape)
# print(df.columns)
# type(df)

# print(df.loc[0])

# print(df['name'])


print(fiona.supported_drivers)

# Geopandas select by index (label)
california = df.loc[df['name'] == "California"]
#california.plot(figsize=(7,7))

# Geopandas select by position
multipl = df.iloc[[5,7,9,11]]
#multipl.plot(cmap="Set1", figsize=(7,7))


# Geopandas select by intersection with bounding box. 
exp = df.cx[-124:-118,30:50]
#exp.plot(cmap="Set1", figsize=(7,7))


#print(df.to_json())
#df.to_file(driver='GeoJSON',filename=r'C:\data\SPC_PRV_ADMZONE.geojson')
#df.to_file(driver='DGN',filename=r'C:\data\SPC_PRV_ADMZONE.dgn')
#df.to_file(filename=r'C:\data\SPC_PRV_ADMZONE.dxf', driver='DXF')
df.to_csv(path_or_buf=r'C:\data\states_provinces.csv', sep='\t', encoding='utf-8')

states = gpd.read_file(r"C:\data\geoanalysis\ne_110m_admin_1_states_provinces.shp")
#states.plot(figsize=(10,10))

fires = gpd.read_file(r"C:\data\geoanalysis\mtbs_FODpoints_DD.shp")
print(fires.columns)
print(fires.crs)
print(states.crs)

fires = fires.to_crs({'init': 'epsg:4326'})

state_fires = gpd.sjoin(fires,states[['name','geometry']].copy(),op='within' )

counts_per_state = state_fires.groupby('name').size()
counts_per_state.sort_values(axis=0, ascending=False)
counts_per_state_df = counts_per_state.reset_index(name='number_of_fires')

join = states.merge(counts_per_state_df, left_on='name', right_on='name')

print(join.columns)
#ax = join.plot(column='number_of_fires', figsize=(15, 6), cmap='OrRd', legend=True)
f, ax = plt.subplots(1, figsize=(18,6))
ax = join.plot(column='number_of_fires', cmap='Accent', legend=True, ax=ax)
lims = plt.axis('equal')
f.suptitle('US Wildfire count per state in 1984-2015')
ax.set_axis_off()

plt.show()