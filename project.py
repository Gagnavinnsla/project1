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
print(Header1)