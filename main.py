import turtle, pong, time, ball, random, score

WIDTH = 600
HEIGHT = 600
OFFSETX =20
OFFSETY = 20


x1 = WIDTH/2 - WIDTH + OFFSETX
x2 = WIDTH/2 - OFFSETX

y1 = HEIGHT/2 - HEIGHT + OFFSETY
y2 = HEIGHT/2 - OFFSETY

MAGNITUDE = 6
MIN_DIRECTION = 0
MAX_DIRECTION =360

directions = [60,100, 120, 130, 150]

# INITS:
def init_screen(width, height):
	screen = turtle.Screen()
	screen.setup(width, height)
	screen.title("Pong")
	screen.bgcolor("black")
	rectCors = ((-70,10),(70,10),(70,-10),(-70,-10))
	screen.register_shape("rectangle", rectCors)
	return screen


screen = init_screen(WIDTH, HEIGHT) # Init the Screen, must be before initing panels (pongs) becuase pongs may not create a rectangular shape

screen.tracer(0)

pong1 = pong.Pong(0)
pong2 = pong.Pong(1)

p1_score = score.ScoreBoard(5, (-100, 270))
p2_score = score.ScoreBoard(5, (100, 270))
direction = random.choice(directions)
ball = ball.Ball(direction)

pong1_up = ball.ycor() + 35
pong_1_down = ball.ycor() - 35
pong2_up = ball.ycor() + 35
pong2_down = ball.ycor() - 35

force = ball.return_force(MAGNITUDE, direction)

des_point = force.desired_point
ball.apply_force(des_point[0], des_point[1])

screen.listen()
screen.onkey(pong1.up, "w")
screen.onkey(pong1.down, "s")
screen.onkey(pong2.up, "Up")
screen.onkey(pong2.down, "Down")

game_over = False


while not game_over:

	screen.update()
	if (ball.xcor() < x1):
		p1_score.increase_score()
		ball.init_ball()

	elif (ball.xcor() > x2):
		p2_score.increase_score()
		ball.init_ball()

	if (ball.distance(pong1) <= 50 or ball.distance(pong2) <= 50):
		des_point = ball.bounce(MAGNITUDE, 180)

	if (ball.ycor() > y2 or ball.ycor() < y1):
		des_point = ball.bounce(MAGNITUDE, 360)
	ball.apply_force(des_point[0], des_point[1])

screen.exitonclick()
