import pandas as pd
cars = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/cars.csv',index_col =0)
# print (cars[['country', 'drives_right']])
#
# print(cars.iloc[[0,1,2]]) #1st 3 obs
# print(cars.iloc[[3,4,5]]) #4,5,6 obs

print(cars.iloc[[5],[2]])
