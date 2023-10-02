import BOUYAc
import TetrisVersus
import HARDCORE
from tkinter import *
import pygame
pygame.init()
fen=Tk()
fen.geometry("499x600")
fen.title("||Tetris||")
C=Canvas(fen,width=500,height=600,bg="white")
C.pack()
couleur=["black","red","yellow","sky blue","purple","light green","blue","orange"]
nbcolonne=15
stop=1
nbcolonne2=15
scoreligne=0
scoreligne2=0
Menu=PhotoImage(file="MenuPNG.png")
Modes=PhotoImage(file="ModesPNG.png")
J1J2=PhotoImage(file="J1J2.png")
Option=PhotoImage(file="Reglage3.png")
a=0
t=""
t2=""
t3=""
type2touche=""
touchegauche="k"
touchedroite="m"
touchebas="l"
toucheRdroite="p"
toucheRgauche="o"
toucheaide="i"
touchegj2="q"
touchedj2="d"
touchebj2="s"
toucheRdj2="z"
toucheRgj2="a"
toucheaj2="e"
piecedujoueuriR1=[1,1,2,2]
piecedujoueurjR1=[2,3,2,3]
piecedujoueuriR2=[1,1,2,2]
piecedujoueurjR2=[2,3,2,3]
piecedujoueuriR3=[1,1,2,2]
piecedujoueurjR3=[2,3,2,3]
piecedujoueuriR4=[1,1,2,2]
piecedujoueurjR4=[2,3,2,3]

