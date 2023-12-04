import pandas as pd
import numpy as np
import glob
import os

# 定义文件夹路径和固定的CSV文件路径
folder_path = r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\New folder"
fixed_csv_path = r"C:\zhijie_project\data\location.csv"

# 定义计算距离的函数
def calculate_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# 读取固定的CSV文件
df1 = pd.read_csv(fixed_csv_path)
df1.dropna(subset=['latitude', 'longitude'], inplace=True)
latitudes_df1 = df1['latitude'].values
longitudes_df1 = df1['longitude'].values

# 使用glob获取文件夹中所有CSV文件的路径
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# 遍历每个CSV文件
for file in csv_files:
    df2 = pd.read_csv(file)
    df2.dropna(inplace=True)

    min_distances = []
    min_indices = []

    for index2, row2 in df2.iterrows():
        x2 = row2['LAT']
        y2 = row2['LON']
        
        distances = calculate_distance(latitudes_df1, longitudes_df1, x2, y2)
        min_distance = np.min(distances)
        min_index = np.argmin(distances)
        min_distances.append(min_distance)
        min_indices.append(min_index)

    df2['latitude'] = latitudes_df1[min_indices]
    df2['longitude'] = longitudes_df1[min_indices]

    new_file_name = os.path.splitext(os.path.basename(file))[0] + '_location.csv'
    df2.to_csv(os.path.join(folder_path, new_file_name), index=False)
