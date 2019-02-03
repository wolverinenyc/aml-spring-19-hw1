import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import savefig

df = pd.read_csv('mpg.csv',index_col=0)

#   DICTIONARY TO ASSIGN COLORS AND LABELS TO EACH DRIVE TYPE
cdict = {'f':'y', 'r':'b', '4':'k'}
labeldict = {'f':'FWD', 'r':'RWD', '4':'4WD'}

#   EXAMPLE FIGURE OF OVERLAPPING POINTS: Fig 18.1

fig,ax = plt.subplots(figsize=(6,6))

for g in ['r','4','f']:
    subdf = df[df['drv']==g]
    ax.scatter(subdf['displ'],subdf['cty'],marker='o',
               c=cdict[g],s=60,label=labeldict[g])

ax.set_ylim((8,37))
ax.set_yticks(list(range(10,40,5)))
ax.legend(loc=0,title="drive train")
ax.set_xlabel("displacement (l)")
ax.set_ylabel("fuel economy (mpg)")
savefig('figure18.1_overlapping_points.png', bbox_inches='tight')


#   OVERLAPPING POINTS WITH PARTIAL TRANSPARENCY: Fig 18.2

fig,ax = plt.subplots(figsize=(6,6))

for g in ['r','4','f']:
    subdf = df[df['drv']==g]
    ax.scatter(subdf['displ'],subdf['cty'],marker='o', alpha=0.3,
               c=cdict[g],s=60,label=labeldict[g])

ax.set_ylim((8,37))
ax.set_yticks(list(range(10,40,5)))
ax.legend(loc=0,title="drive train")
ax.set_xlabel("displacement (l)")
ax.set_ylabel("fuel economy (mpg)")
savefig('figure18.2_add_transparency.png', bbox_inches='tight')



#   OVERLAPPING POINTS WITH JITTERING (small shifts in x,y coordinates): Fig 18.3

np.random.seed(123)
fig,ax = plt.subplots(figsize=(6,6))

for g in ['r','4','f']:
    subdf = df[df['drv']==g]
    randnoise = np.random.normal(0,1,size=(len(subdf),2))/15
    ax.scatter(subdf['displ']+randnoise[:,0],subdf['cty']+randnoise[:,1],
               marker='o', c=cdict[g],s=60,label=labeldict[g], alpha=0.5)

ax.set_ylim((8,37))
ax.set_yticks(list(range(10,40,5)))
ax.legend(loc=0,title="drive train")
ax.set_xlabel("displacement (l)")
ax.set_ylabel("fuel economy (mpg)")
savefig('figure18.3_add_jitter.png', bbox_inches='tight')



#   OVERLAPPING POINTS WITH TOO MUCH JITTERING (small shifts in x,y coordinates): Fig 18.4

np.random.seed(123)
fig,ax = plt.subplots(figsize=(6,6))

for g in ['r','4','f']:
    subdf = df[df['drv']==g]
    randnoise = np.random.normal(0,1,size=(len(subdf),2))/5
    ax.scatter(subdf['displ']+randnoise[:,0],subdf['cty']+randnoise[:,1],
               marker='o', c=cdict[g],s=60,label=labeldict[g], alpha=0.5)

ax.set_ylim((8,37))
ax.set_yticks(list(range(10,40,5)))
ax.legend(loc=0,title="drive train")
ax.set_xlabel("displacement (l)")
ax.set_ylabel("fuel economy (mpg)")
savefig('figure18.4_toomuch_jitter.png', bbox_inches='tight')


