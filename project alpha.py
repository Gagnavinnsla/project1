import pandas as pd
import numpy as np
import csv as csv
import func


Nameoffile1='mannfjoldi-test.csv'
Nameoffile2='mannfjoldi-test2.csv'

Header1,Vektor1,Ar1=func.openfile(Nameoffile1)#'SAM04101.csv'
Header2,Vektor2,Ar2=func.openfile(Nameoffile2)

##Finnur tímabilið sem árin eru eins og lengd þess.
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

##Lætur notendann sækja flokinn sem við viljum skoða
indexinput1=func.Veljaflokk(Header1)
indexinput2=func.Veljaflokk(Header2)

## Býr til lista úr gögnunum sem notandinn valdi ásamt því að eyða út öllum nan línum
list1,counter,listdeleted1=func.Createlist(Vektor1,Index1,counter,indexinput1)

if (Nameoffile2==Nameoffile1) & (indexinput1==indexinput2):
	print("Indexinput:",indexinput1,indexinput2)
	list2=list1
else:
	for i in range(len(listdeleted1)):
		for j in range(len(Vektor2)):
			if Vektor2[j][Ar2]==listdeleted1[i][Ar1]:
				break
		del Vektor2[j]
		
	list2,counter,listdeleted2=func.Createlist(Vektor2,Index2,counter,indexinput2)
	print(len(listdeleted1),len(listdeleted2))
	for i in range(len(listdeleted2)):
		for j in range(len(Vektor1)):
			if Vektor1[j][Ar1]==listdeleted2[i][Ar2]:
				break
		del Vektor1[j]
		del list1[j]
for i in range(counter):
	print(Vektor1[i][Ar1],list1[i],Vektor2[i][Ar2],list2[i])
##Reiknar öðruvísi ef verið er að skoða mismunandi gögn og ef þau eru eins
if list1!=list2:

	Difference=[]
	ChangeinDifference=[]
	ratio=[]
	Changeinratio=[]
	for i in range(counter):
		Difference.append(list1[i]-list2[i])
		ratio.append(list1[i]/list2[i])
		if 0.00 in ratio:
			print("Data comparison invalid")
			exit()
	for i in range(counter-1):
		Changeinratio.append((ratio[i+1]/ratio[i]-1)*100)
	correlation=np.corrcoef(list1,list2)[0][1]
	for i in range(counter-1):
		print("%.2f %%" %(Changeinratio[i]))
elif list1==list2:
	print("Sami listi")
	variance=np.var(list1)
	std=np.std(list1)
	listmax=np.max(list1)
	listmin=np.min(list1)
	listsum=np.sum(list1)
	listmean=np.mean(list1)
	lnchange=[]
	change=[]
	for i in range(counter-1):
		change.append((list1[i+1]/list1[i]-1)*100)
		lnchange.append((np.log(list1[i+1]/list1[i])-1)*100)
else:
	print('God dammit')
"""
print(Vektor1[Index1][Ar1])
print(Vektor2[Index2][Ar2])
print('---------------------------')
for i in range(counter):
	print(Vektor1[Index1+i][Ar1])
"""
