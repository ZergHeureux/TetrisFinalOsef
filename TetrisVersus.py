from random import*
from tkinter import*
import pygame
pygame.init()
aide_objet=["cube","barre","L1","L2","Z","S","T"]
list_objet=["cube","barre","L1","L2","Z","S","T"]
couleur=["black","red","yellow","sky blue","purple","light green","blue","orange","grey","white","test","red","yellow","sky blue","purple","light green","blue","orange","grey","grey"]
acceleration=12
acceleration2=12
y=0
j=0
A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
action=0
action2=0
cadeau=0
verif = 0
ligne=4
scoreligne=0
scoreligne2=0
touche1sauv=""
ligne_supprimée=[]
rotation=0
vitesse=10
ligne2=4
Malus1=0
Malus2=0
pluie1=0
pluie2=0
touche10sauv=""
ligne_supprimée2=[]
rotation2=0
vitesse2=10
mouvbarre=0
pieceapres=""
spawnafter2=""
mouvbarre2=0
Chargement1=0
Chargement2=0
powerup1=0
powerup2=0
spawn="cube"
spawn2="cube"
powerpret1=0
powerpret2=0
quadrillageaffichagej1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
quadrillageaffichagej2=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def TetrisVersus(arg1,touche1,touche2,touche3,touche4,touche5,touche6,touche10,touche11,touche12,touche13,touche14,touche15,piecedujoueuriR1,piecedujoueurjR1,piecedujoueuriR2,piecedujoueurjR2,piecedujoueuriR3,piecedujoueurjR3,piecedujoueuriR4,piecedujoueurjR4,couleurjoueur,nbcolonne,nbcolonne2):
    global quadrillage,quadrillage2,C2j1,C2j2,Cj1,Cj2
    print(piecedujoueuriR1)
    def PowerUpPret1():
        global Chargement1,powerup1,powerpret1
        if Chargement1>=1:
            powerup1=1
        if powerup1==1:
            if powerpret1==0:
                PowerUp1()
            powerpret1=1
        arg1.after(1,PowerUpPret1)
    def PowerUpPret2():
        global Chargement2,powerup2,powerpret2
        if Chargement2>=1:
            powerup2=1
        if powerup2==1:
            if powerpret2==0:
                PowerUp2()
            powerpret2=1
        arg1.after(1,PowerUpPret2)
    def PowerUp1():
        global C2j1,itmPU1,Fantom,Baguette,Barre,Pluie,Piece1,Brique,PieceJ1,Acide,boost,cage,seisme
        xx=choice([1,2,3,4,5,6,7,8,9,10,11])
        if xx==1:
            Fantom=PhotoImage(file="MalusFantom.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Fantom)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveF1)
        if xx==2:
            Baguette=PhotoImage(file="BonusBaguette.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Baguette)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveBag1)
        if xx==3:
            Barre=PhotoImage(file="BonusBarre.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Barre)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveBar1)
        if xx==4:
            Brique=PhotoImage(file="MalusBrique.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Brique)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveBri1)
        if xx==5:
            Piece1=PhotoImage(file="MalusPiece1.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Piece1)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactivePie1)
        if xx==6:
            Pluie=PhotoImage(file="BonusPluie.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Pluie)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactivePlu1)
        if xx==7:
            PieceJ1=PhotoImage(file="PieceJ1.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=PieceJ1)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactivePj1)
        if xx==8:
            Acide=PhotoImage(file="MalusAcide.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=Acide)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveA1)
        if xx==9:
            boost=PhotoImage(file="MalusVit.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=boost)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveB1)
        if xx==10:
            cage=PhotoImage(file="MalusCage.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=cage)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveC1)
        if xx==11:
            seisme=PhotoImage(file="MalusSeisme.png")
            itmPU1=C2j1.create_image(0,100,anchor=NW,image=seisme)
            arg1.unbind(touche5)
            arg1.bind(touche5,PUactiveS1)
    def PowerUp2():
        global C2j2,itmPU2,powerup2,Fantom,Baguette,Barre,Pluie,Piece1,Brique,PieceJ1,Acide,MCarre,boost,cage,seisme
        xx=choice([1,2,3,4,5,6,7,8,9,10,11])
        if xx==1:
            Fantom=PhotoImage(file="MalusFantom.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Fantom)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveF2)
        if xx==2:
            Baguette=PhotoImage(file="BonusBaguette.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Baguette)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveBag2)
        if xx==3:
            Barre=PhotoImage(file="BonusBarre.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Barre)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveBar2)
        if xx==4:
            Brique=PhotoImage(file="MalusBrique.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Brique)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveBri2)
        if xx==5:
            Piece1=PhotoImage(file="MalusPiece1.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Piece1)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactivePie2)
        if xx==6:
            Pluie=PhotoImage(file="BonusPluie.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Pluie)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactivePlu2)
        if xx==7:
            PieceJ1=PhotoImage(file="PieceJ1.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=PieceJ1)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactivePj2)
        if xx==8:
            Acide=PhotoImage(file="MalusAcide.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=Acide)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveA2)
        if xx==9:
            boost=PhotoImage(file="MalusVit.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=boost)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveB2)
        if xx==10:
            cage=PhotoImage(file="MalusCage.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=cage)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveC2)
        if xx==11:
            seisme=PhotoImage(file="MalusSeisme.png")
            itmPU2=C2j2.create_image(0,100,anchor=NW,image=seisme)
            arg1.unbind(touche14)
            arg1.bind(touche14,PUactiveS2)
    def PUactiveS2(event):
        global Chargement2,powerup2,powerpret2
        Chargement2,powerup2,powerpret2=0,0,0
        C2j2.delete(itmPU2)
        arg1.unbind(touche14)
        s=randint(2,13)
        for i in range(28):
            if quadrillage[i][s]>10:
                quadrillage[i][s]=0
            if quadrillage[i][s+1]>10:
                quadrillage[i][s+1]=0
    def PUactiveS1(event):
        global Chargement1,powerup1,powerpret1
        Chargement1,powerup1,powerpret1=0,0,0
        C2j1.delete(itmPU1)
        arg1.unbind(touche5)
        s=randint(1,14)
        for i in range(28):
            if quadrillage2[i][s]>10:
                quadrillage2[i][s]=0
            if quadrillage2[i][s+1]>10:
                quadrillage2[i][s+1]=0

    def PUactiveB2(event):
        global Chargement2,powerup2,powerpret2,acceleration,vitesse
        Chargement2,powerup2,powerpret2=0,0,0
        acceleration=acceleration/2
        vitesse=vitesse/2
        arg1.unbind(touche14)
        C2j2.delete(itmPU2)
        arg1.after(8000,B2off)
    def B2off():
        global vitesse,acceleration
        vitesse=vitesse*2
        acceleration=acceleration*2
    def PUactiveB1(event):
        global Chargement1,powerup1,powerpret1,acceleration2,vitesse2
        Chargement1,powerup1,powerpret1=0,0,0
        acceleration2=acceleration2/2
        vitesse2=vitesse2/2
        arg1.unbind(touche5)
        C2j1.delete(itmPU1)
        arg1.after(8000,B1off)
    def B1off():
        global vitesse2,acceleration2
        vitesse2=vitesse2*2
        acceleration2=acceleration2*2
    def PUactiveF1(event):
        global quadrillage2,Chargement1,powerup1,powerpret1
        Chargement1,powerup1,powerpret1=0,0,0
        for i in range(4):
            xi1=randint(19,27)
            xj1=randint(1,14)
            quadrillage2[xi1][xj1]=0
        C2j1.delete(itmPU1)
        arg1.unbind(touche5)
    def PUactiveF2(event):
        global quadrillage,Chargement2,powerup2,powerpret2
        Chargement2,powerup2,powerpret2=0,0,0
        for i in range(4):
            xi2=randint(19,27)
            xj2=randint(1,14)
            quadrillage[xi2][xj2]=0
        C2j2.delete(itmPU2)
        arg1.unbind(touche14)
    def PUactiveBag1(event):
        global quadrillage,C2j1,Chargement1,powerup1,powerpret1
        hi1=randint(26,27)
        Chargement1,powerup1,powerpret1=0,0,0
        quadrillage[hi1]=[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]
        C2j1.delete(itmPU1)
        arg1.unbind(touche5)
    def PUactiveBag2(event):
        global quadrillage2,Chargement2,powerup2,powerpret2
        hi2=randint(26,27)
        Chargement2,powerup2,powerpret2=0,0,0
        quadrillage2[hi2]=[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]
        C2j2.delete(itmPU2)
        arg1.unbind(touche14)
    def PUactiveBri1(event):
        global Malus2,Chargement1,powerup1,powerpret1
        Malus2=1
        objetsuite2()
        Chargement1,powerup1,powerpret1=0,0,0
        C2j1.delete(itmPU1)
        arg1.unbind(touche5)
    def PUactiveBri2(event):
        global Malus1,Chargement2,powerup2,powerpret2
        C2j2.delete(itmPU2)
        Chargement2,powerup2,powerpret2=0,0,0
        arg1.unbind(touche14)
        Malus1=1
        objetsuite()
    def PUactivePie1(event):
        global Malus2,Chargement1,powerup1,powerpret1
        arg1.unbind(touche5)
        Malus2=2
        objetsuite2()
        Chargement1,powerup1,powerpret1=0,0,0
        C2j1.delete(itmPU1)
    def PUactivePie2(event):
        global Malus1,Chargement2,powerup2,powerpret2
        Malus1=2
        objetsuite()
        C2j2.delete(itmPU2)
        Chargement2,powerup2,powerpret2=0,0,0
        arg1.unbind(touche14)
    def PUactiveBar1(event):
        global Malus1,Chargement1,powerup1,powerpret1
        arg1.unbind(touche5)
        Chargement1,powerup1,powerpret1=0,0,0
        Malus1=3
        C2j1.delete(itmPU1)
    def PUactiveBar2(event):
        global Malus2,Chargement2,powerup2,powerpret2
        arg1.unbind(touche14)
        Chargement2,powerup2,powerpret2=0,0,0
        Malus2=3
        objetsuite2()
        C2j2.delete(itmPU2)
    def PUactivePlu1(event):
        global Malus1,pluie1,Chargement1,powerup1,powerpret1
        pluie1=10
        objetsuite()
        Chargement1,powerup1,powerpret1=0,0,0
        arg1.unbind(touche5)
        C2j1.delete(itmPU1)
        Malus1=4
    def PUactivePlu2(event):
        global Malus2,pluie2,Chargement2,powerup2,powerpret2
        Chargement2,powerup2,powerpret2=0,0,0
        pluie2=10
        arg1.unbind(touche14)
        Malus2=4
        objetsuite2()
        C2j2.delete(itmPU2)
    def PUactivePj2(event):
        global Malus1,Chargement2,powerup2,powerpret2
        Chargement2,powerup2,powerpret2=0,0,0
        Malus1=5
        objetsuite()
        arg1.unbind(touche14)
        C2j2.delete(itmPU2)
    def PUactivePj1(event):
        global Malus2,Chargement1,powerup1,powerpret1
        Chargement1,powerup1,powerpret1=0,0,0
        Malus2=5
        objetsuite2()
        arg1.unbind(touche5)
        C2j1.delete(itmPU1)
    def PUactiveC1(event):
        global Chargement1,powerup1,powerpret1
        arg1.unbind(touche5)
        arg1.unbind(touche11)
        arg1.unbind(touche12)
        C2j1.delete(itmPU1)
        Chargement1,powerup1,powerpret1=0,0,0
        arg1.after(5000,PUdesactiveC1)
    def PUdesactiveC1():
        arg1.bind(touche12,gauche2)
        arg1.bind(touche11,droite2)
    def PUactiveC2(event):
        global Chargement2,powerup2,powerpret2
        arg1.unbind(touche14)
        C2j2.delete(itmPU2)
        arg1.unbind(touche2)
        arg1.unbind(touche3)
        Chargement2,powerup2,powerpret2=0,0,0
        arg1.after(5000,PUdesactiveC2)
    def PUdesactiveC2():
        arg1.bind(touche2,gauche)
        arg1.bind(touche3,droite)
    def PUactiveA1(event):
        global Chargement1,powerup1,powerpret1
        arg1.unbind(touche5)
        Acidep2()
        Chargement1,powerup1,powerpret1=0,0,0
        C2j1.delete(itmPU1)
    def PUactiveA2(event):
        global Chargement2,powerup2,powerpret2
        arg1.unbind(touche14)
        Acidep1()
        Chargement2,powerup2,powerpret2=0,0,0
        C2j2.delete(itmPU2)
    def Acidep2():
        global A
        acte=0
        for j in range(9):
            acte=0
            acide=choice(A)
            A.remove(acide)
            for i in range(28):
                if quadrillage2[i][acide]>11 and acte==0:
                    acte=1
                    quadrillage2[i][acide]=0
        A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    def Acidep1():
        global A
        acte=0
        for j in range(9):
            acte=0
            acide=choice(A)
            A.remove(acide)
            for i in range(28):
                if quadrillage[i][acide]>8 and acte==0:
                    acte=1
                    quadrillage[i][acide]=0
        A=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    def objet():
        global quadrillage,spawn,rotation,color,Malus1,pluie1
        spawnapres()
        if pluie1>0 and Malus1!=4:
            pluie1=0
        if Malus1==1:
            spawn="brique"
            Malus1=0
        if Malus1==2:
            spawn="piece1"
            Malus1=0
        if Malus1==3:
            spawn="barre"
            Malus1=0
        if Malus1==4:
            spawn="bloc"
            pluie1=pluie1-1
            if pluie1==0:
                Malus1=0
        if Malus1==5:
            spawn="PieceJoueur"
            Malus1=0
        if spawn=="brique":
            quadrillage[1][5]=7
            quadrillage[1][6]=7
            quadrillage[1][7]=7
            quadrillage[2][5]=7
            quadrillage[2][7]=7
            quadrillage[3][5]=7
            quadrillage[3][6]=7
            quadrillage[3][7]=7
            color=7
        if spawn=="piece1":
            quadrillage[1][4]=6
            quadrillage[2][4]=6
            quadrillage[2][5]=6
            quadrillage[2][6]=6
            quadrillage[3][3]=6
            quadrillage[3][4]=6
            quadrillage[3][6]=6
            quadrillage[4][5]=6
            quadrillage[4][6]=6
            color=6
        if spawn=="bloc":
            quadrillage[1][4]=3
            color=3
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
        if spawn=="PieceJoueur":
            for i in range(len(piecedujoueuriR1)):
                quadrillage[piecedujoueuriR1[i]][piecedujoueurjR1[i]]=couleurjoueur
            color=couleurjoueur
            rotation=1
        print(spawn)
        print("spawn ok")
        grille()
    def objet2():
        global quadrillage2,list_objet,spawn2,rotation2,color2,Malus2,pluie2
        spawnapres2()
        if Malus2==1:
            spawn2="brique"
            Malus2=0
        if Malus2==2:
            spawn2="piece1"
            Malus2=0
        if Malus2==3:
            spawn2="barre"
            Malus2=0
        if Malus2==4:
            spawn2="bloc"
            pluie2=pluie2-1
            if pluie2==0:
                Malus2=0
        if Malus2==5:
            spawn2="PieceJoueur"
            Malus2=0
        if spawn2=="brique":
            quadrillage2[1][5]=7
            quadrillage2[1][6]=7
            quadrillage2[1][7]=7
            quadrillage2[2][5]=7
            quadrillage2[2][7]=7
            quadrillage2[3][5]=7
            quadrillage2[3][6]=7
            quadrillage2[3][7]=7
            color2=7
        if spawn2=="piece1":
            quadrillage2[1][4]=6
            quadrillage2[2][4]=6
            quadrillage2[2][5]=6
            quadrillage2[2][6]=6
            quadrillage2[3][3]=6
            quadrillage2[3][4]=6
            quadrillage2[3][6]=6
            quadrillage2[4][5]=6
            quadrillage2[4][6]=6
            color2=6
        if spawn2=="bloc":
            quadrillage2[1][4]=3
            color2=3
        if spawn2=="Z":
            quadrillage2[1][2+4]=1
            quadrillage2[2][2+4]=1
            quadrillage2[1][1+4]=1
            quadrillage2[2][3+4]=1
            color2 = 1
            rotation2=1
        if spawn2=="cube":
            quadrillage2[1][2+4]=2
            quadrillage2[1][3+4]=2
            quadrillage2[2][2+4]=2
            quadrillage2[2][3+4]=2
            color2 = 2
            rotation2=1
        if spawn2=="barre":
            quadrillage2[1][2+4]=3
            quadrillage2[1][3+4]=3
            quadrillage2[1][4+4]=3
            quadrillage2[1][5+4]=3
            color2 = 3
            rotation2=1
        if spawn2=="T":
            quadrillage2[1][3+4]=4
            quadrillage2[2][3+4]=4
            quadrillage2[2][2+4]=4
            quadrillage2[2][4+4]=4
            color2 = 4
            rotation2=1


        if spawn2=="S":
            quadrillage2[2][2+4]=5
            quadrillage2[2][3+4]=5
            quadrillage2[1][3+4]=5
            quadrillage2[1][4+4]=5
            color2 = 5
            rotation2=1

        if spawn2=="L1":
            quadrillage2[0][1+4]=6
            quadrillage2[0][2+4]=6
            quadrillage2[0][3+4]=6
            quadrillage2[1][3+4]=6
            color2 = 6
            rotation2=1

        if spawn2=="L2":
            quadrillage2[2][1+4]=7
            quadrillage2[2][2+4]=7
            quadrillage2[2][3+4]=7
            quadrillage2[1][3+4]=7
            color2 = 7
            rotation2=1
        if spawn2=="PieceJoueur":
            for i in range(len(piecedujoueuriR1)):
                quadrillage2[piecedujoueuriR1[i]][piecedujoueurjR1[i]]=couleurjoueur
            color2=couleurjoueur
            rotation2=1

##        print(spawn2)
        grille2()
    def objetsuite():
        global quadrillageaffichagej1,list_objet,pieceapres,rotation,color,pluie1,Malus1
        quadrillageaffichagej1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        pieceapres=choice(list_objet)
        if Malus1==1:
            pieceapres="brique"
        if Malus1==2:
            pieceapres="piece1"
        if Malus1==3:
            pieceapres="barre"
        if Malus1==4:
            pieceapres="bloc"
        if Malus1==5:
            pieceapres="PieceJoueur"
        if pieceapres=="brique":
            quadrillageaffichagej1[0][1]=7
            quadrillageaffichagej1[0][2]=7
            quadrillageaffichagej1[0][3]=7
            quadrillageaffichagej1[1][1]=7
            quadrillageaffichagej1[1][3]=7
            quadrillageaffichagej1[2][1]=7
            quadrillageaffichagej1[2][2]=7
            quadrillageaffichagej1[2][3]=7
        if pieceapres=="piece1":
            quadrillageaffichagej1[0][1]=6
            quadrillageaffichagej1[1][1]=6
            quadrillageaffichagej1[1][2]=6
            quadrillageaffichagej1[1][3]=6
            quadrillageaffichagej1[2][0]=6
            quadrillageaffichagej1[2][1]=6
            quadrillageaffichagej1[2][3]=6
            quadrillageaffichagej1[3][2]=6
            quadrillageaffichagej1[3][3]=6
        if pieceapres=="bloc":
            quadrillageaffichagej1[1][2]=3
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
        if pieceapres=="PieceJoueur":
            for i in range(len(piecedujoueuriR1)):
                quadrillageaffichagej1[piecedujoueuriR1[i]][piecedujoueurjR1[i]]=couleurjoueur


        print(pieceapres)
        print("pieceapres ok")
        grilleaffichage1()
    def objetsuite2():
        global quadrillageaffichagej2,list_objet,spawnafter2,rotation2,color2,pluie2,Malus2
        quadrillageaffichagej2=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        spawnafter2=choice(list_objet)
        if Malus2==1:
            spawnafter2="brique"
        if Malus2==2:
            spawnafter2="piece1"
        if Malus2==3:
            spawnafter2="barre"
        if Malus2==4:
            spawnafter2="bloc"
        if Malus2==5:
            spawnafter2="PieceJoueur"
        if spawnafter2=="brique":
            quadrillageaffichagej2[0][1]=7
            quadrillageaffichagej2[0][2]=7
            quadrillageaffichagej2[0][3]=7
            quadrillageaffichagej2[1][1]=7
            quadrillageaffichagej2[1][3]=7
            quadrillageaffichagej2[2][1]=7
            quadrillageaffichagej2[2][2]=7
            quadrillageaffichagej2[2][3]=7
        if spawnafter2=="piece1":
            quadrillageaffichagej2[0][1]=6
            quadrillageaffichagej2[1][1]=6
            quadrillageaffichagej2[1][2]=6
            quadrillageaffichagej2[1][3]=6
            quadrillageaffichagej2[2][0]=6
            quadrillageaffichagej2[2][1]=6
            quadrillageaffichagej2[2][3]=6
            quadrillageaffichagej2[3][2]=6
            quadrillageaffichagej2[3][3]=6
        if spawnafter2=="bloc":
            quadrillageaffichagej2[1][2]=3
        if spawnafter2=="Z":
            quadrillageaffichagej2[1][2]=1
            quadrillageaffichagej2[2][2]=1
            quadrillageaffichagej2[1][1]=1
            quadrillageaffichagej2[2][3]=1
        if spawnafter2=="cube":
            quadrillageaffichagej2[1][2]=2
            quadrillageaffichagej2[1][3]=2
            quadrillageaffichagej2[2][2]=2
            quadrillageaffichagej2[2][3]=2
        if spawnafter2=="barre":
            quadrillageaffichagej2[1][1]=3
            quadrillageaffichagej2[1][2]=3
            quadrillageaffichagej2[1][3]=3
            quadrillageaffichagej2[1][4]=3
        if spawnafter2=="T":
            quadrillageaffichagej2[1][2]=4
            quadrillageaffichagej2[2][2]=4
            quadrillageaffichagej2[2][1]=4
            quadrillageaffichagej2[2][3]=4
        if spawnafter2=="S":
            quadrillageaffichagej2[2][2]=5
            quadrillageaffichagej2[2][3]=5
            quadrillageaffichagej2[1][3]=5
            quadrillageaffichagej2[1][4]=5
        if spawnafter2=="L1":
            quadrillageaffichagej2[1][1]=6
            quadrillageaffichagej2[1][2]=6
            quadrillageaffichagej2[1][3]=6
            quadrillageaffichagej2[2][3]=6
        if spawnafter2=="L2":
            quadrillageaffichagej2[2][1]=7
            quadrillageaffichagej2[2][2]=7
            quadrillageaffichagej2[2][3]=7
            quadrillageaffichagej2[1][3]=7
        if spawnafter2=="PieceJoueur":
            for i in range(len(piecedujoueuriR1)):
                quadrillageaffichagej2[piecedujoueuriR1[i]][piecedujoueurjR1[i]]=couleurjoueur
##        print(spawnafter2)
        grilleaffichage2()
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
    def changepiece2(event):
        global spawn2,rotation2
        test=[]
        acte=0
        for i in range (a):
            for j in range (b):
                if quadrillage2[i][j]>0 and quadrillage2[i][j]<8:
                    test.append(i)
                    test.append(j)
        if mouvbarre==1:
            acte=1
        if len(test)>0:
            if spawn2=="L2" and rotation2==1 and test[1]<nbcolonne-1 and acte==0 and quadrillage2[test[4]-1][test[5]+1]<=7 and quadrillage2[test[2]-2][test[3]+2]<=7 and quadrillage2[test[0]+1][test[1]+1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]+1]=7
                quadrillage2[test[2]-2][test[3]+2]=7
                quadrillage2[test[4]-1][test[5]+1]=7
                quadrillage2[test[6]][test[7]]=7
                rotation2=2
                acte=1
            if spawn2=="L2" and rotation2==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage2[test[2]+1][test[3]+1]<=7 and quadrillage2[test[0]+2][test[1]+2]<=7 and quadrillage2[test[6]+1][test[7]-1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+2][test[1]+2]=7
                quadrillage2[test[2]+1][test[3]+1]=7
                quadrillage2[test[4]][test[5]]=7
                quadrillage2[test[6]+1][test[7]-1]=7
                rotation2=3
                acte=1
            if spawn2=="L2" and rotation2==3 and test[1]>0 and  acte==0 and quadrillage2[test[2]+1][test[3]-1]<=7 and quadrillage2[test[6]-1][test[7]-1]<=7 and quadrillage2[test[4]+2][test[5]-2]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]][test[1]]=7
                quadrillage2[test[2]+1][test[3]-1]=7
                quadrillage2[test[4]+2][test[5]-2]=7
                quadrillage2[test[6]-1][test[7]-1]=7
                rotation2=4
                acte=1
            if spawn2=="L2" and rotation2==4 and test[1]>0 and acte==0 and quadrillage2[test[6]-2][test[7]-2]<=7 and quadrillage2[test[4]-1][test[5]-1]<=7 and quadrillage2[test[2]][test[3]]<=7 and quadrillage2[test[0]-1][test[1]+1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]-1][test[1]+1]=7
                quadrillage2[test[2]][test[3]]=7
                quadrillage2[test[4]-1][test[5]-1]=7
                quadrillage2[test[6]-2][test[7]-2]=7
                rotation2=1
                acte=1
            if spawn2=="L1" and rotation2==1 and acte==0 and quadrillage2[test[0]-1][test[1]+2]<=7 and quadrillage2[test[2]-1][test[3]+1]<=7 and quadrillage2[test[6]-1][test[7]-1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]-2][test[1]+2]=6
                quadrillage2[test[2]-1][test[3]+1]=6
                quadrillage2[test[4]][test[5]]=6
                quadrillage2[test[6]-1][test[7]-1]=6
                rotation2=2
                acte=1
            if spawn2=="L1" and rotation2==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage2[test[4]-1][test[5]+1]<=7 and quadrillage2[test[2]+1][test[3]+1]<=7 and quadrillage2[test[0]+2][test[1]+2]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[0]+2][test[1]+2]=6
                quadrillage2[test[2]+1][test[3]+1]=6
                quadrillage2[test[4]-1][test[5]+1]=6
                rotation2=3
                acte=1
            if spawn2=="L1" and rotation2==3  and acte==0 and quadrillage2[test[0]+1][test[1]+1]<=7 and quadrillage2[test[6]+2][test[7]-2]<=7 and quadrillage2[test[4]+1][test[5]-1]<=7:
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]+1]=6
                quadrillage2[test[4]+1][test[5]-1]=6
                quadrillage2[test[6]+2][test[7]-2]=6
                rotation2=4
                acte=1
            if spawn2=="L1" and rotation2==4 and test[1]>1 and acte==0 and quadrillage2[test[2]+1][test[3]-1]<=7 and quadrillage2[test[6]-2][test[7]-2]<=7 and quadrillage2[test[4]-1][test[5]-1]<=7:
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]][test[1]]=6
                quadrillage2[test[2]+1][test[3]-1]=6
                quadrillage2[test[4]-1][test[5]-1]=6
                quadrillage2[test[6]-2][test[7]-2]=6
                rotation2=1
                acte=1
            if spawn2=="Z" and rotation2==1 and acte==0 and quadrillage2[test[2]+2][test[3]]<=7 and quadrillage2[test[0]][test[1]+2]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[0]][test[1]+2]=1
                quadrillage2[test[2]+2][test[3]]=1
                rotation2=2
                acte=1
            if spawn2=="Z" and rotation2==2 and acte==0 and test[1]>1 and quadrillage2[test[6]-1][test[7]+1]<=7 and quadrillage2[test[2]-1][test[3]-1]<=7 and quadrillage2[test[4]][test[5]-1]<=7 and quadrillage2[test[0]][test[1]-1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]][test[1]-1]=1
                quadrillage2[test[4]][test[5]-1]=1
                quadrillage2[test[2]-1][test[3]-1]=1
                quadrillage2[test[6]-1][test[7]+1]=1
                rotation2=1
                acte=1
            if spawn2=="S" and rotation2==1 and acte==0 and quadrillage2[test[4]-1][test[5]]<=7 and quadrillage2[test[2]+1][test[3]-2]<=7 and quadrillage2[test[6]+1][test[7]]<=7 and quadrillage2[test[0]+1][test[1]]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[0]+1][test[1]]=5
                quadrillage2[test[6]+1][test[7]]=5
                quadrillage2[test[2]+1][test[3]-2]=5
                quadrillage2[test[4]-1][test[5]]=5
                rotation2=2
                acte=1
            if spawn2=="S" and rotation2==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage2[test[6]-1][test[7]-1]<=7 and quadrillage2[test[4]-1][test[5]+1]<=7 and quadrillage2[test[2]][test[3]+1]<=7 and quadrillage2[test[0]][test[1]+1]<=7:
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]][test[1]+1]=5
                quadrillage2[test[2]][test[3]+1]=5
                quadrillage2[test[4]-1][test[5]+1]=5
                quadrillage2[test[6]-1][test[7]-1]=5 #-1, pas -2+1
                rotation2=1
                acte=1
            if spawn2=="barre" and rotation2==1 and acte==0 and quadrillage2[test[0]-1][test[1]+2]<=7 and quadrillage2[test[2]+1][test[3]+1]<=7 and quadrillage2[test[6]+2][test[7]-1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]-1][test[1]+2]=3
                quadrillage2[test[2]+1][test[3]+1]=3
                quadrillage2[test[6]+2][test[7]-1]=3
                rotation2=2
                acte=1
            if spawn2=="barre" and rotation2==2 and test[1]>1 and test[1]<nbcolonne-1 and acte==0 and quadrillage2[test[6]-2][test[7]-2]<=7 and quadrillage2[test[0]+1][test[1]+1]<=7 and quadrillage2[test[4]-1][test[5]-1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]+1]=3
                quadrillage2[test[4]-1][test[5]-1]=3
                quadrillage2[test[6]-2][test[7]-2]=3
                rotation2=1
                acte=1
            if spawn2=="T" and rotation2==3 and acte==0 and quadrillage2[test[4]-1][test[5]-1]<=7:

                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[4]-1][test[5]-1]=4
                rotation2=4
                acte=1
            if spawn2=="T" and rotation2==2 and test[1]>0 and  acte==0 and quadrillage2[test[0]+1][test[1]-1]<=7:
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[0]+1][test[1]-1]=4
                rotation2=3
                acte=1
            if spawn2=="T" and rotation2==1 and acte==0 and quadrillage2[test[2]+1][test[3]+1]<=7:
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[2]+1][test[3]+1]=4
                rotation2=2
                acte=1
            if spawn2=="T" and rotation2==4  and test[1]<nbcolonne-1 and acte==0 and quadrillage2[test[6]-1][test[7]+1]<=7:

                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[6]-1][test[7]+1]=4
                rotation2=1
                acte=1
            print("rotation2=",rotation2)
        grille2()





    def rotationG2(event):
        global spawn2,rotation2
        test=[]
        acte=0
        for i in range (a):
            for j in range (b):
                if quadrillage2[i][j]>0 and quadrillage2[i][j]<8:
                    test.append(i)
                    test.append(j)
        if mouvbarre==1:
            acte=1
        if len(test)>0:
            if spawn2=="L2" and rotation2==1 and acte==0 and quadrillage2[test[4]+1][test[5]+1]<=7 and quadrillage2[test[2]+2][test[3]+2]<=7 and quadrillage2[test[0]+1][test[1]-1]<=7:
                hv=1
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[0]+1][test[1]-1]=7
                quadrillage2[test[2]+2][test[3]+2]=7
                quadrillage2[test[4]+1][test[5]+1]=7
                acte=1
                rotation2=4
            if spawn2=="L2" and rotation2==2 and test[1]>1 and acte==0 and quadrillage2[test[2]+1][test[3]-1]<=7 and quadrillage2[test[0]+2][test[1]-2]<=7 and quadrillage2[test[6]-1][test[7]-1]<=7:
                hv=2
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+2][test[1]-2]=7
                quadrillage2[test[2]+1][test[3]-1]=7
                quadrillage2[test[6]-1][test[7]-1]=7
                acte=1
                rotation2=1
            if spawn2=="L2" and rotation2==3 and acte==0 and quadrillage2[test[2]-1][test[3]-1]<=7 and quadrillage2[test[6]-1][test[7]+1]<=7 and quadrillage2[test[4]-2][test[5]-2]<=7:
                hv=3
                print(hv)
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[2]-1][test[3]-1]=7
                quadrillage2[test[4]-2][test[5]-2]=7
                quadrillage2[test[6]-1][test[7]+1]=7
                acte=1
                rotation2=2
            if spawn2=="L2" and rotation2==4 and acte==0  and test[1]<nbcolonne-3 and quadrillage2[test[6]-2][test[7]+2]<=7 and quadrillage2[test[4]-1][test[5]+1]<=7 and quadrillage2[test[0]+1][test[1]+1]<=7:
                hv=4
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]+1]=7
                quadrillage2[test[4]-1][test[5]+1]=7
                quadrillage2[test[6]-2][test[7]+2]=7
                acte=1
                rotation2=3
            if spawn2=="L1" and rotation2==1 and test[1]<nbcolonne-3 and acte==0 and quadrillage2[test[0]+2][test[1]+2]<=7 and quadrillage2[test[2]+1][test[3]+1]<=7 and quadrillage2[test[6]-1][test[7]+1]<=7:
                hv=5
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+2][test[1]+2]=6
                quadrillage2[test[2]+1][test[3]+1]=6
                quadrillage2[test[6]-1][test[7]+1]=6
                acte=1
                rotation2=4
            if spawn2=="L1" and rotation2==2  and test[1]>1 and acte==0 and quadrillage2[test[4]+1][test[5]+1]<=7 and quadrillage2[test[2]+1][test[3]-1]<=7 and quadrillage2[test[0]+2][test[1]-2]<=7:
                hv=6
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[0]+2][test[1]-2]=6
                quadrillage2[test[2]+1][test[3]-1]=6
                quadrillage2[test[4]+1][test[5]+1]=6
                acte=1
                rotation2=1
            if spawn2=="L1" and rotation2==3 and test[1]>0 and acte==0 and quadrillage2[test[0]+1][test[1]-1]<=7 and quadrillage2[test[6]-2][test[7]-2]<=7 and quadrillage2[test[4]-1][test[5]+1]<=7:
                hv=7
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]-1]=6
                quadrillage2[test[4]-1][test[5]-1]=6
                quadrillage2[test[6]-2][test[7]-2]=6
                acte=1
                rotation2=2
            if spawn2=="L1" and rotation2==4 and test[1]<nbcolonne-2 and acte==0 and quadrillage2[test[2]-1][test[3]-1]<=7 and quadrillage2[test[6]-2][test[7]+2]<=7 and quadrillage2[test[4]-1][test[5]+1]<=7:
                hv=8
                print(hv)
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[2]-1][test[3]-1]=6
                quadrillage2[test[4]-1][test[5]+1]=6
                quadrillage2[test[6]-2][test[7]+2]=6
                acte=1
                rotation2=3
            if spawn2=="Z" and rotation2==1 and acte==0 and quadrillage2[test[2]+2][test[3]]<=7 and quadrillage2[test[0]][test[1]+2]<=7:
                hv=9
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[0]][test[1]+2]=1
                quadrillage2[test[2]+2][test[3]]=1
                rotation2=2
                acte=1
            if spawn2=="Z" and rotation2==2 and acte==0 and test[1]>1 and quadrillage2[test[6]-1][test[7]+1]<=7 and quadrillage2[test[2]-1][test[3]-1]<=7 and quadrillage2[test[4]][test[5]-1]<=7 and quadrillage2[test[0]][test[1]-1]<=7:
                hv=10
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]][test[1]-1]=1
                quadrillage2[test[2]-1][test[3]-1]=1
                quadrillage2[test[4]][test[5]-1]=1
                quadrillage2[test[6]-1][test[7]+1]=1
                rotation2=1
                acte=1
            if spawn2=="S" and rotation2==1 and acte==0 and quadrillage2[test[4]-1][test[5]]<=7 and quadrillage2[test[2]+1][test[3]-2]<=7 and quadrillage2[test[6]+1][test[7]]<=7 and quadrillage2[test[0]+1][test[1]]<=7:
                hv=11
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[4]+1][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]]=5
                quadrillage2[test[2]+1][test[3]-2]=5
                quadrillage2[test[4]-1][test[5]]=5
                quadrillage2[test[6]+1][test[7]]=5
                rotation2=2
                acte=1
            if spawn2=="S" and rotation2==2 and acte==0 and test[1]<nbcolonne-2 and quadrillage2[test[6]-1][test[7]-1]<=7 and quadrillage2[test[4]-1][test[5]+1]<=7 and quadrillage2[test[2]][test[3]+1]<=7 and quadrillage2[test[0]][test[1]+1]<=7:
                hv=12
                print(hv)
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]][test[1]+1]=5
                quadrillage2[test[2]][test[3]+1]=5
                quadrillage2[test[4]-1][test[5]+1]=5
                quadrillage2[test[6]-1][test[7]-1]=5
                rotation2=1
                acte=1
            if spawn2=="barre" and rotation2==1 and acte==0 and quadrillage2[test[0]+2][test[1]+2]<=7 and quadrillage2[test[2]+1][test[3]+1]<=7 and quadrillage2[test[6]-1][test[7]-1]<=7:
                hv=13
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[2]][test[3]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+2][test[1]+2]=3
                quadrillage2[test[2]+1][test[3]+1]=3
                quadrillage2[test[6]-1][test[7]-1]=3
                acte=1
                rotation2=2
            if spawn2=="barre" and rotation2==2 and test[1]>1 and test[1]<nbcolonne-1 and acte==0 and quadrillage2[test[6]-2][test[7]-2]<=7 and quadrillage2[test[4]-1][test[5]-1]<=7 and quadrillage2[test[0]+1][test[1]+1]<=7:
                hv=14
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[4]][test[5]]=0
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[0]+1][test[1]+1]=3
                quadrillage2[test[4]-1][test[5]-1]=3
                quadrillage2[test[6]-2][test[7]-2]=3
                acte=1
                rotation2=1
            if spawn2=="T" and rotation2==1 and acte==0 and quadrillage2[test[6]+1][test[7]-1]<=7:
                hv=20
                print(hv)
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[6]+1][test[7]-1]=4


                acte=1
                rotation2=4
            if spawn2=="T" and rotation2==2 and test[1]>0 and acte==0 and quadrillage2[test[6]-1][test[7]-1]<=7:
                hv=17
                print(hv)
                quadrillage2[test[6]][test[7]]=0
                quadrillage2[test[6]-1][test[7]-1]=4
                acte=1
                rotation2=1
            if spawn2=="T" and rotation2==3 and acte==0 and quadrillage2[test[0]-1][test[1]+1]<=7:
                hv=18
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[0]-1][test[1]+1]=4
                acte=1
                rotation2=2
            if spawn2=="T" and rotation2==4 and test[1]<nbcolonne-1 and acte==0 and quadrillage2[test[0]+1][test[1]+1]<=7:
                hv=19
                print(hv)
                quadrillage2[test[0]][test[1]]=0
                quadrillage2[test[0]+1][test[1]+1]=4
                acte=1
                rotation2=3
            print("rotation2=",rotation2)
        grille2()

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
                    if quadrillage[ligne-6][j]>0 and quadrillage[ligne-6][j]<8:
                        piece.append(ligne-6)
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
        arg1.after(5*(int(vitesse*acceleration)),mouvement)
    def mouvement2():
        global acceleration2,quadrillage2,j,vitesse2,piece2,nbpiece2,scoreligne2,mouvbarre2,ligne2
        acte=0
        if ligne2<6 and spawn=="barre":
            mouvbarre2==1
        testdescente2=[]
        piece2=[]
        if len(testdescente2)>0:
            testdescente2=[]
        if len(piece2)>0:
            piece2=[]
        for j in range (b):
            if  ligne2<a-3:

                    if quadrillage2[ligne2+2][j]>0 and quadrillage2[ligne2+2][j]<8:
                        piece2.append(ligne2+2)
                        piece2.append(j)
                    if quadrillage2[ligne2+1][j]>0 and quadrillage2[ligne2+1][j]<8:
                        piece2.append(ligne2+1)
                        piece2.append(j)
                    if quadrillage2[ligne2][j]>0 and quadrillage2[ligne2][j]<8:
                        piece2.append(ligne2)
                        piece2.append(j)
                    if quadrillage2[ligne2-1][j]>0 and quadrillage2[ligne2-1][j]<8:
                        piece2.append(ligne2-1)
                        piece2.append(j)
                    if quadrillage2[ligne2-2][j]>0 and quadrillage2[ligne2-2][j]<8:
                        piece2.append(ligne2-2)
                        piece2.append(j)
                    if quadrillage2[ligne2-3][j]>0 and quadrillage2[ligne2-3][j]<8:
                        piece2.append(ligne2-3)
                        piece2.append(j)
                    if quadrillage2[ligne2-4][j]>0 and quadrillage2[ligne2-4][j]<8:
                        piece2.append(ligne2-4)
                        piece2.append(j)
                    if quadrillage2[ligne2-5][j]>0 and quadrillage2[ligne2-5][j]<8:
                        piece2.append(ligne2-5)
                        piece2.append(j)
                    if quadrillage2[ligne2-6][j]>0 and quadrillage2[ligne2-6][j]<8:
                        piece2.append(ligne2-6)
                        piece2.append(j)

        nbpiece2=len(piece2)
        if acte==0 and nbpiece2>0:
            if nbpiece2==18:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8 and quadrillage2[piece2[6]+1][piece2[7]]<8 and quadrillage2[piece2[10]+1][piece2[11]]<8 and quadrillage2[piece2[8]+1][piece2[9]]<8 and quadrillage2[piece2[14]+1][piece2[15]]<8 and quadrillage2[piece2[12]+1][piece2[13]]<8 and quadrillage2[piece2[16]+1][piece2[17]]<8:
                    quadrillage2[piece2[16]][piece2[17]]=0
                    quadrillage2[piece2[14]][piece2[15]]=0
                    quadrillage2[piece2[12]][piece2[13]]=0
                    quadrillage2[piece2[10]][piece2[11]]=0
                    quadrillage2[piece2[8]][piece2[9]]=0
                    quadrillage2[piece2[6]][piece2[7]]=0
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[16]+1][piece2[17]]=color2
                    quadrillage2[piece2[14]+1][piece2[15]]=color2
                    quadrillage2[piece2[12]+1][piece2[13]]=color2
                    quadrillage2[piece2[10]+1][piece2[11]]=color2
                    quadrillage2[piece2[8]+1][piece2[9]]=color2
                    quadrillage2[piece2[6]+1][piece2[7]]=color2
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[16]][piece2[17]]=quadrillage2[piece2[16]][piece2[17]]+10
                    quadrillage2[piece2[14]][piece2[15]]=quadrillage2[piece2[14]][piece2[15]]+10
                    quadrillage2[piece2[12]][piece2[13]]=quadrillage2[piece2[12]][piece2[13]]+10
                    quadrillage2[piece2[10]][piece2[11]]=quadrillage2[piece2[10]][piece2[11]]+10
                    quadrillage2[piece2[8]][piece2[9]]=quadrillage2[piece2[8]][piece2[9]]+10
                    quadrillage2[piece2[6]][piece2[7]]=quadrillage2[piece2[6]][piece2[7]]+10
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==16:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8 and quadrillage2[piece2[6]+1][piece2[7]]<8 and quadrillage2[piece2[8]+1][piece2[9]]<8 and quadrillage2[piece2[14]+1][piece2[15]]<8 and quadrillage2[piece2[12]+1][piece2[13]]<8:
                    quadrillage2[piece2[14]][piece2[15]]=0
                    quadrillage2[piece2[12]][piece2[13]]=0
                    quadrillage2[piece2[10]][piece2[11]]=0
                    quadrillage2[piece2[8]][piece2[9]]=0
                    quadrillage2[piece2[6]][piece2[7]]=0
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[14]+1][piece2[15]]=color2
                    quadrillage2[piece2[12]+1][piece2[13]]=color2
                    quadrillage2[piece2[10]+1][piece2[11]]=color2
                    quadrillage2[piece2[8]+1][piece2[9]]=color2
                    quadrillage2[piece2[6]+1][piece2[7]]=color2
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[14]][piece2[15]]=quadrillage2[piece2[14]][piece2[15]]+10
                    quadrillage2[piece2[12]][piece2[13]]=quadrillage2[piece2[12]][piece2[13]]+10
                    quadrillage2[piece2[10]][piece2[11]]=quadrillage2[piece2[10]][piece2[11]]+10
                    quadrillage2[piece2[8]][piece2[9]]=quadrillage2[piece2[8]][piece2[9]]+10
                    quadrillage2[piece2[6]][piece2[7]]=quadrillage2[piece2[6]][piece2[7]]+10
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==14:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8 and quadrillage2[piece2[6]+1][piece2[7]]<8 and quadrillage2[piece2[8]+1][piece2[9]]<8 and quadrillage2[piece2[12]+1][piece2[13]]<8:
                    quadrillage2[piece2[12]][piece2[13]]=0
                    quadrillage2[piece2[10]][piece2[11]]=0
                    quadrillage2[piece2[8]][piece2[9]]=0
                    quadrillage2[piece2[6]][piece2[7]]=0
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[12]+1][piece2[13]]=color2
                    quadrillage2[piece2[10]+1][piece2[11]]=color2
                    quadrillage2[piece2[8]+1][piece2[9]]=color2
                    quadrillage2[piece2[6]+1][piece2[7]]=color2
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[12]][piece2[13]]=quadrillage2[piece2[12]][piece2[13]]+10
                    quadrillage2[piece2[10]][piece2[11]]=quadrillage2[piece2[10]][piece2[11]]+10
                    quadrillage2[piece2[8]][piece2[9]]=quadrillage2[piece2[8]][piece2[9]]+10
                    quadrillage2[piece2[6]][piece2[7]]=quadrillage2[piece2[6]][piece2[7]]+10
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==12:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8 and quadrillage2[piece2[6]+1][piece2[7]]<8 and quadrillage2[piece2[8]+1][piece2[9]]<8:
                    quadrillage2[piece2[10]][piece2[11]]=0
                    quadrillage2[piece2[8]][piece2[9]]=0
                    quadrillage2[piece2[6]][piece2[7]]=0
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[10]+1][piece2[11]]=color2
                    quadrillage2[piece2[8]+1][piece2[9]]=color2
                    quadrillage2[piece2[6]+1][piece2[7]]=color2
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[10]][piece2[11]]=quadrillage2[piece2[10]][piece2[11]]+10
                    quadrillage2[piece2[8]][piece2[9]]=quadrillage2[piece2[8]][piece2[9]]+10
                    quadrillage2[piece2[6]][piece2[7]]=quadrillage2[piece2[6]][piece2[7]]+10
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==10:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8 and quadrillage2[piece2[6]+1][piece2[7]]<8 and quadrillage2[piece2[8]+1][piece2[9]]<8:
                    quadrillage2[piece2[8]][piece2[9]]=0
                    quadrillage2[piece2[6]][piece2[7]]=0
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[8]+1][piece2[9]]=color2
                    quadrillage2[piece2[6]+1][piece2[7]]=color2
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2

                else:
                    quadrillage2[piece2[8]][piece2[9]]=quadrillage2[piece2[8]][piece2[9]]+10
                    quadrillage2[piece2[6]][piece2[7]]=quadrillage2[piece2[6]][piece2[7]]+10
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==8:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8 and quadrillage2[piece2[6]+1][piece2[7]]<8:
                    quadrillage2[piece2[6]][piece2[7]]=0
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[6]+1][piece2[7]]=color2
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[6]][piece2[7]]=quadrillage2[piece2[6]][piece2[7]]+10
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==2:
                if quadrillage2[piece2[0]+1][piece2[1]]<8:
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==4:
                if quadrillage2[piece2[0]][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8:
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
            if nbpiece2==6:
                if quadrillage2[piece2[0]+1][piece2[1]]<8 and quadrillage2[piece2[2]+1][piece2[3]]<8 and quadrillage2[piece2[4]+1][piece2[5]]<8:
                    quadrillage2[piece2[4]][piece2[5]]=0
                    quadrillage2[piece2[2]][piece2[3]]=0
                    quadrillage2[piece2[0]][piece2[1]]=0
                    quadrillage2[piece2[4]+1][piece2[5]]=color2
                    quadrillage2[piece2[2]+1][piece2[3]]=color2
                    quadrillage2[piece2[0]+1][piece2[1]]=color2
                else:
                    quadrillage2[piece2[4]][piece2[5]]=quadrillage2[piece2[4]][piece2[5]]+10
                    quadrillage2[piece2[2]][piece2[3]]=quadrillage2[piece2[2]][piece2[3]]+10
                    quadrillage2[piece2[0]][piece2[1]]=quadrillage2[piece2[0]][piece2[1]]+10
        ligne2=ligne2+1
        if ligne2==a-3:
            ligne2=4
            objet2()
            objetsuite2()
            grilleaffichage2()




        scoreligne2=len(ligne_supprimée2)
        Lsj1.config(text=("Score:",scoreligne2))
        grille2()
        arg1.after(5*(int(vitesse2*acceleration)),mouvement2)

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
    def grille2():
        global quadrillage2,ligne_supprimée2,verif,test3,test4
        destrouy=0
        Cj2.delete(ALL)
        for j in range(b2+1):
            x=j*20
            y=0
            Cj2.create_line(x,y,x,y+560,fill="light grey",width=0.5)
        for i in range(28):
            x=0
            y=i*20
            Cj2.create_line(x,y,x+b2*20,y,fill="light grey",width=0.5)
        for j in range(b2):
            x=j*20
            y=580
            Cj2.create_line(0,y,nbcolonne2*10,y+140,fill="light grey",width=0.5)
            Cj2.create_line(x,y,nbcolonne2*10,y+140,fill="light grey",width=0.5)
            Cj2.create_line((b2)*20,y,nbcolonne2*10,y+140,fill="light grey",width=0.5)
        for i in range(1):
            for j in range (b):
                if quadrillage2[5+i][j]>=8:
                    print("perdu j2")
                    destrouy=1
        if destrouy==1:
            arg1.destroy()
        else:
            for i in range (a2):
                for j in range (b2):
                    if quadrillage2[i][j]>0:
                        x=j*20
                        y=i*20
                        test3=quadrillage2[i][j]
                        if test3!=0:
                            test4 = couleur[test3]
                            Cj2.create_rectangle(x,y,x+20,y+20,fill=test4)
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
                        quadrillage[i]=[]
                        for y in range(nbcolonne):
                            quadrillage[casesuppr].append(0)
                        arg1.after(500,descente)
        arg1.after(10,verification)
    def verification2():
        global casesuppr2,action
        for i in range(a2):
            for j in range(b2):
                if quadrillage2[i][j]==9:
                    quadrillage2[i][j]=0
        for i in range (a2):
                verif = 0
                for j in range (b2) :
                    if quadrillage2[i][j]>=10 :
                        verif= verif + 1
                    if verif == nbcolonne2 :
                        action2=1
                        verif=0
                        ligne_supprimée2.append (i)
                        casesuppr2=i
                        quadrillage2[i]=[]
                        for y in range(nbcolonne2):
                            quadrillage2[casesuppr2].append(0)
                        arg1.after(500,descente2)
        arg1.after(10,verification2)
    def descente():
        global quadrillage,Chargement1
        Chargement1=Chargement1+1
        GrilleDescente()
    def GrilleDescente():
        global quadrillage,test3,test4,ligne,action,acceleration
        action=0
        if scoreligne>9:
            acceleration=9
        if scoreligne>19:
            acceleration=5
        if scoreligne>29:
            acceleration=2
    def descente2():
        global quadrillage2,Chargement2
        Chargement2=Chargement2+1
        GrilleDescente2()
    def GrilleDescente2():
        global quadrillage2,test3,test4,action2,acceleration2
        action2=0
        if scoreligne2>9:
            acceleration2=9
        if scoreligne2>19:
            acceleration2=5
        if scoreligne2>29:
            acceleration2=2
    def analyse():
        global quadrillage,action
        if action==0:
            for i in range (29):
                if quadrillage[i]==quadrillage[30]:
                    for j in range(b):
                        if quadrillage[i-1][j]>10:
                            quadrillage[i][j]=quadrillage[i-1][j]
                            quadrillage[i-1][j]=0
        arg1.after(400,analyse)
    def analyse2():
        global quadrillage2,action2
        if action2==0:
            for i in range (29):
                if quadrillage2[i]==quadrillage2[30]:
                    for j in range(b2):
                        if quadrillage2[i-1][j]>10:
                            quadrillage2[i][j]=quadrillage2[i-1][j]
                            quadrillage2[i-1][j]=0
        arg1.after(300,analyse2)
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

    def droite2(event):
        global quadrillage2,color2
        test=[]
        acte=0
        for i in range (a2):
            for j in range (b2):
                if quadrillage2[i][j]>0 and quadrillage2[i][j]<8:
                    test.append(i)
                    test.append(j)
        pop=len(test)
        for limiteD in range (pop//2):
            if test[limiteD*2+1]==nbcolonne2-1:
                acte=1

        for limiteDbloc in range(pop//2):
            if acte!=1:
                if quadrillage2[test[limiteDbloc*2]][test[limiteDbloc*2+1]+1]>10:
                    acte=1
        if acte==0:
            if pop>18 and quadrillage2[test[18]][test[19]+1]<8:
                quadrillage2[test[18]][test[19]+1]=color2
                quadrillage2[test[18]][test[19]]=0
            if pop>16 and quadrillage2[test[16]][test[17]+1]<8:
                quadrillage2[test[16]][test[17]+1]=color2
                quadrillage2[test[16]][test[17]]=0
            if pop>14 and quadrillage2[test[14]][test[15]+1]<8:
                quadrillage2[test[14]][test[15]+1]=color2
                quadrillage2[test[14]][test[15]]=0
            if pop>12 and quadrillage2[test[12]][test[13]+1]<8:
                quadrillage2[test[12]][test[13]+1]=color2
                quadrillage2[test[12]][test[13]]=0
            if pop>10 and quadrillage2[test[10]][test[11]+1]<8:
                quadrillage2[test[10]][test[11]+1]=color2
                quadrillage2[test[10]][test[11]]=0
            if pop>8 and quadrillage2[test[8]][test[9]+1]<8:
                quadrillage2[test[8]][test[9]+1]=color2
                quadrillage2[test[8]][test[9]]=0
            if pop>6 and quadrillage2[test[6]][test[7]+1]<8:
                quadrillage2[test[6]][test[7]+1]=color2
                quadrillage2[test[6]][test[7]]=0
            if pop>4 and quadrillage2[test[4]][test[5]+1]<8:
                quadrillage2[test[4]][test[5]+1]=color2
                quadrillage2[test[4]][test[5]]=0
            if pop>2 and quadrillage2[test[2]][test[3]+1]<8:
                quadrillage2[test[2]][test[3]+1]=color2
                quadrillage2[test[2]][test[3]]=0
            if pop>0 and quadrillage2[test[0]][test[1]+1]<8:
                quadrillage2[test[0]][test[1]+1]=color2
                quadrillage2[test[0]][test[1]]=0
        grille2()
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
    def gauche2(event):
        global quadrillage2,color2
        test=[]
        acte=0
        for i in range (a2):
            for j in range (b2):
                if quadrillage2[i][j]>0 and quadrillage2[i][j]<8:
                    test.append(i)
                    test.append(j)
                    s=len(test)
        pop=len(test)
        for limiteG in range (pop//2):
            if test[limiteG*2+1]==0:
                acte=1
        for limiteGbloc in range(pop//2):
            if quadrillage2[test[limiteGbloc*2]][test[limiteGbloc*2+1]-1]>=8:
                acte=1
        if acte==0:
            if pop>0  and quadrillage2[test[0]][test[1]-1]<8:
                quadrillage2[test[0]][test[1]-1]=color2
                quadrillage2[test[0]][test[1]]=0
            if pop>2 and quadrillage2[test[2]][test[3]-1]<8:
                quadrillage2[test[2]][test[3]-1]=color2
                quadrillage2[test[2]][test[3]]=0
            if pop>4 and quadrillage2[test[4]][test[5]-1]<8:
                quadrillage2[test[4]][test[5]-1]=color2
                quadrillage2[test[4]][test[5]]=0
            if pop>6 and quadrillage2[test[6]][test[7]-1]<8:
                quadrillage2[test[6]][test[7]-1]=color2
                quadrillage2[test[6]][test[7]]=0
            if pop>8 and quadrillage2[test[8]][test[9]-1]<8:
                quadrillage2[test[8]][test[9]-1]=color2
                quadrillage2[test[8]][test[9]]=0
            if pop>10 and quadrillage2[test[10]][test[11]-1]<8:
                quadrillage2[test[10]][test[11]-1]=color2
                quadrillage2[test[10]][test[11]]=0
            if pop>12 and quadrillage2[test[12]][test[13]-1]<8:
                quadrillage2[test[12]][test[13]-1]=color2
                quadrillage2[test[12]][test[13]]=0
            if pop>14 and quadrillage2[test[14]][test[15]-1]<8:
                quadrillage2[test[14]][test[15]-1]=color2
                quadrillage2[test[14]][test[15]]=0
            if pop>16 and quadrillage2[test[16]][test[17]-1]<8:
                quadrillage2[test[16]][test[17]-1]=color2
                quadrillage2[test[16]][test[17]]=0
            if pop>18 and quadrillage2[test[18]][test[19]-1]<8:
                quadrillage2[test[18]][test[19]-1]=color2
                quadrillage2[test[18]][test[19]]=0

        grille2()
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
    def grilleaffichage2():
        global quadrillageaffichagej2,test3,test4
        for i in range (6):
            for j in range (5):
                C2j2.create_rectangle(i*20,j*20,i*20+20,j*20+20,fill="white")
        for i in range (5):
            for j in range (5):
                if quadrillageaffichagej2[i][j]>0:
                    x=j*20
                    y=i*20
                    test3=quadrillageaffichagej2[i][j]
                    if test3!=0:
                        test4 = couleur[test3]
                        C2j2.create_rectangle(x,y,x+20,y+20,fill=test4)
    def Cvitesseon():
        global vitesse
        vitesse=2
    def Cvitesseoff():
        global vitesse
        vitesse=10
    def scanon2(event):
        global t2
        t2 = event.keysym
        if t2==touche10sauv:
            Cvitesseon2()
        if t2==touche1sauv:
            Cvitesseon()
    def scanoff2(event):
        global t2
        t2 = event.keysym
        if t2==touche10sauv:
            Cvitesseoff2()
        if t2==touche1sauv:
            Cvitesseoff()
    def Cvitesseon2():
        global vitesse2
        vitesse2=2
    def Cvitesseoff2():
        global vitesse2
        vitesse2=10
    def brawlalalalala(event):
        global acceleration,acta
        for i in range(14):
            for j in range(nbcolonne-1):
                quadrillage[i+14][j]=randint(11,17)
            for j in range(nbcolonne2-1):
                quadrillage2[i+14][j]=randint(11,17)
        quadrillage[i]=[12]*nbcolonne
        quadrillage2[i]=[12]*nbcolonne2
    def spawnapres():
        global spawn, pieceapres
        if pieceapres == "" :
            spawn = choice(list_objet)
        else :
            spawn = pieceapres
    def spawnapres2():
        global spawn2, spawnafter2
        if spawnafter2 == "" :
            spawn2 = choice(list_objet)
        else :
            spawn2 = spawnafter2

    arg1.geometry("1000x600")
    Cj1=Canvas(arg1,width=300,height=700,bg="white")
    C2j1=Canvas(arg1,width=200,height=620,bg="white")
    C2j1.place(x=300,y=0)
    Cj1.place(x=0,y=-100)
    Cj2=Canvas(arg1,width=300,height=700,bg="white")
    C2j2=Canvas(arg1,width=200,height=620,bg="white")
    C2j2.place(x=500,y=0)
    Cj2.place(x=700,y=-100)
    Lsj1=Label(arg1,text=("Score:",scoreligne),bg="white")
    Lsj2=Label(arg1,text=("Score:",scoreligne2),bg="white")
    Lsj1.place(x=350,y=200)
    Lsj2.place(x=550,y=200)
    quadrillage=[]
    quadrillage2=[]
    for z in range (35):
        quadrillage.append([0]*nbcolonne)
    quadrillage[28]=[]
    for y in range(nbcolonne):
        quadrillage[28].append(8)
    a=len(quadrillage)
    b=len(quadrillage[1])
    for z in range (35):
        quadrillage2.append([0]*nbcolonne2)
    quadrillage2[28]=[]
    for y in range(nbcolonne2):
        quadrillage2[28].append(8)
    a2=len(quadrillage2)
    b2=len(quadrillage2[1])
    print(a,b)
    objetsuite()
    mouvement()
    PowerUpPret1()
    PowerUpPret2()
    objetsuite2()
    mouvement2()
    music4()
    touche1sauv=touche1
    touche10sauv=touche10
    touche2="<"+touche2+">"
    touche3="<"+touche3+">"
    touche4="<"+touche4+">"
    touche5="<"+touche5+">"
    touche6="<"+touche6+">"
    touche11="<"+touche11+">"
    touche12="<"+touche12+">"
    touche13="<"+touche13+">"
    touche14="<"+touche14+">"
    touche15="<"+touche15+">"
    grille()
    analyse()
    analyse2()
    verification()
    grille2()
    grilleaffichage2()
    grilleaffichage1()
    verification2()
    arg1.title("Tetris Versus")
    arg1.bind_all("<KeyPress>",scanon2)
    arg1.bind_all("<KeyRelease>",scanoff2)
    arg1.bind(touche6,rotationG)
    arg1.bind(touche15,rotationG2)
    arg1.bind(touche3,gauche)
    arg1.bind(touche2,droite)
    arg1.bind(touche4,changepiece)
    arg1.bind_all("<KeyPress>",scanon2)
    arg1.bind_all("<KeyRelease>",scanoff2)
    arg1.bind(touche12,gauche2)
    arg1.bind("b",brawlalalalala)
    arg1.bind(touche11,droite2)
    arg1.bind(touche13,changepiece2)
    GrilleDescente()

    arg1.mainloop()

pygame.mixer.music.pause()
