import csv as csv
import numpy as np

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


def Veljaflokk(Header):
	Boolian=True
	while Boolian==True:
		try:
			[print(i,end=", ") for i in Header]
			indexinput=Header.index(input("\nVeldu flokk:\n"))
			Boolian=False
		except ValueError:
			print("\nReyndu aftur\n")
			continue
	return indexinput

def Createlist(Vektor,Index,counter,indexinput):
	list1=[]
	listdeleted=[]
	i=0
	while i<counter:
		try: 
			Vektor[Index+i][indexinput]=float(Vektor[Index+i][indexinput])##Breyta í int?
			list1.append(Vektor[Index+i][indexinput])
			i+=1
		except ValueError:
			listdeleted.append(Vektor[Index+i])
			del Vektor[Index+i]
			counter-=1
	return list1,counter,listdeleted
