import pandas as pd
import numpy as np
from scipy.stats import poisson

poi=pd.read_csv("../../Documentos/PronosticosDeportivos/po_premier_league.csv")

subset=poi[["Unnamed: 7","Unnamed: 8","Unnamed: 9","Unnamed: 10","Unnamed: 11","Unnamed: 12","Unnamed: 13","Unnamed: 14","Unnamed: 15","Unnamed: 16","Unnamed: 17","Unnamed: 18","Unnamed: 19","Unnamed: 20","Unnamed: 21","Unnamed: 22"]]
subset=subset[4:24]
subset=subset.to_numpy()
gol=pd.read_csv("../../Documentos/PronosticosDeportivos/po_premier_league.csv")
gol=gol["Unnamed: 8"]
gol=gol.to_numpy()
promedio_de_goles=float(gol[25])

Probabilidad=0
ProGol=0
key='s'
while(key=='s' or key=='S'):
	i=int(input("Elige el Equipo Local: "))
	j=int(input("Elige el Equipo Visita : "))
	IAL=float(subset[i][12])
	IDL=float(subset[i][13])
	IAV=float(subset[j][14])
	IDV=float(subset[j][15])
	Local=IAL*IDV*promedio_de_goles 
	Visita=IAV*IDL*promedio_de_goles
	print("\n")
	print(Local)
	print(Visita)
	print("\n")
	k=i
	k1=j
	ProG=0
	ProG1=0
	ProG2=0
	for i in range(0,7):
		for j in range(0,7):
			Probabilidad=poisson.pmf(i,Local)*poisson.pmf(j,Visita)
			if(Probabilidad>.01):
				print("Local : ",subset[k][0], i ,"vs" ,"Visita : ",subset[k1][0],j, Probabilidad)
				
			if(j>i):
				ProG=ProG+Probabilidad
			if (i>j):
				ProG1=ProG1+Probabilidad
			if(i==j):
				ProG2=ProG2+Probabilidad
	Gol=0
	Gol1=0
	for i in range(0,7):
		for j in range(0,7):
			ProGol=poisson.pmf(i,Local)*poisson.pmf(j,Visita)
			if(i+j>3):
				Gol=Gol+ProGol
			if(i+j<=3):
				Gol1=Gol1+ProGol
	print("Local : ",ProG1*100)
	print("Emapate : ",ProG2*100)
	print("Visita : ", ProG*100)
	print("Mas de 2.5 : ", Gol)
	print("Menos de 2.5 : ", Gol1)
	print("Suma de Goles : ", Gol+Gol1)
	key=input("Desea Continuar S/N : ")



