import multiprocessing
import generation_images as g_i
import julia
import mutation
import image_fractale as fract
import time
from creat_image import creer_julia

processes=[]
if __name__=='__main__':
	fractales=[fract.ImageAleatoire() for i in range(8)]

	fractales[1]= fractales[0].Copy()
	mutation.RandomMutation(fractales[1],0.02,70,0.8 , nb_bits=1)

	fractales_t=g_i.GroupeImage(fractales)

	fractales_t.EnregistrerImages('fractale')
	import interface
	"""
	for i in range(8):
		p = multiprocessing.Process(target=creer_julia,args=(fractales[i],))
		#p=multiprocessing.Process(target=id)
		processes.append(p)
		p.start()
	
	for process in processes:
		process.join()
	"""