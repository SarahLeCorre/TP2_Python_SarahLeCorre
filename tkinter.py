#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:58:16 2020

@author: sarah
"""

"""TP2 Developpement d'un pendu __ TROISIEME Version__ PROGRAMME PRINCIPAL__ TKINTER
07/12/20 __ Le Corre Sarah"""

#IMPORTATION DES BIBLIOTHEQUES

from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, StringVar

# IMPORTATION DES FONCTIONS

#from fctTKINTER import chance

from fctTKINTER import lancer

from fonctions import fichierMots

from fonctions import tirage

from fonctions import affichage


#Création de mon espace graphique
#création fenetre

fenetre= Tk()                  
fenetre.title('Jeu du pendu')
fenetre.geometry('1500x800+250+150')    #taille de ma fenetre
fenetre['bg'] = '#ACF1E7'               #couleur fond fenetre



#Zone de saisie de texte
valuee = StringVar() 
saisi = Entry(fenetre,textvariable=valuee, width = 30)
saisi.pack(side = 'left',padx=100 )


buttonLettre= Button(fenetre, text = 'Proposer', fg ='#0C9BD2',relief = 'groove', command = lambda :chance(mot, motCache,8,LA))
buttonLettre.pack(side ='left' )

mot = StringVar()
motCache = StringVar()
LA = StringVar()
LA =""


# Mes fonctions


def enregistrerProposition():
    """stock la lettre rentrée par l'utillisateur dans la barre de saisi"""
    
    Lettre= valuee.get()
    valuee.set("")
    print(Lettre)
    return Lettre





def fermer(n):
    """ferme l'image en cours et en affiche une autre"""
    
    ListImage=['bonhomme1.gif', 'bonhomme2.gif', 'bonhomme3.gif', 'bonhomme4.gif', 'bonhomme5.gif','bonhomme6.gif','bonhomme7.gif','bonhomme8.gif']

    global imPendu
    canevas.delete('all')
    imPendu=PhotoImage(file = ListImage[n])
    
    item = canevas.create_image(0,0, anchor= "nw", image = imPendu)
    print("Image de fond(item",item,")")




def chance(mot,motCache,n,LA):
    """Fonction laissant n chances au joueur pour deviner un mot, remplace les underscores par les lettres trouvées par le joueur
    entree: mot en toute lettres, mot caché par les underscores, nombre de chance laissé
    sortie:0 si défaite et 1 si victoire"""
    
    Lettre= valuee.get()
    valuee.set("")
    
    score=n
    L=[] 
    
    for i,v in enumerate(L):
        if v==Lettre:
            
            LA.set("Lettre déjà affichée")
    
    
    if Lettre in mot:
        L+=Lettre
        print('Correct')
        for i,v in enumerate(mot):
            if v == Lettre:
                if i !=0 and i!=len(mot)-1:
                    motCache = (motCache[0:i] +Lettre+ motCache[i+1:] )
                elif i==len(mot)-1:
                    motCache = (motCache[0:i] + Lettre)
          
        motCache.set(motCache)    
        
        if mot == motCache:
            
            score=n
            
        else:
            score=chance(mot, motCache, n, LA)
       
    
    else:
         
        if n!=1:
            LA.set("La lettre n'est pas dans le mot, veuillez réessayer")
            L+=Lettre
            
            ListImage=['bonhomme1.gif', 'bonhomme2.gif', 'bonhomme3.gif', 'bonhomme4.gif', 'bonhomme5.gif','bonhomme6.gif','bonhomme7.gif','bonhomme8.gif']
            global imPendu
            canevas.delete('all')
            imPendu=PhotoImage(file = ListImage[n])
    
            item = canevas.create_image(0,0, anchor= "nw", image = imPendu)
            print("Image de fond(item",item,")")
            
            score= chance(mot, motCache, n-1, LA)
            
        else:
            score=0
            LA.set("Nombre de chance écoulé, vous avez perdu... Le mot était",mot)
                 
        
    return score

# Mes Bouttons 

buttonStart= Button(fenetre, text = 'Nouvelle partie', font='Helvetica', relief = 'groove')

buttonQuitt = Button(fenetre, text="QUITTER", fg = '#0C9BD2',relief = 'groove',font='Helvetica',command = fenetre.destroy)
buttonQuitt.pack(side ='bottom', padx = 20, pady = 60)




# Mes Labels

labelTitre = Label(fenetre, text = "Nombre de chances restantes", fg = '#0C9BD2')
labelTitre.pack(side = 'bottom', padx=20, pady= 10)

LabelLeAff = Label(fenetre, text = LA)
LabelLeAff.pack(side = 'right', padx = 10)


mot = lancer()
motCache1= affichage(mot)
print( motCache1)
labelMot =Label(fenetre, text= motCache1)
labelMot.pack(side= 'right', padx= 100, pady= 5) #affichage du mot à deviner


# Affichage de l'image du pendu dans un canevas

imPendu=PhotoImage(file = 'bonhomme1.gif')
canevas = Canvas(fenetre, width = 300, height = 300)
item = canevas.create_image(0,0, anchor= "nw", image = imPendu)
print("Image de fond(item",item,")")
canevas.pack(side = 'right', padx = 100)






fenetre.mainloop()

