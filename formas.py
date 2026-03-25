from turtle import *
import random
import math
from time import sleep

t = Turtle()

#Função plano cartesiano
def plano():
    t.pu()
    t.goto(-300,0)
    t.pd()

    t.fd(600)
    t.stamp()

    t.pu()
    t.goto(0,-300)
    t.pd()

    t.lt(90)
    t.fd(600)
    t.stamp()

plano()

#Desenho do hexagono no 1o quadrante
color = textinput("Escolha de cor", "Qual cor você deseja pro hexagono?")

def hexagono(x,y,lado,color):
    t.begin_fill()
    t.fillcolor(color)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.rt(90)
    for _ in range(6):
        t.fd(lado)
        t.rt(60)
    t.end_fill()

lado=random.randint(0,100)
altura=int(lado*math.sqrt(3))
x=random.randint(100,300)
y=random.randint(altura,300)

hexagono(x,y,lado,color)


#Desenho do losango no 2o quadrante

color = textinput("Escolha de cor", "Qual cor você deseja pro losango?")
def losango(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.rt(45)
    for _ in range(3):
        t.fd(lado)
        t.rt(90)
    t.fd(lado)
    t.rt(45)
    t.end_fill()

lado=random.randint(0,100)
altura=int(math.sqrt((lado**2)*2))
x=random.randint(-300,-altura)
y=random.randint(altura,300)


losango(x,y,lado,color)


#Desenho do octogono no 3o quadrante

color = textinput("Escolha de cor", "Qual cor você deseja pro octogono?")

def octogono(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.fd(lado)
        t.rt(45)
    t.end_fill()

lado=random.randint(0,100)
altura=int(lado*(1+math.sqrt(2)))
x=random.randint(-300,-altura)
y=random.randint(-100,0)

octogono(x,y,lado,color)


#Desenho do triangulo no 4o quadrante

color = textinput("Escolha de cor", "Qual cor você deseja pro triangulo?")

def triangulo_eq(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(3):
        t.fd(lado)
        t.lt(120)
    t.end_fill()

lado=random.randint(0,100)
altura=int((lado*math.sqrt(3))/2)
x=random.randint(0,300)
y=random.randint(-300,-altura)

triangulo_eq(x,y,lado,color)

sleep(5)
t.clear()

#Função poligono generico

lados = int(textinput("Escolha de lados", "Quantos lados você deseja para seu poligono?"))
tamanho = int(textinput("Escolha de tamanho de lado", "Qual tamanho você deseja pra cada lado?"))
color = textinput("Escolha de cor", "Qual cor você deseja para seu poligono?")

def polgen(lados,tamanho,color):
    t.pu()
    t.goto(0,0)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    angulo=360/lados
    for _ in range(lados):
        t.fd(tamanho)
        t.rt(angulo)
    t.end_fill()

polgen(lados,tamanho,color)

mainloop()