couleurjoueur=1
def Editor():
    global itm,C,couleurjoueur,Rec,stop
    itm=0
    def enregistrement():
        global a,piecedujoueurjR1,piecedujoueuriR1,chou,stop,piecedujoueurjR2,piecedujoueuriR2,piecedujoueurjR3,piecedujoueuriR3,piecedujoueurjR4,piecedujoueuriR4
        piecedujoueurjR1=[]
        piecedujoueuriR1=[]
        piecedujoueurjR2=[]
        piecedujoueuriR2=[]
        piecedujoueurjR3=[]
        piecedujoueuriR3=[]
        piecedujoueurjR4=[]
        piecedujoueuriR4=[]
        stop=2
        C.delete(chou)
        if a==1:
            for i in range(4):
                for j in range (4):
                    if grille[i][j]>=1:
                        piecedujoueuriR1.append(j)
                        piecedujoueurjR1.append(i)
            for i in range(4):
                for j in range(4):
                    grille[j][3-i]=grille[i][j]
                    grille[i][j]=0
            for i in range(4):
                for j in range (4):
                    if grille[i][j]>=1:
                        piecedujoueuriR2.append(j)
                        piecedujoueurjR2.append(i)
            for i in range(4):
                for j in range(4):
                    grille[j][3-i]=grille[i][j]
                    grille[i][j]=0
            for i in range(4):
                for j in range (4):
                    if grille[i][j]>=1:
                        piecedujoueuriR3.append(j)
                        piecedujoueurjR3.append(i)
            for i in range(4):
                for j in range(4):
                    grille[j][3-i]=grille[i][j]
                    grille[i][j]=0
            for i in range(4):
                for j in range (4):
                    if grille[i][j]>=1:
                        piecedujoueuriR4.append(j)
                        piecedujoueurjR4.append(i)
            fen.unbind("<Button-1>")
            fen.bind("<Button-1>",startoption)
            fen.title("||Tetris||")
            for i in range(4):
                for j in range(4):
                    grille[i][j]=0

            C.configure(width=500,height=600)
            fen.geometry("500x600")
            C.create_image(0,0,anchor=NW,image=Menu)
            a=0
    def analyse(event):
        global itm,couleurjoueur,Rec
        acte=0
        if event.x>=633 and event.x<=701 and event.y>=298 and event.y<=366:
            if couleurjoueur<7:
                couleurjoueur=couleurjoueur+1
            else:
                couleurjoueur=1
            C.delete(Rec)
            Rec=C.create_rectangle(633,298,703,368,fill=couleur[couleurjoueur])
        if event.x>=607 and event.y>=66 and event.x<=730 and event.y<=108 and itm>=3:
            enregistrement()
        if event.x>=607 and event.y>=2 and event.x<=730 and event.y<=45:
            print("reset")
            itm=0
            for i in range(4):
                for j in range(4):
                    grille[i][j]=0
            C.delete(ALL)
            C.create_image(1,1,image=grillage,anchor=NW)
            Rec=C.create_rectangle(633,298,703,368,fill=couleur[couleurjoueur])

        for i in range(4):
            for j in range(4):
                if event.x>=150*i and event.x<=150*(i+1) and event.y>=150*j and event.y<=150*(j+1):
                    if grille[i][j]>=1:
                        grille[i][j]=0
                        print("blanc")
                        acte=1
                        if itm>>0:
                            itm=itm-1
                if event.x>=150*i and event.x<=150*(i+1) and event.y>=150*j and event.y<=150*(j+1) and itm!=9 and acte==0:
                    if grille[i][j]==0 and itm==0:
                        grille[i][j]=2
                        itm=itm+1
                        acte=1
                        print("red")
                if event.x>=150*i and event.x<=150*(i+1) and event.y>=150*j and event.y<=150*(j+1) and itm!=9 and acte==0:
                    if grille[i][j]==0 and grille[i+1][j]>=1 or grille[i][j+1]>=1 or grille[i-1][j]>=1 or grille[i][j-1]>=1 :
                        grille[i][j]=1
                        itm=itm+1
                        print("bleu")
                        acte=1
    def scanon(w,v):
        x=w*150
        y=v*150
        C.create_rectangle(x+2,y+2,x+149,y+149,fill="blue")
    def grilleediteur():
        global chou,stop
        if stop<=1:
            C.delete(ALL)
            chou=C.create_image(1,1,image=grillage,anchor=NW)
            Rec=C.create_rectangle(633,298,703,368,fill=couleur[couleurjoueur])
            for i in range(4):
                for j in range(4):
                    if grille[i][j]>0:
                        C.create_rectangle(i*150+2,j*150+2,i*150+149,j*150+149,fill=couleur[couleurjoueur])

            fen.after(10*stop,grilleediteur)

    fen.geometry("732x602")
    fen.title("L'EDITEUR ! CREER VOTRE PROPRE PIECE POUR LE MODE VERSUS WOW")
    grillage=PhotoImage(file="GrilleEdit.png")
    C.create_text(604,2,text="reset",font=3,anchor=NW)
    C.create_text(604,26,font=3,text="valider \n(votre pièce doit\navoir au moins \n3 bloques !)",anchor=NW)
    C.place(x=0,y=0)
    C.create_image(1,1,image=grillage,anchor=NW)
    Rec=C.create_rectangle(633,298,703,367,fill=couleur[couleurjoueur])
    fen.bind("<Button-1>",analyse)
    grille=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    grilleediteur()
    fen.mainloop()
def analyse(event):
    global t,type2touche,t2
    t=event.keysym
    t2=event.char
    type2touche=t2
    print(touchebas,touchedroite,touchegauche,toucheRdroite,toucheRgauche,toucheaide)
def analyse2(event):
    global t3,type2touche,t2
    t3=event.keysym
    t2=event.char
    type2touche=t2
    print(touchebj2,touchedj2,touchegj2,toucheRdj2,toucheRgj2,toucheaj2)
def DefinirToucheRgauche():
    global t,toucheRgauche
    if t=="":
        fen.bind_all("<KeyPress>",analyse)
        fen.after(1,DefinirToucheRgauche)
    else:
        toucheRgauche=t
        print(toucheRgauche,t)
        t=""
        fen.unbind_all("<KeyPress>")
def DefinirToucheBas():
    global t,touchebas
    if t=="":
        fen.bind_all("<KeyPress>",analyse)
        fen.after(1,DefinirToucheBas)
    else:
        touchebas=t
        print(touchebas,t)
        t=""
        fen.unbind_all("<KeyPress>")
