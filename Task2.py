""" аписати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. 
має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії."""

import turtle

user_input = int(input('Enter fractal lvl: '))
order = user_input

screen = turtle.Screen()
t = turtle.Turtle()
t.speed('fastest')
t.left(90)
t.penup()
t.goto(0, -250)  
t.pendown()
angle = 30

def draw_branch(size, level):
    if level > 0:

        t.forward(size)
        t.right(angle)

        draw_branch(0.7 * size, level - 1)

        t.left(2 * angle)

        draw_branch(0.7 * size, level - 1)

        t.right(angle)
        t.backward(size)

draw_branch(80, order)

