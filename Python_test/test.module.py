import sys
import pygame as pg
from pygame.locals import *

print ('Import: Done')

# locate sound files-----------------------------------------------------------------------------------------
sound1 = "./Sounds/Chuckle.wav"
sound2 = "./Sounds/Pregame.wav"
sound3 = "./Sounds/HiThere.wav"
sound4= "./Sounds/YourSuccess.wav"

print ('Define Sounds: Done')

# Initialize libraries---------------------------------------------------------------------------------------
pg.mixer.pre_init(44100, -16, 2048)
pg.init()
status = True

print ('Initialize: Done')

# Initialize sound files with legible variable names---------------------------------------------------------
Chuckle = pg.mixer.Sound(sound1)
Pregame = pg.mixer.Sound(sound2)
HiThere = pg.mixer.Sound(sound3)
YourSuccess = pg.mixer.Sound(sound4)

print ('Load Sounds: Done')

# normalize volume levels of sound bites---------------------------------------------------------------------
Chuckle.set_volume(1)
Pregame.set_volume(.5)
HiThere.set_volume(1)
YourSuccess.set_volume(1)


print ('Set Volume: Done')

# Set the JMU color pallet
lightPurple = (218,204,230)
midPurple = (181,123,206)
darkPurple = (69,0,132)
gold = (173,156,101)

# set window size
display_width = 800
display_height = 600
display = pg.display.set_mode((display_width, display_height))

#populate with title
display.fill(lightPurple)
largeText = pg.font.Font(None,50)
title = largeText.render('Scott Rikkers Soundboard', 1, gold)
display.blit(title, (190,30))


def text_objects(text, font):
    textSurface = font.render(text, True, lightPurple)
    return textSurface, textSurface.get_rect()

		# msg 		=	button text
		# x 		=	x coordinate of top left corner
		# y 		=	y coordinate of top left corner
		# w 		=	button width
		# h 		=	button height
		# ic 		=	inactive color
		# ac		=	active color
		# action	=	sound file

def button(msg, x, y, w, h, ic, ac, action=None):
	mouse = pg.mouse.get_pos()
	click = pg.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pg.draw.rect(display, ac,(x,y,w,h))

		if click[0] == 1 and action != None:
			action()
			pg.time.delay(100)       
	else:
		pg.draw.rect(display, ic,(x,y,w,h))

	smallText = pg.font.SysFont(None,20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	display.blit(textSurf, textRect)


# push display data to app
pg.display.update()
print ('Load Window: Done')

# initialize  main loop
while status:

	pg.display.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
	button("*Chuckle*",100,100,150,50,darkPurple,midPurple,Chuckle.play)
	button("Pregame!",100,200,150,50,darkPurple,midPurple,Pregame.play)
	button("Hi There",100,300,150,50,darkPurple,midPurple,HiThere.play)
	button("Your Success",100,400,150,50,darkPurple,midPurple,YourSuccess.play)
	button("Null",100,500,150,50,darkPurple,midPurple)
	button("Null",325,100,150,50,darkPurple,midPurple)
	button("Null",325,200,150,50,darkPurple,midPurple)
	button("Null",325,300,150,50,darkPurple,midPurple)
	button("Null",325,400,150,50,darkPurple,midPurple)
	button("Null",325,500,150,50,darkPurple,midPurple)
	button("Null",550,100,150,50,darkPurple,midPurple)
	button("Null",550,200,150,50,darkPurple,midPurple)
	button("Null",550,300,150,50,darkPurple,midPurple)
	button("Null",550,400,150,50,darkPurple,midPurple)
	button("Null",550,500,150,50,darkPurple,midPurple)


		





