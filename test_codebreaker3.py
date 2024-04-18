import common

global combinaisonPossible
combinaisonPossible = set()
for c1 in common.COLORS:
    for c2 in common.COLORS:
        for c3 in common.COLORS:
            for c4 in common.COLORS:
                possiblilite = c1 + c2 + c3 + c4
                combinaisonPossible.add(possiblilite)

evaluation_possible = [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0)]
possibilite_minimum_ouverte = []
for combinaison in combinaisonPossible:
    possibilite_minimum_ouverte.append((max([len(common.donner_possibles(combinaison, ev)) for ev in evaluation_possible]), combinaison))
print(possibilite_minimum_ouverte)
print(min(possibilite_minimum_ouverte, key=lambda x: x[0]))
#[(0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0)]
