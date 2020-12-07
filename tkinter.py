#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:58:16 2020

@author: sarah
"""

"""TP2 Developpement d'un pendu __ TROISIEME Version__ PROGRAMME PRINCIPAL__ TKINTER
07/12/20 __ Le Corre Sarah__ lien git : https://github.com/SarahLeCorre/TP2_Python_SarahLeCorre.git """

#IMPORTATION DES BIBLIOTHEQUES

from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, StringVar

# IMPORTATION DES FONCTIONS

from fctTkinter import lancer
from fonctions import affichage



#Création de mon espace graphique


fenetre= Tk()                           #création fenetre      
fenetre.title('Jeu du pendu')
fenetre.geometry('1500x800+250+150')    #taille de ma fenetre
fenetre['bg'] = '#ACF1E7'               #couleur fond fenetre



#Création Strinvar()

mot = StringVar()
motCache = StringVar()
LA = StringVar()
valuee = StringVar() 

#création zone de saisie 

saisi = Entry(fenetre,textvariable=valuee, width = 30)
saisi.pack(side = 'left',padx=100 )


# Mes Bouttons 

buttonLettre= Button(fenetre, text = 'Proposer', fg ='#0C9BD2',relief = 'groove', command = lambda :chance(mot, motCache,8,LA))
buttonLettre.pack(side ='left' )

buttonStart= Button(fenetre, text = 'Nouvelle partie', font='Helvetica', relief = 'groove')

buttonQuitt = Button(fenetre, text="QUITTER", fg = '#0C9BD2',relief = 'groove',font='Helvetica',command = fenetre.destroy)
buttonQuitt.pack(side ='bottom', padx = 20, pady = 60)


# Mes fonctions


def enregistrerProposition():
    """Fonction qui stock la lettre rentrée par l'utillisateur dans la barre de saisie
    entrée : pas de paramètre
    sortie : Lettre donnée par le joueur"""
    
    Lettre= valuee.get()    #récupère la valeur dans la barre de saisie
    valuee.set("")  #efface les valeurs dans barre de saisie
    print(Lettre)
    return Lettre





def fermer(n):
    """fonction qui ferme l'image affichée dans le canevas et qui en affiche une autre
    entrée : numéro de l'image
    sortie : affichage de la nouvelle image    """
    
    ListImage=['bonhomme1.gif', 'bonhomme2.gif', 'bonhomme3.gif', 'bonhomme4.gif', 'bonhomme5.gif','bonhomme6.gif','bonhomme7.gif','bonhomme8.gif']

    global imPendu
    canevas.delete('all')   #suppression de l'ancienne image
    imPendu=PhotoImage(file = ListImage[n-1])   #choix de l'image dans la liste
    
    item = canevas.create_image(0,0, anchor= "nw", image = imPendu)
    print("Image de fond(item",item,")")




def chance(mot,motCache,n,LA):
    """Fonction laissant n chances au joueur pour deviner un mot, remplace les underscores par les lettres trouvées par le joueur
    entree: mot en toute lettres, mot caché par les underscores, nombre de chance laissé, StringVar() affichée dans un label
    sortie:score du joueur"""
    
    Lettre= valuee.get()    #obtention de la lettre tapée dans la barre de saisie
    valuee.set("")          #effacement de la barre de saisie
    
    score=n
    L=[] 
    
    for i,v in enumerate(L):
        if v==Lettre:
            
            LA.set("Lettre déjà affichée")  #changement du texte dans le label LA
    
    
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
            score= 0
       
    
    else:
         
        if n!=1:
            LA.set("La lettre n'est pas dans le mot, veuillez réessayer")
            L+=Lettre
            
            ListImage=['bonhomme8.gif', 'bonhomme7.gif', 'bonhomme6.gif', 'bonhomme5.gif', 'bonhomme4.gif','bonhomme3.gif','bonhomme2.gif','bonhomme1.gif']
            
            global imPendu
            canevas.delete('all')
            imPendu=PhotoImage(file = ListImage[n-1])
    
            item = canevas.create_image(0,0, anchor= "nw", image = imPendu)
            print("Image de fond(item",item,")")
            
            score= n-1
            
        else:
            score=0
            LA.set("Nombre de chance écoulé, vous avez perdu... Le mot était",mot)
                 
        
    return score






# Mes Labels

labelTitre = Label(fenetre, text = "Nombre de chances restantes", fg = '#0C9BD2')
labelTitre.pack(side = 'bottom', padx=20, pady= 10)

LabelLeAff = Label(fenetre, textvariable = LA)
LabelLeAff.pack(side = 'top', padx = 10, pady = 20)


mot = lancer()      #tirage aléatoire du mot
motCache.set(affichage(mot))    #afffichage du mot avec les underscores
print( motCache)
labelMot =Label(fenetre, textvariable= motCache)
labelMot.pack(side= 'right', padx= 100, pady= 5) #affichage du mot à deviner


# Affichage de l'image du pendu dans un canevas

imPendu=PhotoImage(file = 'bonhomme1.gif')
canevas = Canvas(fenetre, width = 300, height = 300)
item = canevas.create_image(0,0, anchor= "nw", image = imPendu) #creation de l'image
print("Image de fond(item",item,")")
canevas.pack(side = 'right', padx = 100)






fenetre.mainloop()

