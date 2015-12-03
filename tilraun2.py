from pandas import *
import numpy as np
import pandas as pd

settings = {}
settings['encoding'] = 'utf-8'
settings['sep'] = ';'
settings['dayfirst'] = True
settings['index_col'] = 0

skjal = pd.read_csv('mannfjoldi.csv', **settings)
skjal = skjal.apply(pd.to_numeric, errors='coerce') 
#gæti þurft að update-a pandas til að pd.to_numeric virkar

colfjol = print(len(skjal.columns))
s1 = [i.strip().replace(' ','_') for i in skjal[0:colfjol]]
"""
[print(i,end=", ") for i in skjal[0:colfjol]]
x = input("\nVeldu flokk: ")

stdev = np.std(skjal[x])
meðaltal = np.mean(skjal[x])
miðgildi = np.median(skjal[x])
"""
skjal = skjal[-100:].dropna()
d = {}
d['Staðalfrávik'] = np.std(skjal)
d['Meðaltal'] = np.mean(skjal)
#skiptir ekki máli hvort maður noti skjal.apply eða np.brah(skjal) nema fyrir median
d['Miðgildi'] = np.median(skjal, axis=0)
df = pd.DataFrame(d)
print(df)


#-------------------------Operation Tilgáta-----------------------------#





