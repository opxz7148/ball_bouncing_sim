import turtle
import random

class Ball:

    def __init__(self, xpos, ypos, vx, vy, color, size, canvas_width, canvas_height):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def draw_circle(self):

        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.xpos, self.ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self):


        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (self.canvas_width - self.size):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (self.canvas_height - self.size):
            self.vy = -self.vy


class initilizing:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls):
        self.ball_ls = []
        for i in range(num_balls):
            self.ball_ls.append(
            Ball(
                random.randint(-1 * canvas_width + ball_radius, canvas_width - ball_radius),
                random.randint(-1 * canvas_height + ball_radius, canvas_height - ball_radius),
                random.randint(1, 0.01 * canvas_width),
                random.randint(1, 0.01 * canvas_height),
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                ball_radius,
                canvas_width,
                canvas_height
                )
            )
