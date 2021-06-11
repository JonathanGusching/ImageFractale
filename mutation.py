import image_fractale as fract
import numpy.random as rd

#Utilise une loi de Poisson pour modifier les couleurs
def PoissonRGB(r,g,b,lam):
	nbCol=rd.randint(3)
	col=rd.randint(2)
	if(nbCol==0):
		r=(r+rd.poisson(lam)-lam)%256
	if(nbCol==1):
		g=(g+rd.poisson(lam)-lam)%256
	if(nbCol==2):
		g=(g+rd.poisson(lam)-lam)%256	

# Modifie aléatoirement une des deux couleurs de la zone de convergence
def MutationColCV(img,lam):
	r,g,b=img.GetColCV(col)
	PoissonRGB(r,g,b,lam)
	img.SetColCV_RGB(r,g,b,col)

# Modifie aléatoirement une des deux couleurs de la zone de divergence
def MutationColDV(img,lam):
	r,g,b=img.GetColCV(col)
	PoissonRGB(r,g,b,lam)
	img.SetColDV_RGB(r,g,b,col)

# Modifie le paramètre c selon une gaussienne
def MutationParameter(img,lam):
	c_x,c_y=img.GetParam_XY()
	img.SetParam_XY(c_x+rd.normal(),c_y+rd.normal())	


#à utiliser si besoin:
invert={"0":"1","1":"0"}
# Choisit aléatoirement au plus n bits à modifier uniformément / 8 bits * 3 = 24 bits
def BitWiseMutation(r,g,b,n):
	r_b=format(r,"08b") # 8 bits chacun
	g_b=format(g,"08b")	
	b_b=format(b,"08b")
	dna = r_b+g_b+b_b # 24 bits
	i=0
	#Faire les opérations ici :
	while(i<n):
		index=rd.randint(24)
		dna[index]=invert[dna[index]] #Inversion : 0 devient 1 et 1 devient 0
		i+=1
	#On remet tout dans r,g,b:
	r=int(dna[0:7],2)
	g=int(dna[8:15],2)
	b=int(dna[16:23],2)

# Fonction qui regroupe ce qu'il faut pour faire muter l'image
def RandomMutation(img,lam_normale,lam_poisson, p_mutation, nb_bits=1):
	rd.seed()
	rand_float=rd.random()
	if(p_mutation>rand_float):
		rand_float=rd.random()
		MutationColCV(img,lam_poisson)
		MutationColDV(img,lam_poisson)
		MutationParameter(img,lam_normale)


""" Quelques tests :
img=fract.ImageFractale(1,2)
print(img.__str__())
img.WriteToFile('test.txt')
img2=fract.NewFromFile('test.txt',2)
RandomMutation(img,1,2,0.1)
img=-img
"""