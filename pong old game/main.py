import engine
import turtle
import random

print("Welcome to PONG")

# input("Press any key to start [Except the power button]")

player1 = turtle.Turtle()
player2 = turtle.Turtle()
ball = turtle.Turtle()
board = turtle.Screen()
turtle.bgcolor("black")
player1.penup()
player2.penup()
ball.penup()
ball.shape("turtle")
player1.shape("square")
player2.shape("square")
player1.color("white")
player2.color("white")
ball.color("white")

board.setup(600, 600)

player1.goto(-250, 0)
player2.goto(250, 0)
player1.seth(90)
player2.seth(90)

paddle = ((-5, -15), (-5, 15), (5, 15), (5, -15))
turtle.register_shape("paddle", paddle)
player1.shape("paddle")
player2.shape("paddle")


def player1up():
    player1.fd(10)


def player1down():
    player1.bk(10)


def player2up():
    player2.fd(10)


def player2down():
    player2.bk(10)


ball.seth(25)

while True:
    # ball movement
    ball.fd(1)

    if ball.distance(player2) <= 30 or ball.distance(player1) <= 30 or ball.ycor() >= 250 or ball.ycor() <= -250:
        theta = ball.heading()
        randval = random.randint(0, 10)
        posneg = random.getrandbits(1)

        if posneg == 0:
            mod = 90 + randval
        elif posneg == 1:
            mod = 90 - randval

        if theta >= 270 or theta <= 90:
            if theta >= 270:
                thetaIncident = theta - 270
                thetaReflection = 180 - thetaIncident

            elif theta <= 90:
                thetaIncident = 90 - theta
                thetaReflection = 180 + thetaIncident

        elif theta > 90 and theta < 270:
            if theta > 90 and theta <= 180:
                thetaIncident = theta - 90
                thetaReflection = 0 + thetaIncident

            elif theta > 180 and theta < 270:
                theta = 270 - theta
                thetaReflection = 270 + thetaIncident

        ball.seth(thetaReflection)

        # else:
        # randval = random.randint(0, 30)
        # posneg = random.getrandbits(1)
        # if posneg == 0:
        # mod = 180 + randval
        # elif posneg == 1:
        # mod = 180 - randval
        # theta = theta + mod

    board.onkeypress(player1up, "w")
    board.onkeypress(player1down, "s")
    board.onkeypress(player2up, "i")
    board.onkeypress(player2down, "k")
    turtle.listen()

    if ball.ycor() == -250:
        if ball.heading() >= 180:
            heading = ball.heading()
            heading = heading + 95
            ball.seth(heading)
        if ball.heading() < 180:
            heading = ball.heading()
            heading = heading - 95
            ball.seth(heading)

    if ball.ycor() == 250:
        if ball.heading() >= 0 and ball.heading() < 90:
            heading = ball.heading()
            heading = heading + 95
            ball.seth(heading)
        if ball.heading() < 0 and ball.heading() > 270:
            heading = ball.heading()
            heading = heading - 95
            ball.seth(heading)
