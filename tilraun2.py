from pandas import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Lesaskra(nafn):
	settings = {}
	settings['encoding'] = 'utf-8'
	settings['sep'] = ';'
	settings['dayfirst'] = True
	settings['index_col'] = 0

	skjal = pd.read_csv(nafn, **settings)
	skjal = skjal.apply(pd.to_numeric, errors='coerce') 
	#gæti þurft að update-a pandas til að pd.to_numeric virkar

	colfjol = len(skjal.columns)
	s1 = [i.strip().replace(' ','_') for i in skjal[0:colfjol]]

	skjal = skjal.dropna()
	return skjal

skjal1=Lesaskra('mannfjoldi.csv')
skjal2=Lesaskra('SAM04101.csv')	

skjal = pd.concat([skjal1,skjal2],axis=1, join_axes=[skjal1.index]).dropna()

d = {}
d['Staðalfrávik'] = np.std(skjal, axis=0)
d['Meðaltal'] = np.mean(skjal, axis=0)
#skiptir ekki máli hvort maður noti skjal.apply eða np.brah(skjal) nema fyrir median
d['Miðgildi'] = np.median(skjal, axis=0)
d['Max'] =np.max(skjal, axis=0)
d['Min']=np.min(skjal, axis=0)
df = pd.DataFrame(d)

#saman =pd.concat([df1,df2])
print(df)
skjal.to_csv('Nidurstodur.csv')
df.to_csv('Nidurstodur2.csv')
#print(skjal1[,"\n",skjal2['Alls'])
#print(skjal[-25:])
"""
[print(i,end=", ") for i in skjal[0:colfjol]]
x = input("\nVeldu flokk: ")

stdev = np.std(skjal[x])
meðaltal = np.mean(skjal[x])
miðgildi = np.median(skjal[x])
"""

#-------------------------Operation Tilgáta-----------------------------#





