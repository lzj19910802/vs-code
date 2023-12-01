# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:35:59 2023

@author: zhijiel
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. 读取CSV文件
df = pd.read_csv(r"C:\FIA-Data\FIA数据\USA 50 states data after settling\P2-chapter2\New folder\latitude3-sem.csv")

# 2. 选择要标准化的特征
features_to_normalize = df[['CARBON_DOWN_DEAD', 'CARBON_LITTER', 'CARBON_SOIL_ORG','CARBON_STANDING_DEAD','CARBON_UNDERSTORY_AG', 'CARBON_UNDERSTORY_BG', 'flash_drought', 'tp','t2m']]

# 3. 创建标准化对象
scaler = StandardScaler()

# 4. 对数据进行标准化
normalized_features = scaler.fit_transform(features_to_normalize)

# 5. 替换原始数据
df[['CARBON_DOWN_DEAD', 'CARBON_LITTER', 'CARBON_SOIL_ORG','CARBON_STANDING_DEAD','CARBON_UNDERSTORY_AG', 'CARBON_UNDERSTORY_BG', 'flash_drought', 'tp','t2m']] = normalized_features

# 6. 保存标准化后的数据（可选）
df.to_csv(r"C:\FIA-Data\FIA数据\USA 50 states data after settling\P2-chapter2\New folder\latitude3-sem-standard.csv", index=False)
