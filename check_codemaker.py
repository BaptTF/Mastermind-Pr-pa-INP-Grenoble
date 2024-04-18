import common
def check_codemaker(nom_fichier):
    combinaisonPossible = set() #Construit toutes les solutions possible car elle sont toutes possible initialement
    for c1 in common.COLORS:
        for c2 in common.COLORS:
            for c3 in common.COLORS:
                for c4 in common.COLORS:
                    possiblilite = c1 + c2 + c3 + c4
                    combinaisonPossible.add(possiblilite)
    
    with open(nom_fichier + '.txt') as f: #ouvre le fichier text
        lines = f.readlines()        #Lis les lignes dans le fichier
        for i in range(0,len(lines)-1,2): # Pour chaque ligne
            #Met a jour l'ensemble des combinaisons encore possible avec le tuple de l'évaluation associée
            combinaisonPossible = common.maj_possibles(combinaisonPossible, lines[i][:-1], tuple(map(int, lines[i+1][:-1].split(",")))) 
            if len(combinaisonPossible) == 0: #Si il n'y a plus de possibilité restante c'est qu'il a triché
                print("Il y a eu tricherie")
                return 
        print("Il n'y a pas eu tricherie")
        return 
check_codemaker("test")