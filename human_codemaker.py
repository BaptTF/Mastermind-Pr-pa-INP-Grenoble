#!/usr/bin/env python3
from pywebio.input import input, NUMBER
from pywebio.output import put_html
import common

def init():
    return

def valid_bien_place(bp): #Fonction qui vérifie que le nombre rentrée est correcte
    if bp < 0 or bp > common.LENGTH:
        return "valeur invalide (< 0 ou > {})".format(common.LENGTH)
    
def codemaker(combinaison):
    combinaison_img = ""
    for letter in combinaison: #Transforme les charactères en image pour les affichers
        combinaison_img += common.conversion[letter]
    put_html(f'Combinaison proposée: {combinaison_img}') #affiche la combinaison proposée
    bp = input('Saisir nombre de plots bien placés: ',type=NUMBER, validate=valid_bien_place) #Demande le nombre de plot bien placé
    mp = input('Saisir nombre de plots mal placés: ',type=NUMBER, validate=valid_bien_place) #Demande le nombre de plot bien mal placé
    return bp,mp
 
