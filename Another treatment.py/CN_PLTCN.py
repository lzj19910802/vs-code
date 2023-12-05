# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:47:51 2023

@author: zhijiel
"""

import pandas as pd

# 读取CSV文件1和CSV文件2
df1 = pd.read_csv(r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.4_PLOT\AR_PLOT.csv")
df2 = pd.read_csv(r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\AR_COND.csv")


# 删除CSV文件2中的"CN"列
df2.drop(columns=['CN'], inplace=True)

# 使用merge函数将两个数据框合并，基于"cn"和"plt_cn"列进行匹配
merged_df = df2.merge(df1[['CN', 'LAT', 'LON']], left_on='PLT_CN', right_on='CN', how='left')


print(merged_df)


# 删除多余的"cn"列


# 将合并后的数据保存到新文件中
merged_df.to_csv(r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\AR_COND1.csv", index=False)
