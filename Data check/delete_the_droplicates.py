# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:08:33 2023

@author: zhijiel
"""

import pandas as pd

# 读取合并后的CSV文件
combined_data = pd.read_csv(r"C:\FIA-Data\FIA数据\整理后美国50州数据\P2-chapter2\COND\COND_coordinate\1_selected.csv")

# 提取LAT和LON列
lat_lon_data = combined_data[['LAT', 'LON']]

# 使用drop_duplicates方法去除重复的(LAT, LON)组合，并保留唯一值
unique_lat_lon = lat_lon_data.drop_duplicates()

# 打印或进一步处理唯一的(LAT, LON)组合
print(unique_lat_lon)

unique_lat_lon.to_csv(r"C:\FIA-Data\FIA数据\整理后美国50州数据\P2-chapter2\COND\COND_coordinate\1_cordinate.csv", index = False)

