
import pandas as pd

# 读取文件1和文件2
df1 = pd.read_csv(r"C:\FIA-Data\FIA数据\整理后美国50州数据\P2-chapter2\COND\COND_coordinate\1_selected variables - Copy.csv")
df2 = pd.read_csv(r"C:\FIA-Data\FIA数据\整理后美国50州数据\P2-chapter2\COND\COND_coordinate\1_selected variables_FD - Copy.csv")


# 使用merge函数合并两个DataFrame，使用LAT、LON和INVYR作为合并键
merged_df = pd.merge(df1, df2, on=['LAT', 'LON', 'INVYR'], how='inner')

# 去重合并后的数据
merged_df.drop_duplicates(subset=['LAT', 'LON', 'INVYR'], inplace=True)

# 保留文件1中的INVYR、LAT和LON列
filtered_df1 = merged_df[['INVYR', 'LAT', 'LON']]

# 将结果保存到新的CSV文件
filtered_df1.to_csv('筛选结果1.csv', index=False)
