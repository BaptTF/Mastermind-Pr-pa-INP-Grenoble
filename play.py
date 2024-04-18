#!/usr/bin/env python3

import common


def play(codemaker, codebreaker, quiet=False):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    Renvoie le nombre de coups joués pour trouver la solution
    """
    n_essais = 0
    codebreaker.init() #On initialise le codebreaker
    codemaker.init() #On initialise le codemaker
    ev = None
    if not quiet:
        print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        combinaison = codebreaker.codebreaker(ev) #On fait jouer le codebreaker avec la dernière évaluation
        ev = codemaker.codemaker(combinaison) #On fait jouer le codemaker avec la combinaison founie par codebreaker juste avant
        n_essais += 1
        if not quiet:
            print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
            return n_essais


if __name__ == '__main__':
# Faire jouer ensemble codemaker0.py et codebreaker0.py pour 1 partie :
    import codebreaker3
    import codemaker1
    for i in range(1):
        play(codemaker1, codebreaker3)
