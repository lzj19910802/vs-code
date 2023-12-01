from netCDF4 import Dataset
import os
import numpy as np

data_folder = "./data/1981-2020 original moisture"  # replace with your actual path
nc_files = [f for f in os.listdir(data_folder) if f.endswith('.nc')]



data = []
for file in nc_files:
    year = file.split('-')[1][:4]
    file_path = os.path.join(data_folder, file)
    nc_data = Dataset(file_path, 'r')
    time_dim = len(nc_data.variables['time'])
    longitude_dim = len(nc_data.variables['longitude'])
    latitude_dim = len(nc_data.variables['latitude'])
    time_dtype = nc_data.variables['time'].dtype
    longitude_dtype = nc_data.variables['longitude'].dtype
    latitude_dtype = nc_data.variables['latitude'].dtype
    swvl4_dtype = nc_data.variables['swvl4'].dtype
    break

year_dim = len(nc_files)

# merged nc file
merged_nc_file = os.path.join("data", 'merged.nc')
merged_nc = Dataset(merged_nc_file, 'w', format='NETCDF4')

year_dim = merged_nc.createDimension('year', year_dim)
time_dim = merged_nc.createDimension('time', time_dim)  # unlimited dimension
lon_dim = merged_nc.createDimension('longitude', longitude_dim)  # assuming 360 longitudes
lat_dim = merged_nc.createDimension('latitude', latitude_dim) 

var = merged_nc.createVariable('swvl4', swvl4_dtype, ('year', 'time', 'longitude', 'latitude'))

year_base = 1981

for file in nc_files:
    year = file.split('-')[1][:4]
    year = np.int64(year)
    nc_data = Dataset(os.path.join(data_folder, file), 'r')
    data = nc_data.variables['swvl4'][:]
    var[year - year_base, :, :, :] = data.copy()
    
#print(merged_nc.variables.keys())
merged_nc.close()

#print(merged_nc.variables['year'][:])