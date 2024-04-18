import random
from common import *

assert evaluation("RVBR","RVBR") == (4,0) #evaluation dont on est sur du résultat
assert evaluation("RRBR","RVBR") == (3,0)#idem
assert evaluation("RVBR","VRRB") == (0,4)#idem
assert evaluation("RVBR","JROJ") == (0,1)#idem
assert evaluation("JRVB","JROR") == (2,0)#idem
assert evaluation("JJVB","JRJR") == (1,1)#idem
assert evaluation("JVVB","JRBV") == (1,2)#idem
assert evaluation("JRVB","VRBJ") == (1,3)#idem
assert evaluation("RJBV","RBJV") == (2,2)#idem
assert evaluation("RJVB","NMOG") == (0,0)#idem



# Création d'un test aléatoire
def test_aléatoire():
    comb = "" # on créé une combainaison vide
    ref = "" # on créé une référence vide
    for i in range(4):
        comb += random.choice(COLORS) # on a créé aléatoirement une combianaiso/proposition de 4 couleurs
        ref += random.choice(COLORS) # on a créé aléatoirement une combinasion/référence de 4 couleurs
    return (comb, ref, evaluation(comb,ref))# on retourne la proposition, la référence et le résultat de l'évaluation entre les deux
    
print(test_aléatoire()) #affiche la comb la ref et l'évaluation 