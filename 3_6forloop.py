# fam = [1.73, 1.71, 1.68,1.89]
# for height in fam:
#     print(height)

# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# for i, area in enumerate(areas, start = 1):
#     print('room', i, ':', area)

#loop for list
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for room, area in house:
    print ('the', room, 'is ', area, ' sqm')

# loop for dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
for country, capital in europe.items():
    print('the capital of ', country, 'is', capital)
