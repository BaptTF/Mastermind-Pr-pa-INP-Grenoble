import play
import matplotlib.pyplot as plt
import codemaker1
import codemaker2
import codebreaker2

f, (ax1, ax2) = plt.subplots(2)

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
    ax1.hist(listEssaiTotal)
    
def histogramme_makerbreaker2():
    nbEssaisTotal = {}
    
    for i in range(100):
        print(f"2: {i}")
        nbEssai = play.play(codemaker2, codebreaker2, quiet=True)
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
    histogramme_makerbreaker2()
    histogramme_codebreaker2()
    f.savefig("Q8.png")
    plt.show()
    
histogramme()
