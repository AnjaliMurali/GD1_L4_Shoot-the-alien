import pgzrun
import random

WIDTH=800
HEIGHT=600

alien = Actor("alien")
#alien.x =  50
#alien.y = 50
ms = "Catch the alien"
def draw():
    screen.fill("red")
    alien.draw()
    screen.draw.text(ms,(300,500))

def on_mouse_down(pos):
    global ms
    #print(alien.collidepoint(pos))
    if alien.collidepoint(pos):
        alien.x = random.randint(50,750)
        alien.y = random.randint(50,HEIGHT-50)
        ms = "Good Shot! "
    else:
        ms="You missed! "

pgzrun.go()