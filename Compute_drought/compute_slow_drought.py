from netCDF4 import Dataset
from slow_mod import slowdrought_mod
import csv
from tqdm import tqdm

def slow_drought_identification(a):
    b, drt, osev, odur, ospd = slowdrought_mod.slowdrought(a)
    num_of_flash_drought, mean_duration_flash_droughts, mean_severity_flash_droughts, mean_speed_flash_droughts = b
    num_of_flash_drought = int(num_of_flash_drought)
    duration_of_each_flash_drought = odur[:num_of_flash_drought]
    severtiy_of_each_flash_drought = osev[:num_of_flash_drought]
    onset_speed_of_each_flash_drought = ospd[:num_of_flash_drought]
    drt = list(map(int, drt.tolist()))
    
    return num_of_flash_drought, mean_duration_flash_droughts, mean_severity_flash_droughts, mean_speed_flash_droughts, duration_of_each_flash_drought, severtiy_of_each_flash_drought, onset_speed_of_each_flash_drought, drt

single_year_file = "./data/1981-2020 original moisture/daily_mean_adaptor.mars.internal-1981_swvl4.nc"
data_single_year = Dataset(single_year_file, 'r')

longitudes_list = data_single_year.variables['longitude'][:]
latitudes_list = data_single_year.variables['latitude'][:]
times = data_single_year.variables['time'][:]


data_file = "./data/percentile_every_time_window_length.nc"
data = Dataset(data_file, 'r')
percentiles = data.variables['percentile'][:]
year_dim, time_dim, longitude_dim, latitude_dim = percentiles.shape

csv_file_path = "./data/slow_drought.csv"
base_year = 1981
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['year', 'longitude', 'latitude', 'num_of_flash_drought', 'mean_duration_flash_droughts', 'mean_severity_flash_droughts', 'mean_speed_flash_droughts', 'duration_of_each_flash_drought', 'severtiy_of_each_flash_drought', 'onset_speed_of_each_flash_drought', 'drt'])
    for year in tqdm(range(year_dim), desc="year"):
        for longitude in tqdm(range(longitude_dim), desc="longitude", leave=False):
            for latitude in tqdm(range(latitude_dim), desc="latitude", leave=False):
                percentile = percentiles[year, :, longitude, latitude]
                data = list(slow_drought_identification(percentile))
                writer.writerow([year+base_year, longitudes_list[longitude], latitudes_list[latitude]] + data)

