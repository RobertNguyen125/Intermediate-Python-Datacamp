# Access DataFrame
# Column
# 1.  DataFrame['column1', 'column2']/ datatype is object
# 2.  DataFrame[['column1','colum2']]/ datatype is DataFrame
# Row: use slicing
# DataFrame [1:4]
#
# loc[]: label_base
# iloc[]: integer_position_base

import pandas as pd
brics = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/brics.csv', index_col=0)
#print(brics)

# print(brics[['country', 'capital']])
# print(brics[1:4])
#
# print(brics.loc[['RU', 'IN', 'CN'], ['country','capital']])

print(brics.iloc[[1,2,3],[0,1]])
