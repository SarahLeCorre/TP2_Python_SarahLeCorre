#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:41:45 2020

@author: sarah
"""


"""TP2 Developpement d'un pendu __ Deuxième Version__ PROGRAMME PRINCIPAL
30/11/20 __ Le Corre Sarah"""

#IMPORTATION DES FONCTIONS
from fonctions import  fichierMots

from fonctions import  tirage

from fonctions import affichage

from fonctions import chance

from fonctions import totalScore


def progPrinc2():
    """Fonction lançant une partie, qui comptabilise les points, 
    propose de rejouer, affiche le score de la partie et le meilleur score.
    entree: pas de paramètre
    sortie: progPrinc2() ou 'au revoir' """
    
    print('Nouvelle partie')
    
    liste = fichierMots()        #appel de la fonction pour créer et trier la liste
    mot = tirage(liste)          #appel de la fonction pour tirer un mot au hasard dans la liste
    motCache = affichage(mot)    #appel de la fonction pour afficher le mot caché
    
    print(motCache)
    
    
    partie = chance(mot, motCache, 8, [])   #appel de la fonction pour gérer le nombre de chance du joueur,
                                            # ainsi que l'affichage ou non des lettres entrées
   
    
    print("Votre score est de", partie , " points")
    
    meilleurScore = totalScore(str(partie))
    print(meilleurScore)
    
    rejouer= input('Voulez-vous rejouer ?') 
    
    if rejouer== 'oui' or rejouer== 'Oui' or rejouer=='OUI':
        partie=progPrinc2()
    
    else:
        print("Au revoir !")
    return partie
    

partie2=progPrinc2()

