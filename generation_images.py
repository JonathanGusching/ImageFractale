import image_fractale as fract
import mutation as mut
import creat_image as c_i
import numpy as np

#Variables globales
NB_FRACT=8
P_MUT=0.10
F_NOTES="notes.txt"
N_BEST="best_fractale.png"
N_BEST_TXT="best_fractale.txt"
MAX_NOTE=5

INDEX_ERROR="Wrong index, must be between 0 and "+str(NB_FRACT-1)

#Fonction de probabilité discrète 
def proba_survie(note):
	return (note+1)/(MAX_NOTE+2)

"""Classe qui contient NB_FRACT ImageFractale sous forme d'un tableau et les notes"""
class GroupeImage:
	def __init__(self,img_fract_t=[fract.ImageFractale() for j in range(NB_FRACT)],img_fract_note_t=[0 for i in range(NB_FRACT)]):
		self.img_fract_t=img_fract_t
		self.img_fract_note_t=img_fract_note_t

	def GetImageFractale(self,n=-1):
		if(n>=0):
			try:
				return self.img_fract_t[n]
			except:
				print(INDEX_ERROR)
		return self.img_fract_t

	def SetImageFractale(self,n=-1):
		try:
			return self.img_fract_t[n]
		except:
			print(INDEX_ERROR)

	def GetNote(self,n=-1):
		try:
			if(n>=0):
				return self.img_fract_note_t[n]
		except:
			print(INDEX_ERROR)
		
		return self.img_fract_note_t

	"""note=0,n=-1 correspond à un reset """
	def SetNote(self,note=0,n=-1):
		if(n>=0):
			try:
				self.img_fract_note_t[n]=note
			except:
				print(INDEX_ERROR)
		else:
			self.img_fract_note_t=[0 for i in range(NB_FRACT)]

	def SetNoteFromFile(self,nom=F_NOTES):
		with open(nom,'r') as f:
			i=0
			while(i<NB_FRACT):
				buff = f.read(1)
				if(buff.isdigit()):
					self.SetNote(int(buff),i)
					i+=1

	def Copy(self):
		return GroupeImage(self.GetImageFractale(),self.GetImageNote())

	def Crossover(self):
		print("ok")

	def Mutation(self):
		np.random.seed()
		for i in range(NB_FRACT):
			mut.RandomMutation(self.img_fract_t[i],0.01,70,P_MUT,1)

	#Change l'ancienne génération en une nouvelle
	def NouvelleGeneration(self):
		new_gen=self.Copy()
		new_gen.Crossover()
		new_gen.Mutation()
		return new_gen
	
	#ATTENTION: Pour l'instant, ne s'occupe pas de vérifier les doublons.
	def AjoutMeilleureAuFichier(nom=N_BEST_TXT):
		i_max=np.argmax(self.GetNote())
		best_fract=self.GetImageFractale(i_max)
		#Ajout au fichier texte:
		with open(nom, 'a') as f:
			f.write('#'+self.__str__())
		f.close()

	#Enregistre les 8 fractales sous petit format
	def EnregistrerImages(self, nom):
		for i in range(NB_FRACT):
			fichier=nom+'_'+str(i//(NB_FRACT//2))+'_'+str(i%(NB_FRACT//2))
			c_i.creer_julia(self.GetImageFractale(i),fichier)

	#Enregistre la meilleure fractale de la dernière génération. On peut la faire sous former fond d'écran ou non
	def EnregistrerMeilleure(self,wallpaper=True):
		i_max=np.argmax(self.GetNote())
		best_fract=self.GetImageFractale(i_max)
		
		#Agrandissement :
		c_i.creer_julia(best_fract,nom=N_BEST,xn=700,yn=700,dpi=70)
		#fond d'écran :
		if(wallpaper):
			c_i.creer_julia(best_fract,nom="wallpaper.png",xn=3840,yn=2160,dpi=10,width=192,height=108)

"""
img_fract_t=[fract.ImageFractale() for i in range(NB_FRACT)]
gp=GroupeImage(img_fract_t)
gp.EnregistrerImages('fractale')"""