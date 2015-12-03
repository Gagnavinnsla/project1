from pandas import *
import numpy as np
import pandas as pd
import csv as csv

settings = {}
settings['encoding'] = 'utf-8'
settings['sep'] = ';'
settings['dayfirst'] = True
settings['index_col'] = 0

skjal = pd.read_csv('mannfjoldi.csv', **settings)
skjal = skjal.apply(pd.to_numeric, errors='coerce')
colfjol = print(len(skjal.columns))
s1 = [i.strip().replace(' ','_') for i in skjal[0:colfjol]]


#[print(i,end=", ") for i in skjal[0:colfjol]]
#x = input("\nVeldu flokk: ")
#print(skjal[x])

df = {}
df['Staðalfrávik'] = skjal.apply(np.std, axis=0, reduce=False).dropna()


print(df)

#-------------------------Operation Tilgáta-----------------------------#


#tilgáta = input("Veldu ")

