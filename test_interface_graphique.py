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
    codebreaker.init()
    codemaker.init()
    ev = None
    html_of_colors = "<p> "
    for couleur in common.COLORS:
        html_of_colors += f"{couleur} : {common.conversion[couleur]} | "
    html_of_colors += " </p>"
    put_html(f'<p> Combinaisons de taille {common.LENGTH}, couleurs disponibles {html_of_colors}')
    while True:
        combinaison = codebreaker.codebreaker(ev)
        ev = codemaker.codemaker(combinaison)
        n_essais += 1
        combinaison_img = ""
        for letter in combinaison:
            combinaison_img += common.conversion[letter]
        put_html(f"<p>Essai {n_essais} : {combinaison_img} <p> </p><img src='https://upload.wikimedia.org/wikipedia/commons/3/3e/Ic%C3%B4ne_Boule_Rouge.png' alt='Boule Rouge' width='16' height='16'> {ev[0]} <img src='https://upload.wikimedia.org/wikipedia/commons/f/f2/Snooker_ball_white.png' alt='Boule Blanche' width='16' height='16'> {ev[1]}</p>")
        if ev[0] >= common.LENGTH:
            put_html(f"<p> Bravo ! Trouvé {combinaison_img} en {n_essais} essais </p>")
            return n_essais


if __name__ == '__main__':
    # Les lignes suivantes sont à modifier / supprimer selon ce qu'on veut faire, quelques exemples :
    # Faire jouer ensemble codemaker0.py et codebreaker0.py pour 5 parties :
    import human_codebreaker
    import human_codemaker
    for i in range(1):
        play(human_codemaker, human_codebreaker)

    #  Faire jouer un humain contre codemaker0.py :
    #import codemaker0
    #import human_codebreaker
    #play(codemaker0, human_codebreaker)

    # Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
    #import codebreaker2
    #import codemaker2
    #play(codemaker2, codebreaker2)

    # Ou encore :
    #import codebreaker1
    #import human_codemaker
    #play(human_codemaker, codebreaker1)
