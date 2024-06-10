import pgzrun
import random

WIDTH=800
HEIGHT=600

alien = Actor("cat")
#alien.x =  50
#alien.y = 50
ms = "Catch the alien"
score = 0
def draw():
    screen.fill("red")
    alien.draw()
    screen.draw.text(ms,(300,500))
    screen.draw.text("score = "+ str(score),(300,400),color="blue")

def on_mouse_down(pos):
    global ms
    global score
    #print(alien.collidepoint(pos))
    if alien.collidepoint(pos):
        alien.x = random.randint(50,750)
        alien.y = random.randint(50,HEIGHT-50)
        ms = "Good Shot! "
        score +=1
    else:
        ms="You missed! "
        score -=1

pgzrun.go()