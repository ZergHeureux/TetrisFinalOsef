import BOUYAc
import TetrisVersus
from tkinter import*
import pygame
pygame.init()
##BOUYA.TetrisBase()
t=""
t2=""
t3=""
type2touche=""
touchegauche="Left"
touchedroite="Right"
touchebas="Down"
touchehaut="Up"
toucheaide="Return"
touchegj2="q"
touchedj2="d"
touchebj2="s"
touchehj2="z"
toucheaj2="a"
def Reglage(arg1):

    def analyse(event):
        global t,type2touche,t2
        t=event.keysym
        t2=event.char
        type2touche=t2
        print(touchebas,touchedroite,touchegauche,touchehaut)
    def analyse2(event):
        global t3,type2touche,t2
        t3=event.keysym
        t2=event.char
        type2touche=t2
        print(touchebj2,touchedj2,touchegj2,touchehj2)
    def DefinirToucheBas():
        global t,touchebas
        if t=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse)
            arg1.after(1,DefinirToucheBas)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchebas=t
            print(touchebas,t)
            t=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def DefinirToucheGauche():
        global t,touchegauche
        if t=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse)
            arg1.after(1,DefinirToucheGauche)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchegauche=t
            print(touchegauche,t)
            t=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def DefinirToucheDroite():
        global t,touchedroite
        if t=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse)
            arg1.after(1,DefinirToucheDroite)
        else:

            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchedroite=t
            print(touchedroite,t)
            t=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def DefinirToucheHaut():
        global t,touchehaut
        if t=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse)
            arg1.after(1,DefinirToucheHaut)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchehaut=t
            print(touchehaut,t)
            t=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def Definirtouchebj2():
        global t3,touchebj2
        if t3=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse2)
            arg1.after(1,Definirtouchebj2)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchebj2=t3
            print(touchebj2,t3)
            t3=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def Definirtouchegj2():
        global t3,touchegj2
        if t3=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse2)
            arg1.after(1,Definirtouchegj2)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchegj2=t3
            print(touchegj2,t3)
            t3=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def Definirtouchedj2():
        global t3,touchedj2
        if t3=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse2)
            arg1.after(1,Definirtouchedj2)
        else:

            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchedj2=t3
            print(touchedj2,t3)
            t3=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def Definirtouchehj2():
        global t3,touchehj2
        if t3=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse2)
            arg1.after(1,Definirtouchehj2)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            touchehj2=t3
            print(touchehj2,t3)
            t3=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def DefinirTouchePU2():
        global t3,toucheaj2
        if t3=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse2)
            arg1.after(1,DefinirTouchePU2)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            toucheaj2=t3
            print(toucheaj2,t3)
            t3=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def DefinirTouchePU():
        global t,toucheaide
        if t=="":
            L1.grid_forget()
            L.grid(row=3,column=4,columnspan=5)
            arg1.bind_all("<KeyPress>",analyse)
            arg1.after(1,DefinirTouchePU)
        else:
            L1.grid(row=1,column=3,columnspan=2)
            L1.config(text=type2touche)
            toucheaide=t
            print(toucheaide,t)
            t=""
            L.grid_forget()
            arg1.unbind_all("<KeyPress>")
    def Quitter():
        menu(fenetre)
        BoutonBas.grid_forget()
        BoutonDroite.grid_forget()
        BoutonGauche.grid_forget()
        BoutonHaut.grid_forget()
        BoutonQuitter.grid_forget()
        L.grid_forget()
        L1.grid_forget()
        BoutonBas2.grid_forget()
        BoutonDroite2.grid_forget()
        BoutonGauche2.grid_forget()
        BoutonHaut2.grid_forget()
        BoutonPU.grid_forget()
        BoutonPU2.grid_forget()
        C.grid_forget()
    arg1.geometry("800x500")
    arg1.title("Réglage")
    B1.grid_forget()
    Cmenu.grid_forget()
    B2.grid_forget()
    B3.grid_forget()
    L2.grid_forget()
    C=Canvas(arg1,width=800,height=500,bg="white")
    C.grid(columnspan=12,rowspan=10)
    L=Label(arg1,bg="white",text="Appuyer sur une touche",font="Helvetica")
    L1=Label(arg1,bg="white",text=type2touche)
    BoutonBas=Button(arg1,width=10,height=1,text="bas J1",command=DefinirToucheBas)
    BoutonBas.grid(column=0,row=0)
    BoutonGauche=Button(arg1,width=10,height=1,text="gauche J1",command=DefinirToucheGauche)
    BoutonGauche.grid(column=1,row=0)
    BoutonDroite=Button(arg1,width=10,height=1,text="droite J1",command=DefinirToucheDroite)
    BoutonDroite.grid(column=2,row=0)
    BoutonHaut=Button(arg1,width=10,height=1,text="ChangePiece J1",command=DefinirToucheHaut)
    BoutonHaut.grid(column=3,row=0)
    BoutonPU=Button(arg1,width=10,height=1,text="PowerUp J1",command=DefinirTouchePU)
    BoutonPU.grid(column=4,row=0)
    BoutonBas2=Button(arg1,width=10,height=1,text="bas J2",command=Definirtouchebj2)
    BoutonBas2.grid(column=0,row=1)
    BoutonGauche2=Button(arg1,width=10,height=1,text="gauche J2",command=Definirtouchegj2)
    BoutonGauche2.grid(column=1,row=1)
    BoutonDroite2=Button(arg1,width=10,height=1,text="droite J2",command=Definirtouchedj2)
    BoutonDroite2.grid(column=2,row=1)
    BoutonHaut2=Button(arg1,width=10,height=1,text="ChangePiece J2",command=Definirtouchehj2)
    BoutonHaut2.grid(column=3,row=1)
    BoutonPU2=Button(arg1,width=10,height=1,text="PowerUp J2",command=DefinirTouchePU2)
    BoutonPU2.grid(column=4,row=1)
    BoutonQuitter=Button(arg1,width=10,height=1,text="Quitter",command=Quitter)
    BoutonQuitter.grid(row=2,column=0)
def menu(arg1):
    global B1,B2,Cmenu,L2,B3
    def lancerTB():
        arg1.unbind(ALL)
        BOUYAc.TetrisBase(fenetre,touchebas,touchedroite,touchegauche,touchehaut)
    def lancerR():
        Reglage(arg1)
    def lancerTV():
        TetrisVersus.TetrisVersus(fenetre,touchebas,touchedroite,touchegauche,touchehaut,toucheaide,touchebj2,touchedj2,touchegj2,touchehj2,toucheaj2)
    arg1.geometry("700x600")
    Cmenu=Canvas(arg1,bg="white",width=700,height=600)
    Cmenu.grid(rowspan=200,columnspan=200,row=0,column=0)
    B1=Button(arg1,text="Tetris de base", command=lancerTB,width=15,height=2)
    B1.grid(row=0,column=0)
    B2=Button(arg1,text="Réglage", command=lancerR,width=15,height=2)
    B2.grid(row=1,column=0)
    B3=Button(arg1,text="TetrisVersus",command=lancerTV,width=15,height=2)
    B3.grid(row=2,column=0)
    L2=Label(arg1,bg="white",text="Veuillez définir vos touches dans -Réglage")
    L2.grid(row=3,column=0,columnspan=10)
    print(touchebas,touchedroite,touchegauche,touchehaut)

fenetre=Tk()
menu(fenetre)
fenetre.mainloop()
pygame.mixer.music.pause()