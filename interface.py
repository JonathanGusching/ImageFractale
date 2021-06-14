from tkinter import *
from functools import partial


# constantes de couleurs
BG_COLOUR = '#363636'
TEXT_COLOUR = '#000'
BUTTON_COLOUR = '#ECECEC'
ACTIVATED_BUTTON_COLOUR = '#9C9C9C'

# taille des images 
IMAGE_WIDTH = 400
IMAGE_HEIGHT = 225



# affiche le bouton associé après clic et le maintient enfoncé en réinitialisant ceux dans le même groupement
def res_button(button_position):
	for k in range(6):
		# remise à la couleur d'origine des autres boutons du groupement
		buttons[button_position[0]][button_position[1]][k].config(bg=BUTTON_COLOUR)
	buttons[button_position[0]][button_position[1]][button_position[2]].config(bg=ACTIVATED_BUTTON_COLOUR)

	return(button_position)


# renvoie les notes si elles ont toutes été données et que l'on a appuyé sur le bouton de validation
def valider():
	pass


# efface tout et affiche la meilleure fractale finale
def arreter():
	pass


	

# GENERATION DES WIDGETS

# initialisation et personnalisation de la fenêtre
window = Tk()
window.title("Fractales génétiques")
window.geometry("1920x1080") # taille par défaut
img = PhotoImage(file='icone.png')  # logo fenêtre
window.tk.call('wm', 'iconphoto', window._w, img)
window.config(background='#363636')


# frame centrale contenant celles contenant les images et les boutons de notation 
centralframe = Frame(window, bg=BG_COLOUR)
# frames contenant les boutons de validation et d'arrêt
frame_validation_stop = Frame(window, bg=BG_COLOUR)

# frames contenant les images et les boutons de notation
frames = []
for i in range(4):
	frames.append([])
	for j in range(4):
		frames[i].append(Frame(centralframe, bg=BG_COLOUR))



# boutons validation finale et arrêt
validation_button = Button(frame_validation_stop, text='Valider', font=("Arial", 30), bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=valider)
validation_button.grid(row=0, column=1, padx=50)
stop_button = Button(frame_validation_stop, text='Arrêter', font=("Arial", 30), bg=BUTTON_COLOUR, fg=TEXT_COLOUR, command=arreter)
stop_button.grid(row=0, column=0, padx=50)

# boutons de notation
buttons = []
# les lignes 1 et 3 correspondent aux boutons
for i in [1,3]:
	buttons.append([])
	for j in range(4):
		# on se ramène à 0,1 correspondant aux positions dans les listes (1->0, 3->1)
		i_liste = (i-1)//2
		buttons[i_liste].append([])
		for k in range(6):
			buttons[i_liste][j].append(Button(frames[i][j], text=str(k), font=("Arial", 30), bg=BUTTON_COLOUR, fg=TEXT_COLOUR, activebackground=ACTIVATED_BUTTON_COLOUR, command=partial(res_button, [i_liste,j,k])))



# images 
images = []
canvas = []
# les lignes 0 et 2 correspondent aux images
for i in [0,2]:
	images.append([])
	canvas.append([])
	for j in range(4):
		# comme pour les buttons (ici : 0->0, 2->1)
		i_liste = i//2
		images[i_liste].append(PhotoImage(file='fractale_'+str(i_liste)+'_'+str(j)+'.png'))
		canvas[i_liste].append(Canvas(frames[i][j], bg=BG_COLOUR, width=IMAGE_WIDTH, height=IMAGE_HEIGHT))
		canvas[i_liste][j].create_image(IMAGE_WIDTH//2, IMAGE_HEIGHT//2, image=images[i_liste][j])





# AFFICHAGE DES WIDGETS

for i in range(2):
	for j in range(4):
		canvas[i][j].pack()



for i in range(2):
	for j in range(4):
		for k in range(6):
			buttons[i][j][k].grid(row=1, column=k)


for i in range(4):
	for j in range(4):
		frames[i][j].grid(row=i, column=j, padx=20, pady=20)




centralframe.pack(expand=YES)
frame_validation_stop.pack(expand=YES)




window.mainloop()







