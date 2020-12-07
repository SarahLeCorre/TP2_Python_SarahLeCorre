#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:36:20 2020

@author: sarah
"""

"""TP2 Developpement d'un pendu __ FONCTIONS A APPELER DANS LE PROGRAMME TKINTER
30/11/20 __ Le Corre Sarah___ lien git : https://github.com/SarahLeCorre/TP2_Python_SarahLeCorre.git"""


#IMPORTATION DES FONCTIONS
from fonctions import  fichierMots

from fonctions import  tirage




def lancer():
    """Lancement du jeu, la fonction tire un mot au sort
    entrée : pas de paramètres
    sortie: mot choisit"""
    
    liste = fichierMots() #appel de la fonction pour créer et trier la liste
    mot = tirage(liste)   #appel de la fonction pour tirer un mot au hasard dans la liste
    
    return mot
