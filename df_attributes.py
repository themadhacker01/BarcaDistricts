import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Read data from static file
district_data = gpd.read_file('./district_data.geojson')
# print(district_data.head())

# View the CRS of geo dataframe
# print(district_data.crs)

# Transform to another CRS for ease of analysis
# EPSG:2062 is the standard projected CRS for Spain
district_data.to_crs(epsg = 2062, inplace = True)

# Area attribute finds the area of every district in m2
# We convert it km2 for ease of calculation
district_data['area'] = district_data.area / 1000000

# Centroid attribute finds the centroid of every  district
district_data['centroid'] = district_data.centroid

# Boundary attribute finds the boundary of every  district
district_data['boundary'] = district_data.boundary

# Calculate the distance between a church and every centroid
# Define a location and convert it into the correct CRS geo series
church_loc = Point(2.1743680500855005, 41.403656946781304)
church_loc = gpd.GeoSeries(church_loc, crs = 2062)

# Finds the distance between every district centroid and church location
district_data['church_dist'] = [church_loc.distance(cen).astype(float) / 1000 for cen in district_data['centroid']]

district_data.plot(column = district_data['NOM'], figsize = (10, 6), edgecolor = 'black', legend = True)
plt.show()