# http://www.caprinomics.com/projects/gdp-vs-life-expectancy/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches #for legend later
#use pwd to check the directory to the file for read_csv()
gapminder = pd.read_csv('/Users/apple/desktop/py4e/intermediatePython/gapminder.csv', index_col=0)


#since the population are big, we need to divide so the plot can fit into the frame
gapminder['pop'] = gapminder['population']/1000000
pop = gapminder['pop'].tolist()

#convert population to array for calculation later
np_pop = np.array(pop)
np_pop = np_pop * 2

#def the color the match the continent
def color_map(c):
 if c['cont'] == 'Asia':
     return 'red'
 elif c['cont'] == 'Europe':
     return 'green'
 elif c['cont'] == 'Africa':
     return 'blue'
 elif c['cont'] == 'Americas':
     return 'yellow'
 else:
     return 'black'

gapminder['color']=gapminder.apply(color_map, axis = 1)
col = gapminder['color'].tolist()

#start plotting
#using the population as size, color as defined above and alpha for transparency
plt.scatter(gapminder.gdp_cap, gapminder.life_exp, s=np_pop, c = col, alpha = 0.8)
plt.xscale('log')

#putting the label
plt.xlabel('GDP per Capita [USD]')
plt.ylabel('Life Expectancy')
plt.title('World Development in 2007')

#put the label for x-axis
tick_val =  [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)
# https://matplotlib.org/3.1.1/tutorials/intermediate/legend_guide.html
#put legend
red_patch = mpatches.Patch(color='red', label='Asia')
green_patch = mpatches.Patch(color='green', label='Europe')
blue_patch = mpatches.Patch(color='blue', label='Africa')
yellow_patch = mpatches.Patch(color='yellow', label='Americas')
black_patch = mpatches.Patch(color='black', label='Ocenia')
plt.legend(handles=[red_patch, green_patch, blue_patch, yellow_patch, black_patch])

#put the grid
plt.grid(True)

#save the figure
plt.savefig('/Users/apple/desktop/py4e/intermediatePython/gdpVsLifeExpectancy.png')

plt.show()


# plt.scatter(gapminder.gdp_cap, gapminder.life_exp)
# plt.xscale('log')
# plt.scatter(gapminder.population, gapminder.life_exp)

# plt.hist(gapminder.life_exp, bins = 5)
# plt.show()
# plt.clf()
#
# plt.hist(gapminder.life_exp, bins = 20)
# plt.show()
# plt.clf()
