import pandas as pd
# brics = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/brics.csv',index_col =0)
#
#
# #the original variables was lab (label) and row
# #for x, y in brics.iterrows():
#     #print(x)
#     #print(y)
#     #print(x, ':', y['capital'])
#
#
#     # add new column: name length
#     #brics.loc[x, 'name_length'] = len(y['country'])
#
# brics['name_length'] = brics['country'].apply(len) # this is for the whole loop above to add new column
#
# print(brics)

cars = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/cars.csv',index_col =0)
#for lab, row in cars.iterrows():
    #print(lab, ':', row['cars_per_cap'])
    #cars.loc[lab, 'COUNTRY'] = row['country'].upper()

cars['COUNTRY'] = cars['country'].apply(str.upper)

print(cars)
