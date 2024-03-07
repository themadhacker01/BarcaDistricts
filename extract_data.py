import geopandas as gpd

# URL source from where we read the geodata
url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'

# Reads and stores the data in a geo dataframe
district_data = gpd.read_file(url)

# View columns in the dataframe
print(district_data.head())

# Write the geo dataframe to a file
district_data.to_file('district_data.geojson', driver = 'GeoJSON')