#!/usr/bin/env python3

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

boule_rouge = "<img src='https://webgamesonline.com/mastermind/images/color_1.gif' alt='Boule Rouge' width='16' height='16'>"
boule_vert = "<img src='https://webgamesonline.com/mastermind/images/color_2.gif' alt='Boule Verte' width='16' height='16'>"
boule_bleu = "<img src='https://webgamesonline.com/mastermind/images/color_3.gif' alt='Boule Bleue' width='16' height='16'>"
boule_jaune = "<img src='https://webgamesonline.com/mastermind/images/color_4.gif' alt='Boule Jaune' width='16' height='16'>"
boule_marron = "<img src='https://webgamesonline.com/mastermind/images/color_5.gif' alt='Boule Marron' width='16' height='16'>"
boule_orange = "<img src='https://webgamesonline.com/mastermind/images/color_6.gif' alt='Boule Orange' width='16' height='16'>"
boule_noir = "<img src='https://webgamesonline.com/mastermind/images/color_7.gif' alt='Boule Noire' width='16' height='16'>"
boule_blanche = "<img src='https://webgamesonline.com/mastermind/images/color_8.gif' alt='Boule Blanche' width='16' height='16'>"

conversion = {'R':boule_rouge, 'V':boule_vert, 'B':boule_bleu, 'J':boule_jaune, 'N':boule_noir, 'M':boule_marron, 'O':boule_orange, 'G':boule_blanche}
# L'INTERFACE GRAPHIQUE NE MARCHE SEULEMENT SI LES COULEURS CHOISIE SONT CELLE PAR DEFAUT
# pour le reste le programme continue de fonctionner si on change les valeurs par défaut ci-dessus

def evaluation(comb, ref):#fonction qui compare la combinaison proposée et la vrai choisie par codemaker
    bienPlace, malPlace = 0,0 #initialise compteur de "pion(s)" mal placés et bien placés
    CouleurMalPlace = []
    for i in range(len(comb)):
        if comb[i] == ref[i]:# si même couleur à la même place...
            bienPlace += 1#... on compte un pion bien placé
            comb = comb.replace(comb[i],"0",1)#utile pour ne pas compter deux fois une couleur et dans la bien placé et dans malplacé
        else:
            CouleurMalPlace.append(ref[i]) # on met dans la liste les couleurs qui restent dans la réf mais que le joueur n'a pas mis au bon endroit
    for i in range(len(comb)):
        if comb[i] in CouleurMalPlace:# si on avait bien mis une bonne couleur mais  que cette couleur avait été chosie pour un autre emplacement.... 
            malPlace += 1 #on dit qu'elle est mal placée et on l'ajoute au compteur des malplacés
            CouleurMalPlace.remove(comb[i])# on retire cette couleur de coueleurmalplace pour eviter de competer deux fois la même chose si la couleur est présente à deux reprises par exemple
    
    return bienPlace, malPlace # on retourne le nombre de couleurs bien placé et malplacé


def donner_possibles(combinaison, evaluationSolution): # en entrée on a une combinaison, et le résulat de la comparaion entre cette combinasion et la solution
    ensemblePossible = set()# initialise ensemblepossible
    for c1 in COLORS:
        for c2 in COLORS:
            for c3 in COLORS:
                for c4 in COLORS:# les 4 lignes signifient : pour toutes les combinasions possibles
                    possibilite = c1 + c2 + c3 + c4 # possibilité devient successivement toute les combinaisons possibles du jeux
                    if evaluation(combinaison, possibilite) == evaluationSolution:# à chaque fois la comparaisons entre combinaison et possibilité donne la même chose que entre combibasion et solutions alors possibilité est "possiblement" la vrai solution et donc on conserve cette possibilité
                         ensemblePossible.add(possibilite)# on concerve possibilité car elle a une chance d'être solution (et bien sur on écarte les combinasions qui ne donne pas la même évaluation que avec solution)
    return ensemblePossible # à la fin on ne garde un ensemble de possibilité qui ont une chance d'être solution

def maj_possibles(possible, combinaison, evaluationSolution): # quand on doit faire successivement des ensemble possibles
    possible = possible.intersection(donner_possibles(combinaison, evaluationSolution))# on garde que les combianasions préentes dans TOUS les ensembles possibles
    return possible
    
    

    

