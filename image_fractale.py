import cmath
class ImageFractale:
	def __init__(self,c_x,c_y,r_cv_0=0, g_cv_0=0, b_cv_0=0, r_cv_1=0, g_cv_1=0, b_cv_1=0,r_dv_1=255, g_dv_1=255, b_dv_1=255,r_dv_inf=255, g_dv_inf=255, b_dv_inf=255):
		self.c_x=c_x
		self.c_y=c_y

	# Pour éviter de se trimballer des constantes
	def GetNumCol(self):
		return 4

	def GetParamComplex(self):
		return complex(self.c_x,self.c_y)
	def GetParamXY(self):
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
	
	def SetParamComplex(self,z):
		self.c_x=z.real
		self.c_y=z.image

	def SetParamXY(self,x,y):
		self.c_x=x
		self.c_y=y

	def SetColCV(self,r,g,b,n):
		if(n==0):
			self.r_cv_0=r
			self.g_cv_0=g
			self.b_cv_0=b
		elif(n==1):
			self.r_cv_1=r
			self.g_cv_1=g
			self.b_cv_1=b

	def SetColDV(self,r,g,b,n):
		if(n==0):
			self.r_dv_1=r
			self.g_dv_1=g
			self.b_dv_1=b
		elif(n==1):
			self.r_dv_inf=r
			self.g_dv_inf=g
			self.b_dv_inf=b