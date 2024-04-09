import colorgram
import random
import turtle as t

# image_colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in image_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

color_list = [(202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.goto(-230, -220)
tim.speed("fastest")
space = 50
size = 20
for row in range(10):
    for dot in range(10):
        if dot == 9:
            color = random.choice(color_list)
            tim.dot(size, color)
        else:
            color = random.choice(color_list)
            tim.dot(size, color)
            tim.forward(space)
    if row % 2 == 0:
        angle = 270
    else:
        angle = 90
    tim.right(angle)
    tim.forward(space)
    tim.right(angle)

















screen = t.Screen()
screen.exitonclick()
