import numpy as np; import pandas as pd; import matplotlib.pyplot as plt; import pylab

def Lesaskra(nafn):
	settings = {'encoding':'utf-8', 'sep':';', 'dayfirst':True}
	skjal = pd.read_csv(nafn, **settings)
	skjal.set_index('Ár',inplace=True)
	skjal = skjal.apply(pd.to_numeric, errors='coerce').dropna(axis=1,how='all')
	return skjal

Valinskra=input('Veldu skrá til að bera saman við <Afbrot.csv>: ')
skjal1=Lesaskra('Afbrot.csv')
skjal2=Lesaskra(Valinskra)	
skjal = pd.concat({'Afbrot.csv': skjal1, Valinskra: skjal2},axis=1, join_axes=[skjal1.index]).dropna()
df = pd.DataFrame({'Staðalfrávik':np.std(skjal),'Meðaltal':np.mean(skjal),'Miðgildi':np.median(skjal,axis=0),'Max':np.max(skjal), 'Min':np.min(skjal)})

[print(i,end="; ") for i in skjal]
x1 = input("\nVeldu skrá: ")
x2 = input("\nVeldu undirflokk: ")
y1 = input("\nVeldu skrá: ")
y2 = input("\nVeldu samanburðarflokk: ")

plt.style.use('ggplot')
df2=pd.DataFrame({x2:skjal[x1][x2].pct_change(),y2:skjal[y1][y2].pct_change()}).dropna(axis=0)

df2.plot()
plt.title('Fylgni valina gagna er: {}'.format(np.corrcoef(df2[x2],df2[y2])[0][1]))
plt.show()

skjal.to_csv('Gögn.csv')
df.to_csv('Tolfraedi.csv')
df2.to_csv('BreytingFlokka.csv')

"""
Kóðinn er pandas útgáfa af hálfkláraða ~lowlevel kóðanum projectalpha, sem var eyddur út af línufjölda.
Forritið byrjar á að lesa inn .csv skrár inn í pandas dataframe eftir völdum stillingum. Setur árin sem index, breytir öllu í tölur,
 og eyðir dálkum sem innihéldu bara texta (Taka má fram að það þarf version 1.10.1 af pandas til að pd.to_numeric virki og skrárnar hafi encoding=utf-8)

Síðan eru gögnin sett saman með concat þar sem árin eru eins og eyðir út NAN. Með MultiIndexing eru dálkarnir merkir með skjalsnafninu til að
koma í veg fyrir misskilning ef dálkaheitin eru þau sömu.

Við búum til grunn tölfræðigögnin í df en notuðum þau síðan ekkert meir, en auðvelt er að bæta við öllum útreikningum sem manni dettur í hug.

Við leyfum notendanum að velja gögnin sem hann vill taka inn, upp á þægileika fyrir báða aðila. Þannig að í stað þess að gefa risastórt fylgnifylki
og fullt af myndum, að finna bara það sem notandinn vill. Gallinn liggur í því að nöfnin verða skrifuð rétt og forritið crashar ef þau eru vitlaust
inn sleginn, við hefðum getað sett þau inn í "try:" lykkju eins og í "functionsalpha.py" en það kostar of margar línur.

Síðan notum við pct.change til að finna breytinguna milli ára og np.corrcoef til að finna fylgnina og teiknum þetta síðan upp, við hefðum örruglega
geta sett myndirnar betur upp, en við runnum út um tíma.
"""
