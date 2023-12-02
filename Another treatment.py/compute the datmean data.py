# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:45:03 2023

@author: zhijiel
"""

import xarray as xr

# 打开NetCDF文件并加载数据集
data = xr.open_dataset(r"C:\Users\zhijiel\Downloads\Science\ERA5\hour-moisture\adaptor.mars.internal-1980-hour.nc")

# 选择您要处理的变量
variable = data[['swvl1', 'swvl2', 'swvl3']]

# 按时间对变量进行排序
variable = variable.sortby('time')

# 计算每日均值
daily_mean = variable.resample(time='D').mean(dim='time')

# 将每日均值保存为新的NetCDF文件
daily_mean.to_netcdf(r"C:\Users\zhijiel\Downloads\Science\ERA5\hour-moisture\adaptor.mars.internal-1980-day.nc")
