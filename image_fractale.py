import cmath
# Pour changer le paramètre c_x,c_y d'une image fractale, il y a trois fonctions :
"""	def SetParam_Complex(self,z):
	def SetParam_XY(self,x,y):
	def SetParam_tuple(self,tup):
"""
# Pour changer les couleurs, c'est à peu près la même chose :
"""	def SetColCV_RGB(self,r,g,b,n):
	def SetColDV_RGB(self,r,g,b,m):
	def SetColCV_tuple(self,tup,n):
	def SetColDV_tuple(self,tup,m):
 
En notant :
n=0 => couleur de convergence en 0
n=1 => couleur de convergence en 1
m=0 => couleur de divergence en 1
m=1 => couleur de divergenec en l'infini
 """
class ImageFractale:
	def __init__(self,c_x=0,c_y=0,r_cv_0=255, g_cv_0=255, b_cv_0=255, r_cv_1=255, g_cv_1=255, b_cv_1=255,r_dv_1=0, g_dv_1=0, b_dv_1=0,r_dv_inf=0, g_dv_inf=0, b_dv_inf=0):
		self.c_x=c_x
		self.c_y=c_y
		self.r_cv_0=r_cv_0
		self.g_cv_0=g_cv_0
		self.b_cv_0=b_cv_0

		self.r_cv_1=r_cv_1
		self.g_cv_1=g_cv_1
		self.b_cv_1=b_cv_1

		self.r_dv_1=r_dv_1
		self.g_dv_1=g_dv_1
		self.b_dv_1=b_dv_1

		self.r_dv_inf=r_dv_inf
		self.g_dv_inf=g_dv_inf
		self.b_dv_inf=b_dv_inf

	def __str__(self):
		return str(self.GetParam_XY())+';'+str(self.GetColCV(0))+';'+str(self.GetColCV(1))+';'+str(self.GetColDV(0))+';'+str(self.GetColDV(1))+'\n'
	# Pour éviter de se trimballer des constantes
	def GetNumCol(self):
		return 4

	# Encapsulation
	def GetParam_Complex(self):
		return complex(self.c_x,self.c_y)
	def GetParam_XY(self):
		return self.c_x,self.c_y

	def GetColCV(self,n):
		if(n==0):
			return self.r_cv_0, self.g_cv_0, self.b_cv_0
		elif(n==1):
			return self.r_cv_1, self.g_cv_1, self.b_cv_1

	def GetColDV(self,n):
		if(n==0):
			return self.r_dv_1, self.g_dv_1, self.b_dv_1
		elif(n==1):
			return self.r_dv_inf, self.g_dv_inf, self.b_dv_inf
	
	def SetParam_Complex(self,z):
		self.c_x=z.real
		self.c_y=z.image

	def SetParam_XY(self,x,y):
		self.c_x=x
		self.c_y=y
	def SetParam_tuple(self,tup):
		try:
			self.c_x=tup[0]
			self.c_y=tup[1]
		except ValueError:
			print("2-tuple expected")

	def SetColCV_RGB(self,r,g,b,n):
		if(n==0):
			self.r_cv_0=r
			self.g_cv_0=g
			self.b_cv_0=b
		elif(n==1):
			self.r_cv_1=r
			self.g_cv_1=g
			self.b_cv_1=b

	def SetColDV_RGB(self,r,g,b,n):
		if(n==0):
			self.r_dv_1=r
			self.g_dv_1=g
			self.b_dv_1=b
		elif(n==1):
			self.r_dv_inf=r
			self.g_dv_inf=g
			self.b_dv_inf=b
	def SetColCV_tuple(self,tup,n):
		try:
			if(n==0):
				self.r_cv_0=tup[0]
				self.g_cv_0=tup[1]
				self.b_cv_0=tup[2]
			elif(n==1):
				self.r_cv_1=tup[0]
				self.g_cv_1=tup[1]
				self.b_cv_1=tup[2]
		except ValueError:
			print('3-tuple expected (RGB)')

	def SetColDV_tuple(self,tup,n):
		try:
			if(n==0):
				self.r_dv_1=tup[0]
				self.g_dv_1=tup[1]
				self.b_dv_1=tup[2]
			elif(n==1):
				self.r_dv_inf=tup[0]
				self.g_dv_inf=tup[1]
				self.b_dv_inf=tup[2]
		except ValueError:
			print('3-tuple expected (RGB)')
	# Méthodes
	def WriteToFile(self,file):
		with open(file, 'a') as f:
			f.write('#'+self.__str__())
		f.close()

#Fonctions/Procédures :

#Créer une ImageFractale à partir du n-ème génome du fichier
def NewFromFile(file,n=1):
	i=0
	with open(file,'r') as f:
		while(i<n):
			buff = f.readline()
			if(buff[0]=='#'):
				i+=1
	#Traitement de la chaine de caractères
	tab=buff[1:].split(';') #On exclut le premier caractère de détection
	img=ImageFractale()
	print(eval(tab[0]))
	img.SetParam_tuple(eval(tab[0]))
	img.SetColCV_tuple(eval(tab[1]),0)
	img.SetColCV_tuple(eval(tab[2]),1)
	img.SetColDV_tuple(eval(tab[3]),0)
	img.SetColDV_tuple(eval(tab[4]),1)
	f.close()
	return img