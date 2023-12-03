#import ctypes
#
#fortran_lib = ctypes.CDLL('./Flash_frought_identification.so')
##fortran_lib.flashdrought()
#for item in dir(fortran_lib):
#    if callable(getattr(fortran_lib, item)):
#        print(item)
from python_mod import test

a = [41, 41,30,35,31,47,35,28,23,17,17,20,21,18,5,35,37,48,46,41,37,32,17,1,23,41,18,21, 41,40,39,38,37,36,35,40,34,33,32,31,19,21,30,29,28,40,27,26,25,11,24,23,22,43,21,20,19,18,17,21,41,31,31,31,32,32,33,24,21,21,26,23,23,23,23,23,23,23,23,23,23,21,32,32,32,32,32,32,32,32,32,32,32,32,32,32,19,20,21]
b = [0, 1, 2, 3]
drt = [0] * len(a)
b, drt, osev, odur, ospd = test.flashdrought(a)
num_of_flash_drought, mean_duration_flash_droughts, mean_severity_flash_droughts, mean_speed_flash_droughts = b
num_of_flash_drought = int(num_of_flash_drought)
duration_of_each_flash_drought = odur[:num_of_flash_drought]
severtiy_of_each_flash_drought = osev[:num_of_flash_drought]
onset_speed_of_each_flash_drought = ospd[:num_of_flash_drought]