def DefinirToucheGauche():
    global t,touchegauche
    if t=="":
        fen.bind_all("<KeyPress>",analyse)
        fen.after(1,DefinirToucheGauche)
    else:
        touchegauche=t
        print(touchegauche,t)
        t=""
        fen.unbind_all("<KeyPress>")
def DefinirToucheDroite():
    global t,touchedroite
    if t=="":
        fen.bind_all("<KeyPress>",analyse)
        fen.after(1,DefinirToucheDroite)
    else:
        touchedroite=t
        print(touchedroite,t)
        t=""
        fen.unbind_all("<KeyPress>")
def DefinirToucheRdroite():
    global t,toucheRdroite
    if t=="":
        fen.bind_all("<KeyPress>",analyse)
        fen.after(1,DefinirToucheRdroite)
    else:
        toucheRdroite=t
        print(toucheRdroite,t)
        t=""
        fen.unbind_all("<KeyPress>")
def Definirtouchebj2():
    global t3,touchebj2
    if t3=="":
        fen.bind_all("<KeyPress>",analyse2)
        fen.after(1,Definirtouchebj2)
    else:
        touchebj2=t3
        print(touchebj2,t3)
        t3=""
        fen.unbind_all("<KeyPress>")
def Definirtouchegj2():
    global t3,touchegj2
    if t3=="":
        fen.bind_all("<KeyPress>",analyse2)
        fen.after(1,Definirtouchegj2)
    else:
        touchegj2=t3
        print(touchegj2,t3)
        t3=""
        fen.unbind_all("<KeyPress>")
def Definirtouchedj2():
    global t3,touchedj2
    if t3=="":
        fen.bind_all("<KeyPress>",analyse2)
        fen.after(1,Definirtouchedj2)
    else:
        touchedj2=t3
        print(touchedj2,t3)
        t3=""
        fen.unbind_all("<KeyPress>")
def DefinirtoucheRdj2():
    global t3,touchehj2
    if t3=="":
        fen.bind_all("<KeyPress>",analyse2)
        fen.after(1,DefinirtoucheRdj2)
    else:
        touchehj2=t3
        print(touchehj2,t3)
        t3=""
        fen.unbind_all("<KeyPress>")
def DefinirtoucheRgj2():
    global t3,touchehj2
    if t3=="":
        fen.bind_all("<KeyPress>",analyse2)
        fen.after(1,DefinirtoucheRgj2)
    else:
        touchehj2=t3
        print(touchehj2,t3)
        t3=""
        fen.unbind_all("<KeyPress>")
def DefinirTouchePU2():
    global t3,toucheaj2
    if t3=="":
        fen.bind_all("<KeyPress>",analyse2)
        fen.after(1,DefinirTouchePU2)
    else:
        toucheaj2=t3
        print(toucheaj2,t3)
        t3=""
        fen.unbind_all("<KeyPress>")
def DefinirTouchePU():
    global t,toucheaide
    if t=="":
        fen.bind_all("<KeyPress>",analyse)
        fen.after(1,DefinirTouchePU)
    else:
        toucheaide=t
        print(toucheaide,t)
        t=""
        fen.unbind_all("<KeyPress>")




