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
for i in range(len(Vektor1)):
	for j in range(len(Vektor2)):
		if Vektor1[i][Ar1] == Vektor2[j][Ar2]:
			Index1=Vektor1[Ar1][i].index()
			print('True')
print(Vektor1[Index1][Ar1])

