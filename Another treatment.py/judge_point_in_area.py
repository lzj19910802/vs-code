import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


shapefile_path = r"C:\Users\zhijiel\OneDrive\NCC论文材料准备\Shapefile\US_continental\ne_110m_admin_1_states_provinces.shp"
gdf = gpd.read_file(shapefile_path)


point = Point (153.2, 23.1)

is_within_shape = gdf.contains(point).any()

# 4. 根据is_within_shape的值来判断点是否在Shapefile范围内
if is_within_shape:
    print("坐标点在Shapefile范围内")
else:
    print("坐标点不在Shapefile范围内")