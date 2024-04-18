import play
import matplotlib.pyplot as plt
import codemaker1
import codebreaker0
import codebreaker1

f, ax = plt.subplots()

def gain():
    nbEssaisTotal = {}
    
    for i in range(100):
        nbEssai = play.play(codemaker1, codebreaker0, quiet=True)
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    for i in range(100):
        nbEssai = play.play(codemaker1, codebreaker1, quiet=True)
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] -= 1
        else:
            nbEssaisTotal[nbEssai] = -1
       
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax.hist(listEssaiTotal)
    f.savefig("Q4Histogramme")
    
def histogramme_codebreaker1():
    nbEssaisTotal = {}
    
    for i in range(100):
        nbEssai = play.play(codemaker1, codebreaker1, quiet=True)
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax.hist(listEssaiTotal)
    
    

