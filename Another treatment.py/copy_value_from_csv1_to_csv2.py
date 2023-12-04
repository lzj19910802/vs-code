

import pandas as pd


csv_file1 = r"C:\zhijie_project\data\flash_drought.csv"
csv_file2 = r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\New folder\VA_COND+PLOT_selected_location.csv"

df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)

merged_df = pd.merge(df2, df1[['year', 'longitude', 'latitude', 'num_of_flash_drought','mean_duration_flash_droughts', 'mean_severity_flash_droughts', 'mean_speed_flash_droughts']], 
                     on=['year', 'longitude', 'latitude'], 
                     how='left')

output_file = r"C:\FIA-Data\FIA数据\USA southern 13 states after settling\P2-chapter2\2.5_COND\New folder\VA_COND+PLOT_selected_location_value.csv"
merged_df.to_csv(output_file, index=False)

print(f"Merged data saved to {output_file}")
