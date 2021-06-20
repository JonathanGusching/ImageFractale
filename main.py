import matplotlib.pyplot as plt
import multiprocessing
import generation_images as g_i
import julia
import mutation
import image_fractale as fract
import time
from creat_image import creer_julia

fractales=[fract.ImageAleatoire() for i in range(8)]

fractales[1]= fractales[0].Copy()
#mutation.RandomMutation(fractales[1],0.02,70,0.8 , nb_bits=1)
mutation.BitWiseMutation(fractales[1],1)
fractales_t=g_i.GroupeImage(fractales)
#fractales_t.Mutation()
fractales_t.EnregistrerImages('fractale')
creer_julia(fractales[0],"test",xmin=-3,xmax=3,xn=375,ymin=-3,ymax=3,yn=375,maxiter=300, horizon=1099511627776.0,dpi=70,width=10,height=10)

liste_fitness = []
liste_fitness_X = []
liste_moyenne = []
liste_moyenne_X = []
gen = 0

plt.close("all")
plt.style.use("dark_background")
plt.figure(0)
couleur = ["ko","bo","ro","go"]
for i in range(8):
	coefs_x = []
	coefs_y = []
	for n in range(4):
		(x, y) = fractales[i].GetParam_XY(n)
		plt.plot(x, y,couleur[n])

plt.title("Diversité génome")
plt.legend(["coefficient de degré 0", "coefficient de degré 1", "coefficient de degré 2", "coefficient de degré 3"])
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.xlabel("partie réelle")
plt.ylabel("partie imaginaire")
plt.savefig("diversite_genome.png", transparent=True)

plt.figure(1)
fichierNotes = open("notes.txt","r")
lignes = fichierNotes.readlines()
for i in range(8):
	liste_fitness.append(int(lignes[i][0]))
	liste_fitness_X.append(gen)
liste_moyenne.append(sum(liste_fitness))
liste_moyenne_X.append(gen)
plt.plot(liste_fitness_X, liste_fitness, "bo")
plt.plot(liste_moyenne_X, liste_moyenne, "r-")

plt.title("Diversité fitness")
plt.legend(["fitness", "moyenne"])
plt.xlim([-1,gen + 1])
plt.ylim([0,5])
plt.xlabel("génération")
plt.ylabel("fitness")
plt.savefig("diversite_fitness.png", transparent=True)
plt.close("all")

import interface
