import pandas as pd
from scipy.stats import shapiro
import numpy as np

# 读取CSV文件
data = pd.read_csv(r"C:\Users\zhijiel\Downloads\ERA51981-2022\1981-2022-day (moisture+t2m+tp)\combine-results.csv")

# 指定要检验的5个变量的名称
variables_to_test = ["flash_drought"]

# 设置显著性水平
alpha = 0.05

# 创建一个循环，对每个指定的变量进行正态性检验
for var in variables_to_test:
    variable_data = data[var].dropna()  # 删除NaN值
    variable_data = variable_data.values.flatten()  # 转换为一维数组
    
    # 运行Shapiro-Wilk测试
    shapiro_test_stat, shapiro_test_pvalue = shapiro(variable_data)
    
    # 打印变量名称和测试结果
    print("Variable:", var)
    print("Shapiro-Wilk Test p-value:", shapiro_test_pvalue)
    
    # 判断是否符合正态分布
    if shapiro_test_pvalue < alpha:
        print("The variable does not follow a normal distribution (reject H0).")
    else:
        print("The variable follows a normal distribution (fail to reject H0).")
    
    print()
