#we use series rather than DataFrame for this purpose
import pandas as pd
import numpy as np
# brics = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/brics.csv',index_col =0)
# print(brics[brics['area']>8])
#
cars = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/cars.csv', index_col = 0)
# cars_maniac = cars[cars['cars_per_cap'] > 500]
# print(cars_maniac)

# cpc = cars['cars_per_cap']
# between = np.logical_and(cpc > 100, cpc < 500)
# medium = cars[between] #no need to put '' for between
# print(between)

print(cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)])
