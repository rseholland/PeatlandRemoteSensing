# Function to convert grid reference to Eastings and Northings
import osgb
import pandas as pd
def gridref_to_easting_northing(grid_ref):
    easting, northing = osgb.parse_grid(grid_ref)
    return pd.Series([easting, northing])
