from pandas import *
import numpy as np
import pandas as pd
import csv as csv

settings = {}
settings['encoding'] = 'utf-8'
settings['sep'] = ';'
#settings['parse_dates'] = ['Date']
settings['dayfirst'] = True
settings['index_col'] = 0

#skjal = read_csv('mannfjoldi.csv', delimiter=';', index_col=0)
#skjal = skjal.columns.strip().replace(' ','_')
#print(skjal[10:])
skjal = pd.read_csv('mannfjoldi.csv', **settings)
#df = skjal.ix[10:, ['Árleg fjölgun', 'Fjölgun', 'Aðfluttir umfram brottflutta',"Fæddir umfram dána"]]
colfjol = print(len(skjal.columns))
s1 = [i.strip().replace(' ','_') for i in skjal[0:colfjol]]
print(skjal[:10])