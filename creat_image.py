import time
import image_fractale as fract
import mutation as mt
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from julia import julia_set

def creer_julia(img,nom,xmin=-1.25,xmax=1.25,xn=375,ymin=-1.25,ymax=1.25,yn=375,maxiter=200, horizon=1099511627776.0,dpi=30,width=10,height=10):
	"""
	xmin, xmax, xn = -1.25, +1.25, 3000//8
	ymin, ymax, yn = -1.25, +1.25, 3000//8
	maxiter = 100
	horizon = 2.0 ** 40 # =1099511627776.0
	"""
	log_horizon = np.log(np.log(horizon))/np.log(2)
	cmap=(img).InterpolColour()
	c_x, c_y=img.GetParam_XY()

	""" Ce qui prend le plus de temps de calcul """
	Z, N = julia_set(xmin, xmax, ymin, ymax, xn, yn, c_x, c_y, maxiter, horizon)
    
    # Normalized recount as explained in:
    # https://linas.org/art-gallery/escape/smooth.html
    # https://www.ibm.com/developerworks/community/blogs/jfp/entry/My_Christmas_Gift

    # This line will generate warnings for null values but it is faster to
    # process them afterwards using the nan_to_num
	with np.errstate(invalid='ignore'):
		M = np.nan_to_num(N + 1 -np.log(np.log(abs(Z)))/(np.log(2)) + log_horizon)
	"""
	dpi = 30
	width = 10
	height = 10
	"""
	fig = plt.figure(figsize=(width, height), dpi=dpi)
	ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

    # Shaded rendering
	light = colors.LightSource(azdeg=315, altdeg=10)
	#M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5, norm=colors.PowerNorm(0.3), blend_mode='hsv')
	M = light.shade(M, cmap=cmap) # or cmap=plt.cm.coolwarm
    #M = light.shade(M, cmap=plt.cm.coolwarm)
    # see https://matplotlib.org/examples/color/colormaps_reference.html
	plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
	ax.set_xticks([])
	ax.set_yticks([])
	plt.savefig(nom)
	#plt.show()

"""
img=fract.ImageFractale(0,0.25, 10,0,100,155,0,0,0,180,75,255,255,255)
print(img.__str__())
#img=-img
img=-img
print(mt.PoissonRGB(img,0.7,1))
mt.MutationCol(img,0.5)
print(img)
mt.MutationCol(img,0.5)
mt.MutationCol(img,0.5)
print(img)
creer_julia(img)"""