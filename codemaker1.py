#!/usr/bin/env python3

import sys
import random
import common  # N'utilisez pas la syntaxe "from common import XXX"


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))#solution chosit par le codemaker est une combinaison au hasard du jeu


def codemaker(combinaison):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    
    if len(combinaison) != len(solution): # check si c'est bien de la même taille entre la proposition du joueur et la solution
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
        
    return common.evaluation(combinaison, solution) # retourne l'évaluation entre la proposition et la solution choisie