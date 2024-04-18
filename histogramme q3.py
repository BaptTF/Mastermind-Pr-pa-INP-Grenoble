import play
import matplotlib.pyplot as plt
import codemaker1
import codebreaker0

f, ax = plt.subplots()



nbEssais = []

for i in range(100):
    nbEssais.append(play.play(codemaker1, codebreaker0, quiet=True))
#print(nbEssais)

ax.hist(nbEssais)
f.savefig("Q3Histogramme")

