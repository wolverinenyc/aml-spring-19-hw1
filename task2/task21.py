"""
Replicate graph from Spurious Correlations:
Number People Drowned in pool vs Nicolas Cage Films
"""

import pandas as pd
from matplotlib import pyplot as plt
from pylab import savefig

df = pd.read_csv("task21data.csv")
df = df.rename(columns={'Unnamed: 0':'Year',
                        'NicholasCage':'Films'})
df.set_index('Year')

corr2 = df['Drownings'].corr(df['Films'])
corr1 = corr2 * 100

# NEED TO GENERATE DATA TO SMOOTH LINES

#   EDITING TITLE WITH MULTIPLE SIZES AND COLORS

fig = plt.figure(figsize=(8,3))
ax1 = plt.subplot(111)
ax2 = ax1.twinx()

#   TWO SMOOTH SCATTERPLOTS
lns1=ax1.plot(df['Year'],df['Drownings'],linewidth=1.0,color='r',marker='D',ms=4,label='Drownings in Pool')
lns2=ax2.plot(df['Year'],df['Films'],linewidth=1.0,color='k',marker='o',ms=4,label='Nic Cage Films')

plt.xlim((1999,2009))
plt.xticks(list(range(1999,2010)))

ax1.set_ylim((80,140))
ax1.set_ylabel('Swimming pool drownings',color='r')
ax1.set_yticks(list(range(80,160,20)))
ax1.set_yticklabels(['80 drownings','100 drownings','120 drownings','140 drownings'],
                     color='r')

ax2.set_ylim((0,6))
ax2.set_ylabel('Nicolas Cage',color='k')
ax2.set_yticks(list(range(0,7,2)))
ax2.set_yticklabels(['0 films','2 films','4 films', '6 films'],color='k')

# set legend below plot
box = ax1.get_position()
ax1.set_position([box.x0,box.y0+box.height*0.1,
                 box.width,box.height *0.9])

lns = lns1 + lns2
labs = [l.get_label() for l in lns]    
ax1.legend(lns, labs, loc='upper center', bbox_to_anchor=(0.5,-0.1),
          fancybox=True,shadow=True,ncol=2)

plt.figtext(0.5,1.1,'Number of people who drowned by falling into a pool',
            fontsize=16,ha='center', color='r')
plt.figtext(0.5,1.04,'correlates with',fontsize=10,ha='center',color='grey')
plt.figtext(0.5,0.97,'Films Nicolas Cage appeared in',
            fontsize=16,ha='center', color='k')
plt.figtext(0.5,0.92,'Correlation: {:.1f}% (r={:.6f})'.format(corr1,corr2),fontsize=10,ha='center',color='grey')
savefig('nic_cage_films_x_drownings.png', bbox_inches='tight')
