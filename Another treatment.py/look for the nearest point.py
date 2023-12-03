import pandas as pd
import numpy as np

# 从CSV文件1中读取数据
df1 = pd.read_csv(r"C:\zhijie_project\data\location.csv")

# 从CSV文件2中读取数据
df2 = pd.read_csv(r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\VA_COND+PLOT_selected.csv")

# 删除df1和df2中包含空白值的行
df1.dropna(subset=['latitude', 'longitude'], inplace=True)
df2.dropna(inplace=True)

# 创建一个函数来计算距离
def calculate_distance(lat1, lon1, lat2, lon2):
    return np.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# 初始化一个用于存储最小距离和对应索引的列表
min_distances = []
min_indices = []

# 将df1的经纬度列转换为NumPy数组以加快计算
latitudes_df1 = df1['latitude'].values
longitudes_df1 = df1['longitude'].values

# 遍历CSV文件2中的每一行
for index2, row2 in df2.iterrows():
    x2 = row2['LAT']
    y2 = row2['LON']
    
    # 计算距离
    distances = calculate_distance(latitudes_df1, longitudes_df1, x2, y2)
    
    # 找到最小距离和对应的索引
    min_distance = np.min(distances)
    min_index = np.argmin(distances)
    
    # 将最小距离和对应索引添加到列表中
    min_distances.append(min_distance)
    min_indices.append(min_index)

    # 输出每一行的结果
    print(f"行 {index2 + 1}: 最小距离 = {min_distance}, 对应的CSV文件1行索引 = {min_index}")

# 将最小距离和对应的a列和b列的值复制到CSV文件2中的c列和d列
df2['latitude'] = latitudes_df1[min_indices]
df2['longitude'] = longitudes_df1[min_indices]

# 将结果保存到一个新的CSV文件
df2.to_csv(r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\VAaaa_COND+PLOT_selected_location.csv", index=False)
