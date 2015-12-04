import numpy as np; import pandas as pd; import matplotlib.pyplot as plt; import pylab

def Lesaskra(nafn):
	settings = {'encoding':'utf-8', 'sep':';', 'dayfirst':True}
	skjal = pd.read_csv(nafn, **settings)
	skjal.set_index('Ár',inplace=True)
	skjal = skjal.apply(pd.to_numeric, errors='coerce').dropna(axis=1,how='all')  #gæti þurft að update-a pandas til að pd.to_numeric virkar
	return skjal

skjal1=Lesaskra('mannfjoldi.csv')
skjal2=Lesaskra('Afbrot.csv')	
skjal = pd.concat({'mannfjoldi.csv': skjal1,'Afbrot.csv': skjal2},axis=1, join_axes=[skjal1.index]).dropna()

df = pd.DataFrame({'Staðalfrávik':np.std(skjal),'Meðaltal':np.mean(skjal),'Miðgildi':np.median(skjal,axis=0),'Max':np.max(skjal), 'Min':np.min(skjal)})

print(skjal.columns)
"""
x1 = input("\nVeldu skrá: ")
x2 = input("\nVeldu flokk: ")
y1 = input("\nVeldu skrá: ")
y2 = input("\nVeldu samanburðarflokk: ")

fylgni = np.corrcoef(skjal[x1][x2].pct_change(), skjal[y1][y2].pct_change())[0][1]


skjal[x1][x2].pct_change().plot()
skjal[y1][y2].pct_change().plot()
plt.show()

skjal.to_csv('Nidurstodur.csv')
df.to_csv('Nidurstodur2.csv')
"""