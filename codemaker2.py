#!/usr/bin/env python3
import codebreaker2
import sys
import random
import common  # N'utilisez pas la syntaxe "from common import XXX"


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    #Choisit une solution au hasard initialement pas forcement une solution qui le plus grand ensemble de solution encore possible maximal
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH)) 
    global combinaisonPossible
    combinaisonPossible = set()
    for c1 in common.COLORS: #Construit toutes les solutions possible car elle sont toutes possible initialement
        for c2 in common.COLORS:
            for c3 in common.COLORS:
                for c4 in common.COLORS:
                    possiblilite = c1 + c2 + c3 + c4 #Construit une combinaison
                    combinaisonPossible.add(possiblilite) #L'ajoute à la liste 


def codemaker(combinaison):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    global combinaisonPossible 
    #Met a jour l'ensemble des combinaisons encore possible avec le tuple de l'évaluation associée
    combinaisonPossible = common.maj_possibles(combinaisonPossible, combinaison, solution)
    nb_possibilite_max = 0 #Initialise le nombre maximal de possibilité
    for sol_possible in combinaisonPossible:
        #Donne le nombre de combinaison/possibilité restante si cette solution est choisie
        nb_possibilite = len(combinaisonPossible.intersection(common.donner_possibles(combinaison, common.evaluation(combinaison, sol_possible))))
        if nb_possibilite >= nb_possibilite_max: #Cherche le maximum de combinaison restante en comparant le précédant max
            nb_possibilite_max = nb_possibilite #Si le précédent max est inférieur prendre le nouveau
            solution = sol_possible 
    if len(combinaison) != len(solution): 
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
        
    return common.evaluation(combinaison, solution) #Renvoie l'évalution associée à la solution ayant le plus de combinaison encore possible