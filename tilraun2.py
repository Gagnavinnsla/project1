import numpy as np; import pandas as pd; import matplotlib.pyplot as plt; import pylab

def Lesaskra(nafn):
	settings = {'encoding':'utf-8', 'sep':';', 'dayfirst':True}
	skjal = pd.read_csv(nafn, **settings)
	skjal.set_index('Ár',inplace=True)
	skjal = skjal.apply(pd.to_numeric, errors='coerce').dropna(axis=1,how='all')  #gæti þurft að update-a pandas til að pd.to_numeric virkar
	return skjal

Valinskra=input('Veldu skrá til að bera saman við "Afbrot.csv":')
skjal1=Lesaskra('Afbrot.csv')
skjal2=Lesaskra(Valinskra)	
skjal = pd.concat({'mannfjoldi.csv': skjal1,'Afbrot.csv': skjal2},axis=1, join_axes=[skjal1.index]).dropna()
df = pd.DataFrame({'Staðalfrávik':np.std(skjal),'Meðaltal':np.mean(skjal),'Miðgildi':np.median(skjal,axis=0),'Max':np.max(skjal), 'Min':np.min(skjal)})

[print(i,end="; ") for i in skjal]
x1 = input("\nVeldu skrá: ")
x2 = input("\nVeldu undirflokk: ")
y1 = input("\nVeldu skrá: ")
y2 = input("\nVeldu samanburðarflokk: ")

plt.style.use('ggplot')
df2=pd.DataFrame({x2:skjal[x1][x2].pct_change(),y2:skjal[y1][y2].pct_change()}).dropna(axis=0)
print('Fylgni valinna gagna er: ', np.corrcoef(df2[x2],df2[y2])[0][1])
df2.plot()
plt.show()

skjal.to_csv('Gögn.csv')
df.to_csv('Tolfraedi.csv')
df2.to_csv('breytingFlokka.csv')
