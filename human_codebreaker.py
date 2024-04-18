#!/usr/bin/env python3
from pywebio.input import input, TEXT
import common


def init():
    return

def valid(combinaison): #Fonction qui renvoie l'erreur de la raison pour laquelle la combinaison n'est pas acceptée
    if len(combinaison) != common.LENGTH:
        return "Combinaison invalide (longueur {} au lieu de {})".format(len(combinaison), common.LENGTH)
    for c in combinaison:
        if c not in common.COLORS:
            return "Combinaison invalide (couleur {} n'existe pas)".format(c)

def codebreaker(__):  # Inutile d'affiche la correction reçue, la boucle principale de jeu s'en charge
    combinaison = input("Saisir la combinaison : ", validate=valid, type=TEXT)  # On lit une combinaison au clavier au lieu d'appeler le codebreaker (qui sera donc joué par un humain)
    return combinaison 

