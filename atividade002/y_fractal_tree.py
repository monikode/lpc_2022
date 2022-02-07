from turtle import *

speed('fastest')

# turning the turtle to face upwards
rt(-90)

# the acute angle between
# the base and branch of the Y
angle = 30


# function to plot a Y
def y(size, level):
    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255//level, 0)

        # drawing the base
        fd(size)

        rt(angle)

        # recursive call for
        # the right subtree
        y(0.8*size, level-1)

        pencolor(0, 255//level, 0)

        lt(2*angle)

        # recursive call for
        # the left subtree
        y(0.8 * size, level-1)

        pencolor(0, 255//level, 0)

        rt(angle)
        fd(-size)


# tree of size 80 and level 7
y(80, 7)
