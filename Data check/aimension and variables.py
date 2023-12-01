import netCDF4 as nc

# 打开NetCDF文件
file_path = r"C:\Users\zhijiel\Downloads\ERA5--1981-2020(vocation treated)\adaptor.mars,internal--1981-2020--daily\swvl4-percentile\original data\1981-2020 original moisture\daily_mean_adaptor.mars.internal-1981_swvl4.nc"
nc_file = nc.Dataset(file_path, "r")

# 查看文件的维度信息
print("文件维度信息:")
for dim_name, dim_obj in nc_file.dimensions.items():
    print(f"Dimension Name: {dim_name}")
    print(f"Size: {len(dim_obj)}")

# 查看文件的变量信息
print("\n文件变量信息:")
for var_name, var_obj in nc_file.variables.items():
    print(f"Variable Name: {var_name}")
    print(f"Dimensions: {var_obj.dimensions}")
    print(f"Shape: {var_obj.shape}")
    print(f"Data Type: {var_obj.dtype}")
    if 'units' in var_obj.ncattrs():
        print(f"Units: {var_obj.units}")
    print()


a = nc_file.variables['latitude'][:]
b = nc_file.variables['longitude'][:]
c = nc_file.variables['time'][:]
# d = nc_file.variables['t2m'][:]
e = nc_file.variables['swvl4'][:]
# f = nc_file.variables['flash_drought'][:]

print(e)
# print('latitude',a)
# print('longitude',b)
# print('time',c)
# # print('t2m',d)
# # print('tp',e)
# print('flash_drought',f)


# # # 关闭文件
# # nc_file.close()


