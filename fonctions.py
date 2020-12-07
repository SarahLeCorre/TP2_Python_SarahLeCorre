# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""TP2 Developpement d'un pendu __ FONCTIONS A APPELER DANS LE PROGRAMME PRINCIPAL
30/11/20 __ Le Corre Sarah"""

#IMPORTATION DES BIBLIOTHÈQUES
import unicodedata

import random


def fichierMots():
    
    """fonction permettant d'ouvrir un fichier texte, de le transformer en liste
    et de trier cette liste par ordre alphabétique et par taille
    La fonction n'a pas de paramètre d'entrée et renvoie la liste des mots triée"""

    fich = open('repertoireMots.txt','r') #ouverture fichier txt
    repertoire = fich.read()    #lecture fichier
    repSansAccents =''.join((accent for accent in unicodedata.normalize('NFD',repertoire) if unicodedata.category(accent) != 'Mn')) #suppression des accents du fichier txt
    fich.close()    #fermeture fichier txt
        
    ListeMots = repSansAccents.split()  #séparation en liste
    L1=repSansAccents.split()
    
    for i,v in enumerate(L1):
        
        if len(v) < 5:
           ListeMots.remove(v) #Supprime le mot de la liste s'il fait moins de 5 lettres
           
        elif len(v) > 8:
            ListeMots.remove(v)  #Supprime le mot de la liste s'il fait plus de 8 lettres
          
        
    trieList = sorted(ListeMots, key=str.lower)   #trie de la liste
    
    return (trieList)




def tirage(liste):
    
    """fonction permettant le tirage aléatoire d'un élément d'une liste
    entree: liste
    sortie: mot aleatoire de la liste en minuscules'"""
    
    valRen = random.choice(liste)
    valRen= valRen.lower()
    return valRen




def affichage(mot): 
    """Fontion affichant la premiere lettre d'un mot,
    puis des underscores(_) pour les autres lettres (sauf pour les lettres identiques à la première)
    entree: mot écrit en toutes lettres
    sortie: mot caché par les underscores"""
    
    valRen=mot[0]
    L=mot[0]        #séparation du lot en deux listes
    L1=mot[1:]
    L2=[]
    
    for i,v in enumerate(L1):
        if len(str(L2))>=1:
            
            if v==L:    #changement des lettres en _ s'il y a des lettres identiques à la première dans le mot
                L2+=v
                L3="".join(L2)
                valRen=str(L)+L3
                
                
            else :      #hangement des lettres en _ s'il n'y a pas de lettre identique à la première
                L2+="_"
                L3="".join(L2)
                valRen=str(L)+L3 
        
        
    return valRen




    
def chance(mot,motCache,n,L):
    """Fonction laissant n chances au joueur pour deviner un mot et qui remplace les underscores par les lettres trouvées par le joueur
    entree: mot en toute lettres, mot caché par les underscores, nombre de chance laissé, liste vide
    sortie:0 score du joueur (8 points pour un sans fautes)"""
    
    lettre = input('Proposition de lettre:')
    
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
            
            score=n                             #Le joueur a trouvé le mot, on stop la fonction et on renvoie son score
           
        else:
            score=chance(mot, motCache, n, L)   # On réitère la fonction pour que le joueur entre une autre lettre. 
                                                # Le nombre le chance reste le même car le joueur a entré une lettre correcte
    
    else:
         
        if n!=1:
           
            print("La lettre n'est pas dans le mot, veuillez réessayer")
            L+=lettre
            score= chance(mot, motCache, n-1, L)        # Le joueur a fait une erreur, on réitère la fonction avec une chance en moins
    
            
        else:
            score=0
            print("Nombre de chance écoulé, vous avez perdu...", "Le mot était",mot)
                 
        
    return score



    
    
def totalScore(score):
    """Fonction regroupant tous les scores des parties jouées dans 
    un fichier txt et qui retourne le meilleur score
    entree: score de la partie 
    sortie: meilleur score de toutes les parties"""
    
    fichScore = open("totalScores.txt", "a")    # On ouvre un fichier en mode écriture sans écraser les données qu'il contient
    fichScore.write(score)                      # On inscrit le score de la partie qui vient de se terminer
    fichScore.write(" ")

    fichScore.close()
    fichScore = open('totalScores.txt','r') #ouverture fichier txt en mode lecture
    scores = fichScore.read()
    ListScores= scores.split()              # Séparation en liste
    meilleurScore= "Le meilleur score est de " + max(ListScores) +" points"     #On extrait la valeur maximale contenue dans la liste
    
    return meilleurScore
    
    
    
