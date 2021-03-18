#Autores: Sergio Chavez y Aida Garza
#Objetivo: Programa que implementa un juego de tiro parabólico que apunta a objetivos de creación aleatoria

#Importa las librerías necesarias para poder hacer funcionar el juego
from random import randrange
from turtle import *
from freegames import vector

#Instancias de la pelota, velocidad y objetivos
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Crea una nueva pelota solamente si no se ha lanzado otra
def tap(x, y):
    #Revisa que no haya pelota en la pantalla
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 350) / 25 # se modifico la velocidad del proyectil
        speed.y = (y + 350) / 25 

#Revisa si está dentro de los límites de la pantalla y regresa true si está dentro
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Dibuja la pelota y los objetivos
def draw():
    clear()
    
    #Dibuja  cada uno de los objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
        
    #Dibuja la pelota
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    update()

# Funcion que permite que los balones se esten moviendo de forma aleatoria    
def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

 #velocidad de "targets"       
    for target in targets:
        target.x -= 3 #se modifico la velocidad de los balones para que vayan mas rapido

 #revisa si la pelota esta dentro de la pantalla       
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    
    dupe = targets.copy()
    targets.clear()
    
#Cuando el proyectil le da al balon, este se elimina de la pantalla
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

 #Revisa que cada objetivo este dentro de la pantalla
    for target in targets:
        #Si el objetivo se sale de la pantalla lo reasigna del otro lado de la pantalla
        if not inside(target):
            target.x = 199

 #despliega los proyectiles y balones en la pantalla           
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
