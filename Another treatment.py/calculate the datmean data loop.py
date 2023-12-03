import os
import xarray as xr

# 指定包含NetCDF文件的文件夹路径
folder_path = r"C:\Users\zhijiel\Downloads\ERA5--1981-2020\adaptor.mars,internal--1981-2020--hourly"

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)

# 循环处理每个文件
for file_name in file_list:
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)

    # 打开NetCDF文件
    data = xr.open_dataset(file_path)

    # 选择要计算日均值的变量
    variable = data[['t2m', 'tp', 'swvl1', 'swvl2', 'swvl3']]  # 用你的变量名称替换'your_variable'

    # 计算日均值
    daily_mean = variable.resample(time='D').mean(dim='time')

    # 构建保存日均值数据的输出文件路径
    output_file_path = os.path.join(r"C:\Users\zhijiel\Downloads\ERA5--1981-2020\adaptor.mars,internal--1981-2020--daily", f'daily_mean_{file_name}')

    # 将日均值数据保存为NetCDF文件
    daily_mean.to_netcdf(output_file_path)

    # 关闭NetCDF文件
    data.close()
