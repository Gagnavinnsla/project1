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
	listdeleted=[]
	i=0
	while i<counter:
		if Vektor[Index+i][indexinput].isdigit():
			list1.append(Vektor[Index+i][indexinput])
		else:
			listdeleted.append(Vektor[Index+i])
			del Vektor[Index+i]
			counter-=1
		i+=1
	return list1,counter,listdeleted
