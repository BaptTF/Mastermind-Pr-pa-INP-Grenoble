#!/usr/bin/env python3

import random
import common


def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global combinaisonPossible#même chose que ensemblePossible
    combinaisonPossible = set()
    for c1 in common.COLORS: #Construit toutes les solutions possible car elle sont toutes possible initialement
        for c2 in common.COLORS:
            for c3 in common.COLORS:
                for c4 in common.COLORS:
                    possiblilite = c1 + c2 + c3 + c4 #Construit une combinaison
                    combinaisonPossible.add(possiblilite) #L'ajoute à la liste 
    return


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). Cette version triviale n'utilise pas cette information, puisqu'
    elle joue au hasard.
    """
    global combinaisonPossible
    global combinaison_p #Permet d'avoir la combinaison précédente ainsi que l'évaluation précédente
    if evaluation_p != None:
        combinaisonPossible = common.maj_possibles(combinaisonPossible, combinaison_p, evaluation_p) #Met a jour l'ensemble possible de combinaison restante
    combinaison = random.sample(combinaisonPossible, 1)[0]#on prend au hasard une combinaison dans combianaisonpossible
    combinaison_p = combinaison #Garde la dernière solution donnée comme solution précédente
    return combinaison