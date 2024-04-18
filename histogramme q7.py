import play
import matplotlib.pyplot as plt
import codemaker1
import codebreaker0
import codebreaker1
import codebreaker2

f, (ax1, ax2, ax3) = plt.subplots(3)

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
    f.savefig("Q7Histogramme")
    
def histogramme_codebreaker0():
    nbEssaisTotal = {}
    
    for i in range(100):
        print(f"0: {i}")
        nbEssai = play.play(codemaker1, codebreaker0, quiet=True)
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax1.hist(listEssaiTotal)
    
def histogramme_codebreaker1():
    nbEssaisTotal = {}
    
    for i in range(100):
        print(f"1: {i}")
        nbEssai = play.play(codemaker1, codebreaker1, quiet=True)
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax2.hist(listEssaiTotal)
    
def histogramme_codebreaker2():
    nbEssaisTotal = {}
    
    for i in range(100):
        print(f"2: {i}")
        nbEssai = play.play(codemaker1, codebreaker2, quiet=True)
        print("here")
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax3.hist(listEssaiTotal)
    
def histogramme():
    histogramme_codebreaker0()
    histogramme_codebreaker1()
    histogramme_codebreaker2()
    plt.show()
    
histogramme()

