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
import interface
