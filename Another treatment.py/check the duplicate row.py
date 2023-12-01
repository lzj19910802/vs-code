# 读取CSV文件
df = pd.read_csv(r"C:\FIA-Data\FIA数据\整理后美国50州数据\P2-chapter2\COND\COND_coordinate\1_selected variables.csv")

# 检查是否有同时重复的行
duplicate_rows = df[df.duplicated(subset=["INVYR", "LAT", "LON"], keep=False)]

if not duplicate_rows.empty:
    print("有同时重复的行:")
    print(duplicate_rows)

    # 将具有重复的行导出为新的CSV文件
    duplicate_rows.to_csv(r"C:\FIA-Data\FIA数据\整理后美国50州数据\P2-chapter2\COND\COND_coordinate\1_selected variables-重复的行.csv", index=False)

    print("重复的行已导出到 duplicate_rows.csv 文件")
else:
    print("没有同时重复的行")
