#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:09:57 2020

@author: sarah
"""
"""TP2 Developpement d'un pendu __ Premiere Version__ PROGRAMME PRINCIPAL
30/11/20 __ Le Corre Sarah"""

#IMPORTATION DES FONCTIONS
from fonctions import  fichierMots

from fonctions import  tirage

from fonctions import affichage

from fonctions import chance



def progPrinc():
    """Programme principal, lance une partie de pendu
    entrée: pas de paramètre
    sortie:  score du joueur"""
    
    print('Nouvelle partie')
    
    liste = fichierMots()        #appel de la fonction pour créer et trier la liste
    mot = tirage(liste)          #appel de la fonction pour tirer un mot au hasard dans la liste
    motCache = affichage(mot)    #appel de la fonction pour afficher le mot caché
    
    print(motCache)
    
    
    essaie = chance(mot, motCache, 8, [])   #appel de la fonction pour gérer le nombre de chance du joueur,
                                            # ainsi que l'affichage ou non des lettres entrées
   
    
    return essaie
    
    

Partie=progPrinc()

