import play
import matplotlib.pyplot as plt
import codemaker1
import codebreaker3
import codemaker2
f, (ax1, ax2) = plt.subplots(2)

def histogramme_codebreaker2():
    nbEssaisTotal = {}
    
    for i in range(100):
        print(f"2: {i}")
        nbEssai = play.play(codemaker1, codebreaker3, quiet=True)
        print("here")
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax1.hist(listEssaiTotal)
    
def histogramme_codebreaker3():
    nbEssaisTotal = {}
    
    for i in range(100):
        print(f"2: {i}")
        nbEssai = play.play(codemaker2, codebreaker3, quiet=True)
        print("here")
        if nbEssai in nbEssaisTotal.keys():
            nbEssaisTotal[nbEssai] += 1
        else:
            nbEssaisTotal[nbEssai] = 1
    
    listEssaiTotal = []
    for k,v in nbEssaisTotal.items():
        for i in range(abs(v)):
            listEssaiTotal.append(k)
    ax2.hist(listEssaiTotal)
    
def histogramme():
    histogramme_codebreaker2()
    histogramme_codebreaker3()
    plt.show()
    
histogramme()