def startoption(event):
    global a,C,stop
    if a==1:
        if event.x>=19 and event.x<=71:
            if event.y>=530 and event.y<=586:
                C.delete(ALL)
                C.create_image(0,0,anchor=NW,image=Menu)
                a=0
        if event.x>=131 and event.x<=374 and event.y>=81 and event.y<=121:
            fen.unbind("<Button-1>")
            C.delete(ALL)
            BOUYAc.TetrisBase(fen,touchebas,touchedroite,touchegauche,toucheRdroite,toucheRgauche)
        if event.x>=180 and event.x<=320 and event.y>=240 and event.y<=275:
            fen.unbind("<Button-1>")
            TetrisVersus.TetrisVersus(fen,touchebj2,touchedj2,touchegj2,toucheRdj2,toucheaj2,toucheRgj2,touchebas,touchedroite,touchegauche,toucheRdroite,toucheaide,toucheRgauche,piecedujoueuriR1,piecedujoueurjR1,piecedujoueuriR2,piecedujoueurjR2,piecedujoueuriR3,piecedujoueurjR3,piecedujoueuriR4,piecedujoueurjR4,couleurjoueur,nbcolonne,nbcolonne2)
        if event.x>=105 and event.x<=400:
            if event.y>=490 and event.y<=520:
                C.delete(ALL)
                C.configure(width=732,height=602)
                stop=1
                Editor()
        if event.x>=127 and event.x<=376 and event.y>=335 and event.y<=378:
            fen.unbind("<Button-1>")
            C.delete(ALL)
            HARDCORE.TetrisHard(fen,touchebas,touchedroite,touchegauche,toucheRdroite,toucheRgauche,nbcolonne)
    if a==3:
        if event.x>=170 and event.x<=330 and event.y>=230 and event.y<=255:
            DefinirToucheBas()
        if event.x>=100 and event.x<=385 and event.y>=330 and event.y<=355:
            DefinirToucheRdroite()
        if event.x>=190 and event.x<=310 and event.y>=55 and event.y<=80:
            DefinirToucheGauche()
        if event.x>=195 and event.x<=305 and event.y>=145 and event.y<=170:
            DefinirToucheDroite()
        if event.x>=165 and event.x<=340 and event.y>=520 and event.y<=545:
            DefinirTouchePU()
        if event.x>=105 and event.x<=400 and event.y>=425 and event.y<=445:
            DefinirToucheRgauche()
        if event.x>=19 and event.x<=71:
            if event.y>=530 and event.y<=586:
                C.delete(ALL)
                C.create_image(0,0,anchor=NW,image=Menu)
                a=0
    if a==4:
        if event.x>=170 and event.x<=330 and event.y>=230 and event.y<=255:
            Definirtouchebj2()
        if event.x>=100 and event.x<=385 and event.y>=330 and event.y<=355:
            DefinirtoucheRdj2()
        if event.x>=190 and event.x<=310 and event.y>=55 and event.y<=80:
            Definirtouchegj2()
        if event.x>=195 and event.x<=305 and event.y>=145 and event.y<=170:
            Definirtouchedj2()
        if event.x>=165 and event.x<=340 and event.y>=520 and event.y<=545:
            DefinirTouchePU2()
        if event.x>=105 and event.x<=400 and event.y>=425 and event.y<=445:
            DefinirtoucheRgj2()
        if event.x>=19 and event.x<=71:
            if event.y>=530 and event.y<=586:
                C.delete(ALL)
                C.create_image(0,0,anchor=NW,image=Menu)
                a=0
    if a==2:
        if event.x>=80 and event.y>=171 and event.x<=405 and event.y<=244:
            C.delete(ALL)
            C.create_image(0,0,anchor=NW,image=Option)
            a=3
        if event.x>=80 and event.y>=412 and event.x<=416 and event.y<=482:
            C.delete(ALL)
            C.create_image(0,0,anchor=NW,image=Option)
            a=3
        if event.x>=19 and event.x<=71:
            if event.y>=530 and event.y<=586:
                C.delete(ALL)
                C.create_image(0,0,anchor=NW,image=Menu)
                a=0
    if a==0:
        if event.x>=175 and event.x<=340:
            if event.y>=307 and event.y<=375:
                C.delete(ALL)
                C.create_image(0,0,anchor=NW,image=Modes)
                a=1
    if a==0:
        if event.x>=165 and event.x<=330:
            if event.y>=445 and event.y<=510:
                C.create_image(0,0,anchor=NW,image=J1J2)
                a=2


C.create_image(0,0,anchor=NW,image=Menu)
fen.bind("<Button-1>",startoption)
fen.mainloop()
pygame.mixer.music.pause()