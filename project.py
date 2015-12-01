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
		Ar=Header.index('Ár')
	return Header,Vektor,Ar

Header1,Vektor1,Ar1=openfile('SAM04101.csv')
Header2,Vektor2,Ar2=openfile('mannfjoldi.csv')

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
	pass

try:
	while Vektor1[Index1+counter][Ar1] == Vektor2[Index2+counter][Ar2]:
		counter+=1
except IndexError:
	pass

def Veljaflokk(Header,Vektor,Index,counter):
	Boolian=True
	while Boolian==True:
		try:
			[print(i,end=", ") for i in Header]
			indexinput=Header.index(input("\nVeldu flokk:\n"))
			Boolian=False
		except ValueError:
			print("\nReyndu aftur\n")
			continue
	list1=[]
	for i in range(counter):
		list1.append(Vektor[Index+i][indexinput])
	list1=[int(i) for i in list1]
	return list1

list1=Veljaflokk(Header1,Vektor1,Index1,counter)
list2=Veljaflokk(Header2,Vektor2,Index2,counter)
if list1!=list2:
	Difference=list1-list2
	for i in range(counter-1)
		ChangeinDifference=Difference[i+1]/Difference[i]
	correlation=np.corrcoef(list1,list2)[0][1]
"""
print(Vektor1[Index1][Ar1])
print(Vektor2[Index2][Ar2])
print('--------------------------')
for i in range(counter):
	print(Vektor1[Index1+i][Ar1])
"""