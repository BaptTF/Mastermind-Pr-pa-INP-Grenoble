from pywebio.input import input, TEXT
from pywebio.output import put_text
from pywebio.output import put_html
from pywebio.output import clear

#!/usr/bin/env python3

import common

def play(codemaker, codebreaker, quiet=False):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    Renvoie le nombre de coups joués pour trouver la solution
    """
    clear()
    n_essais = 0
    codebreaker.init() #On initialise le codebreaker
    codemaker.init() #On initialise le codemaker
    ev = None
    html_of_colors = "<p> "
    for couleur in common.COLORS:
        html_of_colors += f"{couleur} : {common.conversion[couleur]} | " #crée le code html les différentes couleur avec leur charactère associé
    html_of_colors += " </p>"
    put_html(f'<p> Combinaisons de taille {common.LENGTH}, couleurs disponibles {html_of_colors}') #affiche le code html
    while True:
        combinaison = codebreaker.codebreaker(ev) #On fait jouer le codebreaker avec la dernière évaluation
        ev = codemaker.codemaker(combinaison) #On fait jouer le codemaker avec la combinaison founie par codebreaker juste avant
        n_essais += 1
        combinaison_img = ""   #Transforme la combinaison de charactère en image
        for letter in combinaison:
            combinaison_img += common.conversion[letter]
        #Afficher la combinaison proposée et en dessous l'évaluation avec bien placée représenté par une boule rouge et mal placée par une boule blanche
        put_html(f"<p>Essai {n_essais} : {combinaison_img} <p> </p><img src='https://upload.wikimedia.org/wikipedia/commons/3/3e/Ic%C3%B4ne_Boule_Rouge.png' alt='Boule Rouge' width='16' height='16'> {ev[0]} <img src='https://upload.wikimedia.org/wikipedia/commons/f/f2/Snooker_ball_white.png' alt='Boule Blanche' width='16' height='16'> {ev[1]}</p>")
        if ev[0] >= common.LENGTH:
            put_html(f"<p> Bravo ! Trouvé {combinaison_img} en {n_essais} essais </p>")  #affiche le code html
            return n_essais


if __name__ == '__main__':
    # Faire jouer ensemble codemaker0.py et codebreaker0.py pour 1 partie :
    import human_codebreaker
    import human_codemaker
    for i in range(1):
        play(human_codemaker, human_codebreaker)
