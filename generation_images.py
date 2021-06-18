import image_fractale as fract
import mutation as mut
import creat_image as c_i
import numpy.random as rd

NB_FRACT=8
P_MUT=0.10

"""Classe qui contient NB_FRACT ImageFractale sous forme d'un tableau """
class GroupeImage:
	def __init__(self,img_fract_t=[fract.ImageFractale() for j in range(NB_FRACT)]):
		self.img_fract_t=img_fract_t
		"""for i in range(NB_FRACT):
			self.img_fract_t[i]=img_fract_t[i]"""
	def GetImageFractale(self,n):
		try:
			return self.img_fract_t[n]
		except:
			print("Wrong index")
	def Crossover(self):
		print("ok")

	def Mutation(self):
		rd.seed()
		for i in range(NB_FRACT):
			mut.RandomMutation(self.img_fract_t[i],0.01,70,P_MUT,1)

	def NouvelleGeneration():
		print("test")
		
	def EnregistrerImages(self, nom):
		for i in range(NB_FRACT):
			fichier=nom+'_'+str(i//(NB_FRACT//2))+'_'+str(i%(NB_FRACT//2))
			c_i.creer_julia(self.GetImageFractale(i),fichier)


img_fract_t=[fract.ImageFractale() for i in range(NB_FRACT)]
gp=GroupeImage(img_fract_t)
gp.EnregistrerImages('fractale')