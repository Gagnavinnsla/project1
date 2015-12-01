import pandas as pd
import numpy as np
import csv as csv


def openfile(Nameoffile):
	Vektor=[]
	Boolian=True
	with open(Nameoffile) as csvfile:
		File = csv.reader(csvfile, delimiter=';')

		for row in File:
				if Boolian:
					Header=row
					Boolian=False
				else:
						Vektor.append((row))
	return Header,Vektor

Header1,Vektor1=openfile('SAM04101.csv')
Header2,Vektor2=openfile('mannfjoldi.csv')

Ar1=Header1.index('Ár')
Ar2=Header2.index('Ár')
class Found(Exception): pass
Boolian=True
counter=0
try:
	for i in range(len(Vektor1)):
		for j in range(len(Vektor2)):
			if Vektor1[i][Ar1] == Vektor2[j][Ar2]:
				Index1=i
				Index2=j
				raise Found
except Found:
	print('Worked')

try:
	while Vektor1[Index1+counter][Ar1] == Vektor2[Index2+counter][Ar2]:
		counter+=1
except IndexError:
	pass
print(Vektor1[Index1][Ar1])
print(Vektor2[Index2][Ar2])
print('--------------------------')
for i in range(counter):
	print(Vektor1[Index1+i][Ar1])