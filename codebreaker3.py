#!/usr/bin/env python3

import random
import common  # N'utilisez pas la syntaxe "form random import XXX"


def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global combinaisonPossible
    combinaisonPossible = set() #Construit toutes les solutions possible car elle sont toutes possible initialement
    for c1 in common.COLORS:
        for c2 in common.COLORS:
            for c3 in common.COLORS:
                for c4 in common.COLORS:
                    possibilite = c1 + c2 + c3 + c4 #Construit une combinaison
                    combinaisonPossible.add(possibilite) #L'ajoute à la liste 
                    
    global touteCombinaisonPossible#Construit toutes les solutions possibles mais qui ne seront pas modifié contrairement à la l'ensemble au-dessus
    touteCombinaisonPossible = set()
    for c1 in common.COLORS:
        for c2 in common.COLORS:
            for c3 in common.COLORS:
                for c4 in common.COLORS:
                    possibilite = c1 + c2 + c3 + c4 #Construit une combinaison
                    touteCombinaisonPossible.add(possibilite) #L'ajoute à la liste 
    return


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). Cette version triviale n'utilise pas cette information, puisqu'
    elle joue au hasard.
    """
    global combinaisonPossible
    global combinaison_p  #Permet d'avoir la combinaison précédente ainsi que l'évaluation précédente
    if evaluation_p != None: #Si ce n'est pas le premier tour
        #Met a jour l'ensemble possible de combinaison restante
        combinaisonPossible = common.maj_possibles(combinaisonPossible, combinaison_p, evaluation_p)
        evaluation_possible = [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0)] #Ensemble des évaluations possible sauf (4,0) 
        #car inutile puisque le nombre de possibilité ouverte va toujours être = 1
        possibilite_minimum_ouverte = [] #Initialise la liste qui va contenir l'ensemble des combinaisons qui reduit le plus l'ensemble des possibilité restante
        for combinaison in touteCombinaisonPossible:
            nb_possibilite_par_evaluation = []
            for evaluationSolution in evaluation_possible: #Pour chaque évaluation on compte le nombre de possibilité restante
                nb = 0
                for possibilite in combinaisonPossible:
                    if common.evaluation(combinaison, possibilite) == evaluationSolution: # à chaque fois la comparaisons entre combinaison et possibilité donne la même chose que entre combibasion et solutions alors possibilité est "possiblement" la vrai solution et donc on compte cette possibilité
                        nb += 1
                nb_possibilite_par_evaluation.append(nb)
            possibilite_minimum_ouverte.append((combinaison, max(nb_possibilite_par_evaluation))) #On associe chaque combinaison au maximum des possibilité restante donnée pour chaque évaluation (on se place donc dans le pire cas là où le choix donnerai le plus grand nombre de possibilité restante)
        minimum = min(possibilite_minimum_ouverte, key=lambda x: x[1])[1] #Puis on cherche le minimum des maximum pour chaque évaluation (nos algorithme est de la forme minmax)
        tous_combinaison_minimum = [i for i, v in possibilite_minimum_ouverte if v == minimum] #Puis on récupére toutes les combinaisons qui sont = au minimum 
        combinaison = tous_combinaison_minimum[0] #Prend la première par défaut
        for combi in tous_combinaison_minimum: # Par contre si on en trouve une dans l'ensemble des combinaison encore possible
            if combi in combinaisonPossible:
                combinaison = combi      #On choisit celle là
                break
        combinaison_p = combinaison #Garde la dernière solution donnée comme solution précédente
    else:
        combinaison = "JVNG" #Si c'est le premier tour on choisit une combinaison dont on a déjà calculé quelle est la plus optimal avec toute les combinaisons possible
        combinaison_p = combinaison #Garde la dernière solution donnée comme solution précédente
    return combinaison