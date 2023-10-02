from tkinter import*
from random import*
import pygame
pygame.init()
aide_objet=["cube","barre","L1","L2","Z","S","T"]
list_objet=["cube","barre","L1","L2","Z","S","T"]
couleur=["black","red","yellow","sky blue","purple","light green","blue","orange","grey","white","test","red","yellow","sky blue","purple","light green","blue","orange","grey","grey"]
n=0
x=0
acceleration=10
time=10
y=0
j=0
A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
action=0
cadeau=0
verif = 0
ligne=4
scoreligne=0
mouvbarre=0
touche1sauv=""
ligne_supprimée=[]
rotation=0
vitesse=10

Malus1=0

spawn="cube"

quadrillageaffichagej1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def TetrisHard(arg1,touche1,touche2,touche3,touche4,nbcolonne):
    global quadrillage,C2j1,Cj1
    def objet():
        global quadrillage,spawn,rotation,color,Malus1,pluie1
        spawnapres()
        if spawn=="Z":
            quadrillage[1][2+4]=1
            quadrillage[2][2+4]=1
            quadrillage[1][1+4]=1
            quadrillage[2][3+4]=1
            color = 1
            rotation=1
        if spawn=="cube":
            quadrillage[1][2+4]=2
            quadrillage[1][3+4]=2
            quadrillage[2][2+4]=2
            quadrillage[2][3+4]=2
            color = 2
            rotation=1
        if spawn=="barre":
            quadrillage[1][1+4]=3
            quadrillage[1][2+4]=3
            quadrillage[1][3+4]=3
            quadrillage[1][4+4]=3
            color = 3
            rotation=1
        if spawn=="T":
            quadrillage[1][2+4]=4
            quadrillage[2][2+4]=4
            quadrillage[2][1+4]=4
            quadrillage[2][3+4]=4
            color = 4
            rotation=1
        if spawn=="S":
            quadrillage[2][2+4]=5
            quadrillage[2][3+4]=5
            quadrillage[1][3+4]=5
            quadrillage[1][4+4]=5
            color = 5
            rotation=1

        if spawn=="L1":
            quadrillage[1][1+4]=6
            quadrillage[1][2+4]=6
            quadrillage[1][3+4]=6
            quadrillage[2][3+4]=6
            color = 6
            rotation=1

        if spawn=="L2":
            quadrillage[2][1+4]=7
            quadrillage[2][2+4]=7
            quadrillage[2][3+4]=7
            quadrillage[1][3+4]=7
            color = 7
            rotation=1
        print(spawn)
        print("spawn ok")
        grille()
    def objetsuite():
        global quadrillageaffichagej1,list_objet,pieceapres,rotation,color,pluie1,Malus1
        quadrillageaffichagej1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        pieceapres=choice(list_objet)

        if pieceapres=="Z":
            quadrillageaffichagej1[1][2]=1
            quadrillageaffichagej1[2][2]=1
            quadrillageaffichagej1[1][1]=1
            quadrillageaffichagej1[2][3]=1
        if pieceapres=="cube":
            quadrillageaffichagej1[1][2]=2
            quadrillageaffichagej1[1][3]=2
            quadrillageaffichagej1[2][2]=2
            quadrillageaffichagej1[2][3]=2
        if pieceapres=="barre":
            quadrillageaffichagej1[1][1]=3
            quadrillageaffichagej1[1][2]=3
            quadrillageaffichagej1[1][3]=3
            quadrillageaffichagej1[1][4]=3
        if pieceapres=="T":
            quadrillageaffichagej1[1][2]=4
            quadrillageaffichagej1[2][2]=4
            quadrillageaffichagej1[2][1]=4
            quadrillageaffichagej1[2][3]=4
        if pieceapres=="S":
            quadrillageaffichagej1[2][2]=5
            quadrillageaffichagej1[2][3]=5
            quadrillageaffichagej1[1][3]=5
            quadrillageaffichagej1[1][4]=5
        if pieceapres=="L1":
            quadrillageaffichagej1[1][1]=6
            quadrillageaffichagej1[1][2]=6
            quadrillageaffichagej1[1][3]=6
            quadrillageaffichagej1[2][3]=6
        if pieceapres=="L2":
            quadrillageaffichagej1[2][1]=7
            quadrillageaffichagej1[2][2]=7
            quadrillageaffichagej1[2][3]=7
            quadrillageaffichagej1[1][3]=7

        print(pieceapres)
        print("pieceapres ok")
        grilleaffichage1()
    def changepiece(event):
        global spawn,rotation
        test=[]
        acte=0
        for i in range (a):
            for j in range (b):
                if quadrillage[i][j]>0 and quadrillage[i][j]<8:
                    test.append(i)
                    test.append(j)
        if mouvbarre==1:
            acte=1
        if len(test)>0:
            if spawn=="L2" and rotation==1 and test[1]<nbcolonne-1 and acte==0 and quadrillage[test[4]-1][test[5]+1]<=7 and quadrillage[test[2]-2][test[3]+2]<=7 and quadrillage[test[0]+1][test[1]+1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0 ######
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]+1]=7
                quadrillage[test[2]-2][test[3]+2]=7
                quadrillage[test[4]-1][test[5]+1]=7
                quadrillage[test[6]][test[7]]=7
                rotation=2
                acte=1
            if spawn=="L2" and rotation==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage[test[2]+1][test[3]+1]<=7 and quadrillage[test[0]+2][test[1]+2]<=7 and quadrillage[test[6]+1][test[7]-1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+2][test[1]+2]=7
                quadrillage[test[2]+1][test[3]+1]=7
                quadrillage[test[4]][test[5]]=7
                quadrillage[test[6]+1][test[7]-1]=7
                rotation=3
                acte=1
            if spawn=="L2" and rotation==3 and test[1]>0 and  acte==0 and quadrillage[test[2]+1][test[3]-1]<=7 and quadrillage[test[6]-1][test[7]-1]<=7 and quadrillage[test[4]+2][test[5]-2]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]][test[1]]=7
                quadrillage[test[2]+1][test[3]-1]=7
                quadrillage[test[4]+2][test[5]-2]=7
                quadrillage[test[6]-1][test[7]-1]=7
                rotation=4
                acte=1
            if spawn=="L2" and rotation==4 and test[1]>0 and acte==0 and quadrillage[test[6]-2][test[7]-2]<=7 and quadrillage[test[4]-1][test[5]-1]<=7 and quadrillage[test[2]][test[3]]<=7 and quadrillage[test[0]-1][test[1]+1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]-1][test[1]+1]=7
                quadrillage[test[2]][test[3]]=7
                quadrillage[test[4]-1][test[5]-1]=7
                quadrillage[test[6]-2][test[7]-2]=7
                rotation=1
                acte=1
            if spawn=="L1" and rotation==1 and acte==0 and quadrillage[test[0]-1][test[1]+2]<=7 and quadrillage[test[2]-1][test[3]+1]<=7 and quadrillage[test[6]-1][test[7]-1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]-2][test[1]+2]=6
                quadrillage[test[2]-1][test[3]+1]=6
                quadrillage[test[4]][test[5]]=6
                quadrillage[test[6]-1][test[7]-1]=6
                rotation=2
                acte=1
            if spawn=="L1" and rotation==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage[test[4]-1][test[5]+1]<=7 and quadrillage[test[2]+1][test[3]+1]<=7 and quadrillage[test[0]+2][test[1]+2]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[0]+2][test[1]+2]=6
                quadrillage[test[2]+1][test[3]+1]=6
                quadrillage[test[4]-1][test[5]+1]=6
                quadrillage[test[6]][test[7]]=6
                rotation=3
                acte=1
            if spawn=="L1" and rotation==3  and acte==0 and quadrillage[test[0]+1][test[1]+1]<=7 and quadrillage[test[6]+2][test[7]-2]<=7 and quadrillage[test[4]+1][test[5]-1]<=7:
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]+1]=6
                quadrillage[test[4]+1][test[5]-1]=6
                quadrillage[test[6]+2][test[7]-2]=6
                rotation=4
                acte=1
            if spawn=="L1" and rotation==4 and test[1]>1 and acte==0 and quadrillage[test[2]+1][test[3]-1]<=7 and quadrillage[test[6]-2][test[7]-2]<=7 and quadrillage[test[4]-1][test[5]-1]<=7:
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]][test[1]]=6
                quadrillage[test[2]+1][test[3]-1]=6
                quadrillage[test[4]-1][test[5]-1]=6
                quadrillage[test[6]-2][test[7]-2]=6
                rotation=1
                acte=1
            if spawn=="Z" and rotation==1 and acte==0 and quadrillage[test[2]+2][test[3]]<=7 and quadrillage[test[0]][test[1]+2]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[0]][test[1]+2]=1
                quadrillage[test[2]+2][test[3]]=1
                rotation=2
                acte=1
            if spawn=="Z" and rotation==2 and acte==0 and test[1]>1 and quadrillage[test[6]-1][test[7]+1]<=7 and quadrillage[test[2]-1][test[3]-1]<=7 and quadrillage[test[4]][test[5]-1]<=7 and quadrillage[test[0]][test[1]-1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]][test[1]-1]=1
                quadrillage[test[4]][test[5]-1]=1
                quadrillage[test[2]-1][test[3]-1]=1
                quadrillage[test[6]-1][test[7]+1]=1
                rotation=1
                acte=1
            if spawn=="S" and rotation==1 and acte==0 and quadrillage[test[4]-1][test[5]]<=7 and quadrillage[test[2]+1][test[3]-2]<=7 and quadrillage[test[6]+1][test[7]]<=7 and quadrillage[test[0]+1][test[1]]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[0]+1][test[1]]=5
                quadrillage[test[6]+1][test[7]]=5
                quadrillage[test[2]+1][test[3]-2]=5
                quadrillage[test[4]-1][test[5]]=5
                rotation=2
                acte=1
            if spawn=="S" and rotation==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage[test[6]-1][test[7]-1]<=7 and quadrillage[test[4]-1][test[5]+1]<=7 and quadrillage[test[2]][test[3]+1]<=7 and quadrillage[test[0]][test[1]+1]<=7:
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]][test[1]+1]=5
                quadrillage[test[2]][test[3]+1]=5
                quadrillage[test[4]-1][test[5]+1]=5
                quadrillage[test[6]-1][test[7]-1]=5 #-1, pas -2+1
                rotation=1
                acte=1
            if spawn=="barre" and rotation==1 and acte==0 and quadrillage[test[0]-1][test[1]+2]<=7 and quadrillage[test[2]+1][test[3]+1]<=7 and quadrillage[test[6]+2][test[7]-1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]-1][test[1]+2]=3
                quadrillage[test[2]+1][test[3]+1]=3
                quadrillage[test[6]+2][test[7]-1]=3
                rotation=2
                acte=1
            if spawn=="barre" and rotation==2 and test[1]>1 and test[1]<nbcolonne-1 and acte==0 and quadrillage[test[6]-2][test[7]-2]<=7 and quadrillage[test[0]+1][test[1]+1]<=7 and quadrillage[test[4]-1][test[5]-1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]+1]=3
                quadrillage[test[4]-1][test[5]-1]=3
                quadrillage[test[6]-2][test[7]-2]=3
                rotation=1
                acte=1
            if spawn=="T" and rotation==3 and acte==0 and quadrillage[test[4]-1][test[5]-1]<=7:

                quadrillage[test[4]][test[5]]=0
                quadrillage[test[4]-1][test[5]-1]=4
                rotation=4
                acte=1
            if spawn=="T" and rotation==2 and test[1]>0 and  acte==0 and quadrillage[test[0]+1][test[1]-1]<=7:
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[0]+1][test[1]-1]=4
                rotation=3
                acte=1
            if spawn=="T" and rotation==1 and acte==0 and quadrillage[test[2]+1][test[3]+1]<=7:
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[2]+1][test[3]+1]=4
                rotation=2
                acte=1
            if spawn=="T" and rotation==4  and test[1]<nbcolonne-1 and acte==0 and quadrillage[test[6]-1][test[7]+1]<=7:

                quadrillage[test[6]][test[7]]=0
                quadrillage[test[6]-1][test[7]+1]=4
                rotation=1
                acte=1
            print("rotation=",rotation)
        grille()
    def rotationG(event):
        global spawn,rotation
        test=[]
        acte=0
        for i in range (a):
            for j in range (b):
                if quadrillage[i][j]>0 and quadrillage[i][j]<8:
                    test.append(i)
                    test.append(j)
        if mouvbarre==1:
            acte=1
        if len(test)>0:
            if spawn=="L2" and rotation==1 and acte==0 and quadrillage[test[4]+1][test[5]+1]<=7 and quadrillage[test[2]+2][test[3]+2]<=7 and quadrillage[test[0]+1][test[1]-1]<=7:
                hv=1
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[0]+1][test[1]-1]=7
                quadrillage[test[2]+2][test[3]+2]=7
                quadrillage[test[4]+1][test[5]+1]=7
                acte=1
                rotation=4
            if spawn=="L2" and rotation==2 and test[1]>1 and acte==0 and quadrillage[test[2]+1][test[3]-1]<=7 and quadrillage[test[0]+2][test[1]-2]<=7 and quadrillage[test[6]-1][test[7]-1]<=7:
                hv=2
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+2][test[1]-2]=7
                quadrillage[test[2]+1][test[3]-1]=7
                quadrillage[test[6]-1][test[7]-1]=7
                acte=1
                rotation=1
            if spawn=="L2" and rotation==3 and acte==0 and quadrillage[test[2]-1][test[3]-1]<=7 and quadrillage[test[6]-1][test[7]+1]<=7 and quadrillage[test[4]-2][test[5]-2]<=7:
                hv=3
                print(hv)
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[2]-1][test[3]-1]=7
                quadrillage[test[4]-2][test[5]-2]=7
                quadrillage[test[6]-1][test[7]+1]=7
                acte=1
                rotation=2
            if spawn=="L2" and rotation==4 and acte==0  and test[1]<nbcolonne-3 and quadrillage[test[6]-2][test[7]+2]<=7 and quadrillage[test[4]-1][test[5]+1]<=7 and quadrillage[test[0]+1][test[1]+1]<=7:
                hv=4
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]+1]=7
                quadrillage[test[4]-1][test[5]+1]=7
                quadrillage[test[6]-2][test[7]+2]=7
                acte=1
                rotation=3
            if spawn=="L1" and rotation==1 and test[1]<nbcolonne-3 and acte==0 and quadrillage[test[0]+2][test[1]+2]<=7 and quadrillage[test[2]+1][test[3]+1]<=7 and quadrillage[test[6]-1][test[7]+1]<=7:
                hv=5
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+2][test[1]+2]=6
                quadrillage[test[2]+1][test[3]+1]=6
                quadrillage[test[6]-1][test[7]+1]=6
                acte=1
                rotation=4
            if spawn=="L1" and rotation==2  and test[1]>1 and acte==0 and quadrillage[test[4]+1][test[5]+1]<=7 and quadrillage[test[2]+1][test[3]-1]<=7 and quadrillage[test[0]+2][test[1]-2]<=7:
                hv=6
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[0]+2][test[1]-2]=6
                quadrillage[test[2]+1][test[3]-1]=6
                quadrillage[test[4]+1][test[5]+1]=6
                acte=1
                rotation=1
            if spawn=="L1" and rotation==3 and test[1]>0 and acte==0 and quadrillage[test[0]+1][test[1]-1]<=7 and quadrillage[test[6]-2][test[7]-2]<=7 and quadrillage[test[4]-1][test[5]+1]<=7:
                hv=7
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]-1]=6
                quadrillage[test[4]-1][test[5]-1]=6
                quadrillage[test[6]-2][test[7]-2]=6
                acte=1
                rotation=2
            if spawn=="L1" and rotation==4 and test[1]<nbcolonne-2 and acte==0 and quadrillage[test[2]-1][test[3]-1]<=7 and quadrillage[test[6]-2][test[7]+2]<=7 and quadrillage[test[4]-1][test[5]+1]<=7:
                hv=8
                print(hv)
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[2]-1][test[3]-1]=6
                quadrillage[test[4]-1][test[5]+1]=6
                quadrillage[test[6]-2][test[7]+2]=6
                acte=1
                rotation=3
            if spawn=="Z" and rotation==1 and acte==0 and quadrillage[test[2]+2][test[3]]<=7 and quadrillage[test[0]][test[1]+2]<=7:
                hv=9
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[0]][test[1]+2]=1
                quadrillage[test[2]+2][test[3]]=1
                rotation=2
                acte=1
            if spawn=="Z" and rotation==2 and acte==0 and test[1]>1 and quadrillage[test[6]-1][test[7]+1]<=7 and quadrillage[test[2]-1][test[3]-1]<=7 and quadrillage[test[4]][test[5]-1]<=7 and quadrillage[test[0]][test[1]-1]<=7:
                hv=10
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]][test[1]-1]=1
                quadrillage[test[2]-1][test[3]-1]=1
                quadrillage[test[4]][test[5]-1]=1
                quadrillage[test[6]-1][test[7]+1]=1
                rotation=1
                acte=1
            if spawn=="S" and rotation==1 and acte==0 and quadrillage[test[4]-1][test[5]]<=7 and quadrillage[test[2]+1][test[3]-2]<=7 and quadrillage[test[6]+1][test[7]]<=7 and quadrillage[test[0]+1][test[1]]<=7:
                hv=11
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[4]+1][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]]=5
                quadrillage[test[2]+1][test[3]-2]=5
                quadrillage[test[4]-1][test[5]]=5
                quadrillage[test[6]+1][test[7]]=5
                rotation=2
                acte=1
            if spawn=="S" and rotation==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage[test[6]-1][test[7]-1]<=7 and quadrillage[test[4]-1][test[5]+1]<=7 and quadrillage[test[2]][test[3]+1]<=7 and quadrillage[test[0]][test[1]+1]<=7:
                hv=12
                print(hv)
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]][test[1]+1]=5
                quadrillage[test[2]][test[3]+1]=5
                quadrillage[test[4]-1][test[5]+1]=5
                quadrillage[test[6]-1][test[7]-1]=5
                rotation=1
                acte=1
            if spawn=="barre" and rotation==1 and acte==0 and quadrillage[test[0]+2][test[1]+2]<=7 and quadrillage[test[2]+1][test[3]+1]<=7 and quadrillage[test[6]-1][test[7]-1]<=7:
                hv=13
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[2]][test[3]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+2][test[1]+2]=3
                quadrillage[test[2]+1][test[3]+1]=3
                quadrillage[test[6]-1][test[7]-1]=3
                acte=1
                rotation=2
            if spawn=="barre" and rotation==2 and test[1]>1 and test[1]<nbcolonne-1 and acte==0 and quadrillage[test[6]-2][test[7]-2]<=7 and quadrillage[test[4]-1][test[5]-1]<=7 and quadrillage[test[0]+1][test[1]+1]<=7:
                hv=14
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[4]][test[5]]=0
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[0]+1][test[1]+1]=3
                quadrillage[test[4]-1][test[5]-1]=3
                quadrillage[test[6]-2][test[7]-2]=3
                acte=1
                rotation=1
            if spawn=="T" and rotation==1 and acte==0 and quadrillage[test[6]+1][test[7]-1]<=7:
                hv=20
                print(hv)
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[6]+1][test[7]-1]=4


                acte=1
                rotation=4
            if spawn=="T" and rotation==2 and test[1]>0 and acte==0 and quadrillage[test[6]-1][test[7]-1]<=7:
                hv=17
                print(hv)
                quadrillage[test[6]][test[7]]=0
                quadrillage[test[6]-1][test[7]-1]=4
                acte=1
                rotation=1
            if spawn=="T" and rotation==3 and acte==0 and quadrillage[test[0]-1][test[1]+1]<=7:
                hv=18
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[0]-1][test[1]+1]=4
                acte=1
                rotation=2
            if spawn=="T" and rotation==4 and test[1]<nbcolonne-1 and acte==0 and quadrillage[test[0]+1][test[1]+1]<=7:
                hv=19
                print(hv)
                quadrillage[test[0]][test[1]]=0
                quadrillage[test[0]+1][test[1]+1]=4
                acte=1
                rotation=3
            print("rotation=",rotation)
        grille()
    def mouvement():
        global acceleration,quadrillage,j,vitesse,piece,nbpiece,scoreligne,mouvbarre,ligne
        acte=0
        if ligne<6 and spawn=="barre":
            mouvbarre==1
        testdescente=[]
        piece=[]
        if len(testdescente)>0:
            testdescente=[]
        if len(piece)>0:
            piece=[]
        for j in range (b):
            if  ligne<a-3:
                    if quadrillage[ligne+2][j]>0 and quadrillage[ligne+2][j]<8:
                        piece.append(ligne+2)
                        piece.append(j)
                    if quadrillage[ligne+1][j]>0 and quadrillage[ligne+1][j]<8:
                        piece.append(ligne+1)
                        piece.append(j)
                    if quadrillage[ligne][j]>0 and quadrillage[ligne][j]<8:
                        piece.append(ligne)
                        piece.append(j)
                    if quadrillage[ligne-1][j]>0 and quadrillage[ligne-1][j]<8:
                        piece.append(ligne-1)
                        piece.append(j)
                    if quadrillage[ligne-2][j]>0 and quadrillage[ligne-2][j]<8:
                        piece.append(ligne-2)
                        piece.append(j)
                    if quadrillage[ligne-3][j]>0 and quadrillage[ligne-3][j]<8:
                        piece.append(ligne-3)
                        piece.append(j)
                    if quadrillage[ligne-4][j]>0 and quadrillage[ligne-4][j]<8:
                        piece.append(ligne-4)
                        piece.append(j)
                    if quadrillage[ligne-5][j]>0 and quadrillage[ligne-5][j]<8:
                        piece.append(ligne-5)
                        piece.append(j)

        nbpiece=len(piece)
        if acte==0 and nbpiece>0:
            if nbpiece==18:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8 and quadrillage[piece[6]+1][piece[7]]<8 and quadrillage[piece[10]+1][piece[11]]<8 and quadrillage[piece[8]+1][piece[9]]<8 and quadrillage[piece[14]+1][piece[15]]<8 and quadrillage[piece[12]+1][piece[13]]<8 and quadrillage[piece[16]+1][piece[17]]<8:
                    quadrillage[piece[16]][piece[17]]=0
                    quadrillage[piece[14]][piece[15]]=0
                    quadrillage[piece[12]][piece[13]]=0
                    quadrillage[piece[10]][piece[11]]=0
                    quadrillage[piece[8]][piece[9]]=0
                    quadrillage[piece[6]][piece[7]]=0
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[16]+1][piece[17]]=color
                    quadrillage[piece[14]+1][piece[15]]=color
                    quadrillage[piece[12]+1][piece[13]]=color
                    quadrillage[piece[10]+1][piece[11]]=color
                    quadrillage[piece[8]+1][piece[9]]=color
                    quadrillage[piece[6]+1][piece[7]]=color
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[16]][piece[17]]=quadrillage[piece[16]][piece[17]]+10
                    quadrillage[piece[14]][piece[15]]=quadrillage[piece[14]][piece[15]]+10
                    quadrillage[piece[12]][piece[13]]=quadrillage[piece[12]][piece[13]]+10
                    quadrillage[piece[10]][piece[11]]=quadrillage[piece[10]][piece[11]]+10
                    quadrillage[piece[8]][piece[9]]=quadrillage[piece[8]][piece[9]]+10
                    quadrillage[piece[6]][piece[7]]=quadrillage[piece[6]][piece[7]]+10
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==16:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8 and quadrillage[piece[6]+1][piece[7]]<8 and quadrillage[piece[8]+1][piece[9]]<8 and quadrillage[piece[14]+1][piece[15]]<8 and quadrillage[piece[12]+1][piece[13]]<8:
                    quadrillage[piece[14]][piece[15]]=0
                    quadrillage[piece[12]][piece[13]]=0
                    quadrillage[piece[10]][piece[11]]=0
                    quadrillage[piece[8]][piece[9]]=0
                    quadrillage[piece[6]][piece[7]]=0
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[14]+1][piece[15]]=color
                    quadrillage[piece[12]+1][piece[13]]=color
                    quadrillage[piece[10]+1][piece[11]]=color
                    quadrillage[piece[8]+1][piece[9]]=color
                    quadrillage[piece[6]+1][piece[7]]=color
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[14]][piece[15]]=quadrillage[piece[14]][piece[15]]+10
                    quadrillage[piece[12]][piece[13]]=quadrillage[piece[12]][piece[13]]+10
                    quadrillage[piece[10]][piece[11]]=quadrillage[piece[10]][piece[11]]+10
                    quadrillage[piece[8]][piece[9]]=quadrillage[piece[8]][piece[9]]+10
                    quadrillage[piece[6]][piece[7]]=quadrillage[piece[6]][piece[7]]+10
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==14:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8 and quadrillage[piece[6]+1][piece[7]]<8 and quadrillage[piece[8]+1][piece[9]]<8 and quadrillage[piece[12]+1][piece[13]]<8:
                    quadrillage[piece[12]][piece[13]]=0
                    quadrillage[piece[10]][piece[11]]=0
                    quadrillage[piece[8]][piece[9]]=0
                    quadrillage[piece[6]][piece[7]]=0
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[12]+1][piece[13]]=color
                    quadrillage[piece[10]+1][piece[11]]=color
                    quadrillage[piece[8]+1][piece[9]]=color
                    quadrillage[piece[6]+1][piece[7]]=color
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[12]][piece[13]]=quadrillage[piece[12]][piece[13]]+10
                    quadrillage[piece[10]][piece[11]]=quadrillage[piece[10]][piece[11]]+10
                    quadrillage[piece[8]][piece[9]]=quadrillage[piece[8]][piece[9]]+10
                    quadrillage[piece[6]][piece[7]]=quadrillage[piece[6]][piece[7]]+10
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==12:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8 and quadrillage[piece[6]+1][piece[7]]<8 and quadrillage[piece[8]+1][piece[9]]<8:
                    quadrillage[piece[10]][piece[11]]=0
                    quadrillage[piece[8]][piece[9]]=0
                    quadrillage[piece[6]][piece[7]]=0
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[10]+1][piece[11]]=color
                    quadrillage[piece[8]+1][piece[9]]=color
                    quadrillage[piece[6]+1][piece[7]]=color
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[10]][piece[11]]=quadrillage[piece[10]][piece[11]]+10
                    quadrillage[piece[8]][piece[9]]=quadrillage[piece[8]][piece[9]]+10
                    quadrillage[piece[6]][piece[7]]=quadrillage[piece[6]][piece[7]]+10
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==10:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8 and quadrillage[piece[6]+1][piece[7]]<8 and quadrillage[piece[8]+1][piece[9]]<8:
                    quadrillage[piece[8]][piece[9]]=0
                    quadrillage[piece[6]][piece[7]]=0
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[8]+1][piece[9]]=color
                    quadrillage[piece[6]+1][piece[7]]=color
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color

                else:
                    quadrillage[piece[8]][piece[9]]=quadrillage[piece[8]][piece[9]]+10
                    quadrillage[piece[6]][piece[7]]=quadrillage[piece[6]][piece[7]]+10
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==8:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8 and quadrillage[piece[6]+1][piece[7]]<8:
                    quadrillage[piece[6]][piece[7]]=0
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[6]+1][piece[7]]=color
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[6]][piece[7]]=quadrillage[piece[6]][piece[7]]+10
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==2:
                if quadrillage[piece[0]+1][piece[1]]<8:
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==4:
                if quadrillage[piece[0]][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8:
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
            if nbpiece==6:
                if quadrillage[piece[0]+1][piece[1]]<8 and quadrillage[piece[2]+1][piece[3]]<8 and quadrillage[piece[4]+1][piece[5]]<8:
                    quadrillage[piece[4]][piece[5]]=0
                    quadrillage[piece[2]][piece[3]]=0
                    quadrillage[piece[0]][piece[1]]=0
                    quadrillage[piece[4]+1][piece[5]]=color
                    quadrillage[piece[2]+1][piece[3]]=color
                    quadrillage[piece[0]+1][piece[1]]=color
                else:
                    quadrillage[piece[4]][piece[5]]=quadrillage[piece[4]][piece[5]]+10
                    quadrillage[piece[2]][piece[3]]=quadrillage[piece[2]][piece[3]]+10
                    quadrillage[piece[0]][piece[1]]=quadrillage[piece[0]][piece[1]]+10
        ligne=ligne+1
        if ligne==a-3:
            ligne=4
            objet()
            objetsuite()
            grilleaffichage1()




        scoreligne=len(ligne_supprimée)
        Lsj1.config(text=("Score:",scoreligne))
        grille()
        arg1.after(5*((int(vitesse*acceleration)//2)),mouvement)

    def grille():
        global quadrillage,ligne_supprimée,verif,test3,test4
        destrouy=0
        Cj1.delete(ALL)
        for j in range(b+1):
            x=j*20
            y=0
            Cj1.create_line(x,y,x,y+560,fill="light grey",width=0.5)
        for i in range(28):
            x=0
            y=i*20
            Cj1.create_line(x,y,x+b*20,y,fill="light grey",width=0.5)
        for j in range(b):
            x=j*20
            y=580
            Cj1.create_line(x,y,nbcolonne*10,y+140,fill="light grey",width=0.5)
            Cj1.create_line((b)*20,y,nbcolonne*10,y+140,fill="light grey",width=0.5)
        for i in range(1):
            for j in range (b):
                if quadrillage[5+i][j]>=8:
                    print("perdu j1")
                    destrouy=1
        if destrouy==1:
            arg1.destroy()
        else:
            for i in range (a):
                for j in range (b):
                    if quadrillage[i][j]>0:
                        x=j*20
                        y=i*20
                        test3=quadrillage[i][j]
                        if test3!=0:
                            test4 = couleur[test3]
                            Cj1.create_rectangle(x,y,x+20,y+20,fill=test4)
    def verification():
        global casesuppr,action
        for i in range(a):
            for j in range(b):
                if quadrillage[i][j]==9:
                    quadrillage[i][j]=0
        for i in range (a):
                verif = 0
                for j in range (b) :
                    if quadrillage [i][j]>=10 :
                        verif= verif + 1
                    if verif == nbcolonne :
                        action=1
                        verif=0
                        ligne_supprimée.append (i)

                        casesuppr=i
                        quadrillage[casesuppr]=[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
                        arg1.after(500,descente)

        arg1.after(10,verification)
    def descente():
        global quadrillage
        quadrillage[casesuppr]=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        GrilleDescente()
    def GrilleDescente():
        global quadrillage,test3,test4,ligne,action,acceleration
        action=0
        if vitesse+acceleration>=0.4:
            acceleration=acceleration-0.04
    def analyse():
        global quadrillage,action
        if action==0:
            for i in range (29):
                if quadrillage[i]==quadrillage[30]:
                    for j in range(b):
                        if quadrillage[i-1][j]>10:
                            quadrillage[i][j]=quadrillage[i-1][j]
                            quadrillage[i-1][j]=0
        for i in range(10):
            if scoreligne==5*i:
                acceleration=10-i+1
        arg1.after(100,analyse)
    def droite(event):
        global quadrillage,color
        test=[]
        acte=0
        for i in range (a):
            for j in range (b):
                if quadrillage[i][j]>0 and quadrillage[i][j]<8:
                    test.append(i)
                    test.append(j)
        pop=len(test)
        for limiteD in range (pop//2):
            if test[limiteD*2+1]==nbcolonne-1:
                acte=1

        for limiteDbloc in range(pop//2):
            if acte!=1:
                if quadrillage[test[limiteDbloc*2]][test[limiteDbloc*2+1]+1]>=8:
                    acte=1
        if acte==0:
            if pop>18 and quadrillage[test[18]][test[19]+1]<8:
                quadrillage[test[18]][test[19]+1]=color
                quadrillage[test[18]][test[19]]=0
            if pop>16 and quadrillage[test[16]][test[17]+1]<8:
                quadrillage[test[16]][test[17]+1]=color
                quadrillage[test[16]][test[17]]=0
            if pop>14 and quadrillage[test[14]][test[15]+1]<8:
                quadrillage[test[14]][test[15]+1]=color
                quadrillage[test[14]][test[15]]=0
            if pop>12 and quadrillage[test[12]][test[13]+1]<8:
                quadrillage[test[12]][test[13]+1]=color
                quadrillage[test[12]][test[13]]=0
            if pop>10 and quadrillage[test[10]][test[11]+1]<8:
                quadrillage[test[10]][test[11]+1]=color
                quadrillage[test[10]][test[11]]=0
            if pop>8 and quadrillage[test[8]][test[9]+1]<8:
                quadrillage[test[8]][test[9]+1]=color
                quadrillage[test[8]][test[9]]=0
            if pop>6 and quadrillage[test[6]][test[7]+1]<8:
                quadrillage[test[6]][test[7]+1]=color
                quadrillage[test[6]][test[7]]=0
            if pop>4 and quadrillage[test[4]][test[5]+1]<8:
                quadrillage[test[4]][test[5]+1]=color
                quadrillage[test[4]][test[5]]=0
            if pop>2 and quadrillage[test[2]][test[3]+1]<8:
                quadrillage[test[2]][test[3]+1]=color
                quadrillage[test[2]][test[3]]=0
            if pop>0 and quadrillage[test[0]][test[1]+1]<8:
                quadrillage[test[0]][test[1]+1]=color
                quadrillage[test[0]][test[1]]=0
        grille()
    def gauche(event):
        global quadrillage,color
        test=[]
        acte=0
        for i in range (a):
            for j in range (b):
                if quadrillage[i][j]>0 and quadrillage[i][j]<8:
                    test.append(i)
                    test.append(j)
                    s=len(test)
        pop=len(test)
        for limiteG in range (pop//2):
            if test[limiteG*2+1]==0:
                acte=1
        for limiteGbloc in range(pop//2):
            if quadrillage[test[limiteGbloc*2]][test[limiteGbloc*2+1]-1]>=8:
                acte=1
        if acte==0:
            if pop>0  and quadrillage[test[0]][test[1]-1]<8:
                quadrillage[test[0]][test[1]-1]=color
                quadrillage[test[0]][test[1]]=0
            if pop>2 and quadrillage[test[2]][test[3]-1]<8:
                quadrillage[test[2]][test[3]-1]=color
                quadrillage[test[2]][test[3]]=0
            if pop>4 and quadrillage[test[4]][test[5]-1]<8:
                quadrillage[test[4]][test[5]-1]=color
                quadrillage[test[4]][test[5]]=0
            if pop>6 and quadrillage[test[6]][test[7]-1]<8:
                quadrillage[test[6]][test[7]-1]=color
                quadrillage[test[6]][test[7]]=0
            if pop>8 and quadrillage[test[8]][test[9]-1]<8:
                quadrillage[test[8]][test[9]-1]=color
                quadrillage[test[8]][test[9]]=0
            if pop>10 and quadrillage[test[10]][test[11]-1]<8:
                quadrillage[test[10]][test[11]-1]=color
                quadrillage[test[10]][test[11]]=0
            if pop>12 and quadrillage[test[12]][test[13]-1]<8:
                quadrillage[test[12]][test[13]-1]=color
                quadrillage[test[12]][test[13]]=0
            if pop>14 and quadrillage[test[14]][test[15]-1]<8:
                quadrillage[test[14]][test[15]-1]=color
                quadrillage[test[14]][test[15]]=0
            if pop>16 and quadrillage[test[16]][test[17]-1]<8:
                quadrillage[test[16]][test[17]-1]=color
                quadrillage[test[16]][test[17]]=0
            if pop>18 and quadrillage[test[18]][test[19]-1]<8:
                quadrillage[test[18]][test[19]-1]=color
                quadrillage[test[18]][test[19]]=0


        grille()
    def music4():
        pygame.mixer.music.load("Tetris1.mp3")
        pygame.mixer.music.play()
        arg1.after(104000,music1)
    def music1():
        pygame.mixer.music.load("Tetris2.mp3")
        pygame.mixer.music.play()
        arg1.after(210000,music2)
    def music2():
        pygame.mixer.music.load("Tetris3.mp3")
        pygame.mixer.music.play()
        arg1.after(170000,music3)
    def music3():
        pygame.mixer.music.load("Tetris4.mp3")
        pygame.mixer.music.play()
        arg1.after(218000,music4)
    def grilleaffichage1():
        global quadrillageaffichagej1,test3,test4
        for i in range (6):
            for j in range (5):
                C2j1.create_rectangle(i*20,j*20,i*20+20,j*20+20,fill="white")
        for i in range (5):
            for j in range (5):
                if quadrillageaffichagej1[i][j]>0:
                    x=j*20
                    y=i*20
                    test3=quadrillageaffichagej1[i][j]
                    if test3!=0:
                        test4 = couleur[test3]
                        C2j1.create_rectangle(x,y,x+20,y+20,fill=test4)
    def Cvitesseon():
        global vitesse
        vitesse=2
    def Cvitesseoff():
        global vitesse
        vitesse=10
    def scanon2(event):
        global t2
        t2 = event.keysym
        if t2==touche1sauv:
            Cvitesseon()
    def scanoff2(event):
        global t2
        t2 = event.keysym
        if t2==touche1sauv:
            Cvitesseoff()
    def bistoukette(event):
        global acceleration,acta
        print(quadrillage[23])
        print(quadrillage[24])
        print(quadrillage[25])
        print(quadrillage[26])
        print(quadrillage[27])
    def spawnapres():
        global spawn, pieceapres
        if pieceapres == "" :
            spawn = choice(list_objet)
        else :
            spawn = pieceapres
    arg1.geometry("500x600")
    Cj1=Canvas(arg1,width=300,height=700,bg="white")
    C2j1=Canvas(arg1,width=200,height=620,bg="white")
    C2j1.place(x=300,y=0)
    Cj1.place(x=0,y=-100)
    Lsj1=Label(arg1,text=("Score:",scoreligne),bg="white")
    Lsj1.place(x=350,y=200)
    quadrillage=[]
    for z in range (35):
        quadrillage.append([0]*nbcolonne)
    quadrillage[28]=[]
    for y in range(nbcolonne):
        quadrillage[28].append(8)
    a=len(quadrillage)
    b=len(quadrillage[1])
    print(a,b)
    objetsuite()
    mouvement()
    music4()
    touche1sauv=touche1
    touche2="<"+touche2+">"
    touche3="<"+touche3+">"
    touche4="<"+touche4+">"
    grille()
    analyse()
    verification()
    grilleaffichage1()
    arg1.title("Tetris Versus")
    arg1.bind_all("<KeyPress>",scanon2)
    arg1.bind_all("<KeyRelease>",scanoff2)
    arg1.bind("<"+"k"+">",rotationG)
    arg1.bind(touche3,gauche)
    arg1.bind(touche2,droite)
    arg1.bind(touche4,changepiece)
    arg1.bind("b",bistoukette)

    arg1.mainloop()

pygame.mixer.music.pause()
