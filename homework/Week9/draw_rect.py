import turtle

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x  #左下角x坐标
        self.y = y  #左下角y坐标
        self.width = width
        self.height = height

def draw_rect(tur, rect):
    tur.penup()
    tur.goto(rect.x, rect.y)
    tur.setheading(90)
    tur.pendown()

    for i in range(2):
        tur.forward(rect.height)
        tur.right(90)
        tur.forward(rect.width)
        tur.right(90)


x = int(input("请输入矩形左下角的x坐标:"))
y = int(input("请输入矩形左下角的y坐标:"))
w = int(input("请输入矩形的宽度:"))
h = int(input("请输入矩形的高度:"))
color = input("请输入画笔的颜色:")
speed = int(input("请输入画笔的移动速度:"))
pensize = int(input("请输入画笔的尺寸:"))

my_turtle = turtle.Turtle()
my_turtle.color(color)
my_turtle.speed(speed)
my_turtle.pensize(pensize)

my_rect = Rectangle(x, y, w, h)

draw_rect(my_turtle, my_rect)

turtle.done()
