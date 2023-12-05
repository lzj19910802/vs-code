import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 读取Shapefile
shapefile_path = r"C:\Users\zhijiel\OneDrive\NCC论文材料准备\Shapefile\US_continental\ne_110m_admin_1_states_provinces.shp"
gdf = gpd.read_file(shapefile_path)

# 读取CSV文件
csv_path = r"C:\zhijie_project\data\location.csv"
df = pd.read_csv(csv_path)

# 为CSV文件中的每个点创建一个Point对象，并检查是否在Shapefile范围内
def check_point_in_shapefile(lon, lat, gdf):
    point = Point(lon, lat)
    return gdf.contains(point).any()

# 应用函数并创建一个新列
df['is_within_shape'] = df.apply(lambda row: check_point_in_shapefile(row['longitude'], row['latitude'], gdf), axis=1)

# 将结果保存到新的CSV文件
output_path = r"C:\zhijie_project\data\location_selected.csv"
df.to_csv(output_path, index=False)
