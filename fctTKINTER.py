#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:36:20 2020

@author: sarah
"""

"""TP2 Developpement d'un pendu __ FONCTIONS A APPELER DANS LE PROGRAMME TKINTER
30/11/20 __ Le Corre Sarah"""
#rom tkinter import enregistrerProposition

#IMPORTATION DES BIBLIOTHÈQUES
#import unicodedata
#import random

#IMPORTATION DES FONCTIONS
from fonctions import  fichierMots

from fonctions import  tirage



#labelMot =Label(fenetre, text= motCache)
#labelMot.pack(side= 'right', padx= 200, pady= 5) #affichage du mot à deviner


def chance(mot,motCache,n,L,lettre):
    """Fonction laissant n chances au joueur pour deviner un mot, remplace les underscores par les lettres trouvées par le joueur
    entree: mot en toute lettres, mot caché par les underscores, nombre de chance laissé
    sortie:0 si défaite et 1 si victoire"""
    
   # lettre =  enregistrerProposition() 
    
    score=n
    
    
    for i,v in enumerate(L):
        if v==lettre:
            
            print("Lettre déjà rentrée")
    
    
    if lettre in mot:
        L+=lettre
        print('Correct')
        for i,v in enumerate(mot):
            if v == lettre:
                if i !=0 and i!=len(mot)-1:
                    motCache = (motCache[0:i] +lettre+ motCache[i+1:] )
                elif i==len(mot)-1:
                    motCache = (motCache[0:i] + lettre)
                    
        print(motCache)
        
        if mot == motCache:
            
            score=n
            
        else:
            score=chance(mot, motCache, n, L, lettre)
       
    
    else:
         
        if n!=1:
           
            print("La lettre n'est pas dans le mot, veuillez réessayer")
            L+=lettre
            
            score= chance(mot, motCache, n-1, L, lettre)
            
        else:
            score=0
            print("Nombre de chance écoulé, vous avez perdu...", "Le mot était",mot)
                 
        
    return score



def lancer():
    liste = fichierMots() #appel de la fonction pour créer et trier la liste
    mot = tirage(liste)   #appel de la fonction pour tirer un mot au hasard dans la liste
    
    return mot
