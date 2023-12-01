from netCDF4 import Dataset
import numpy as np
from scipy import stats
from tqdm import tqdm

data_file = "./data/merged.nc"
data = Dataset(data_file, 'r')
swvl4_40years = data.variables['swvl4'][:]

year_dim, time_dim, longitude_dim, latitude_dim = swvl4_40years.shape

average_swvl4_every_time_window_length = []
time_window_length = 5
for time_idx in range(0, time_dim, time_window_length):
    data = swvl4_40years[:, time_idx:time_idx+time_window_length, :, :]
    if data.shape[1] < time_window_length:
        break
    data = np.mean(data, axis=1, keepdims=True)
    average_swvl4_every_time_window_length.append(data)

average_swvl4_every_time_window_length = np.concatenate(average_swvl4_every_time_window_length, axis=1)


percentile_every_time_window_length = np.empty(average_swvl4_every_time_window_length.shape)

for longitude_idx in tqdm(range(longitude_dim), desc="longitude"):
    for latitude_idx in tqdm(range(latitude_dim), desc="latitude", leave=False):
        for time_idx in tqdm(range(average_swvl4_every_time_window_length.shape[1]), desc="time", leave=False):
            data = average_swvl4_every_time_window_length[:, time_idx, longitude_idx, latitude_idx]
            for year_idx in tqdm(range(year_dim), desc="year", leave=False):
                percentile = stats.percentileofscore(data, swvl4_40years[year_idx, time_idx, longitude_idx, latitude_idx])
                percentile_every_time_window_length[year_idx, time_idx, longitude_idx, latitude_idx] = percentile


data_file = "./data/percentile_every_time_window_length.nc"
nc = Dataset(data_file, 'w', format='NETCDF4')

year_dim = nc.createDimension('year', year_dim)
time_dim = nc.createDimension('time', average_swvl4_every_time_window_length.shape[1])
lon_dim = nc.createDimension('longitude', longitude_dim)
lat_dim = nc.createDimension('latitude', latitude_dim)

var = nc.createVariable('percentile', 'f4', ('year', 'time', 'longitude', 'latitude'))
var[:] = percentile_every_time_window_length
nc.close()

