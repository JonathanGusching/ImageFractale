import image_fractale as fract
import numpy.random as rd

#Utilise une loi de Poisson pour modifier les couleurs
#Mutation trop faible?
def PoissonRGB(img,lam,n):
	rd.seed()
	nbCol=rd.randint(3)
	r,g,b=img.GetCol(n)
	if(nbCol==0):
		r=(r+rd.poisson(lam))%256
	if(nbCol==1):
		g=(g+rd.poisson(lam))%256
	if(nbCol==2):
		g=(g+rd.poisson(lam))%256	
	img.SetCol_RGB(r,g,b,n)


# Modifie aléatoirement une des quatre couleurs
def MutationCol(img,lam):
	col=rd.randint(4)
	PoissonRGB(img,lam,col)
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
		MutationCol(img,lam_poisson)
		MutationParameter(img,lam_normale)

"""
 Quelques tests :
img=fract.ImageFractale(1,2)
print(img.__str__())
img=-img
img.InterpolColour()"""
