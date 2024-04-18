#!/usr/bin/env python3

import random
import common  # N'utilisez pas la syntaxe "form random import XXX"


def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global dejaVue # liste qui stock les combinaisons déja testées/comparées pour ne pas recommencer l'action une deuxième fois
    dejaVue = []# à chaque nouvelle partie on remet à zéro la liste des combinaisons déja vues.
    return


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). Cette version triviale n'utilise pas cette information, puisqu'
    elle joue au hasard.
    """
    global dejaVue # appel la liste dejaVue
    combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH)) # prends au hasard une combinaison parmis toutes celles qui existent
    while combinaison in dejaVue: # tant que la combinasion choisie au hasard est déja dans la lsite dejaVue...
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))# ...on en prend une autre jusqu'a tomber sur une combinaison qui n'est pas dans dejaVue
    dejaVue.append(combinaison)# enfin on ajoute cette combinaison a dejaVue pour ne pas la retester par la suite
    return combinaison
