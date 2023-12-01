

import pandas as pd
from semopy import Model


data = pd.read_csv(r"C:\FIA-Data\FIA数据\USA 50 states data after settling\P2-chapter2\New folder\latitude3-sem10000.csv")

# 定义 SEM 模型
model = """
    CARBON_UNDERSTORY_AG ~ flash_drought
    CARBON_UNDERSTORY_BG ~ flash_drought
    CARBON_DOWN_DEAD ~ flash_drought
    CARBON_LITTER ~ flash_drought
    CARBON_SOIL_ORG ~ flash_drought
    CARBON_STANDING_DEAD ~ flash_drought
    
"""
mod = Model(model)
res_opt = mod.fit(data)

estimates = mod.inspect()

print(res_opt)
print(estimates)

estimates.to_csv(r"C:\FIA-Data\FIA数据\USA 50 states data after settling\P2-chapter2\New folder\location_test_combine_sem2.csv")
