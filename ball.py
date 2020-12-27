from turtle import Turtle
import random
import force

WIDTH = 600
HEIGHT = 600

MAGNITUDE = 100

MIN_DIRECTION = 0
MAX_DIRECTION = 360

class Ball(Turtle):

	offsetX = 20
	offsetY = 20

	def __init__(self, random_dir):
		super().__init__("circle")
		self.penup()
		self.color("blue")
		self.init_ball()
		self.motion_direction = random_dir

	def init_ball(self):
		randomX = random.randint(WIDTH/2 - WIDTH + self.offsetX , WIDTH/2 - self.offsetX)
		randomY = random.randint(HEIGHT/2 - HEIGHT + self.offsetY, HEIGHT/2 - self.offsetY)

		self.goto(randomX, randomY)

		# self.direction = random.randint(MIN_DIRECTION, MAX_DIRECTION)

		# # initial_force = self.return_force(MAGNITUDE, self.direction)
		# # print(f"Ball Initial Force Report: Mag: {MAGNITUDE} Dir: {self.direction} Force: ({initial_force})")
		# # self.apply_force(initial_force)


	def apply_force(self, force_X, force_Y):
		des_x_pos = self.xcor() + force_X
		des_y_pos = self.ycor() + force_Y
		self.goto(des_x_pos, des_y_pos)


	def return_force(self, mag, _dir):
		app_force = force.Force(mag, _dir)
		return app_force

	def bounce(self, magnitude, subtraction_direction):

		net_direction = subtraction_direction - self.motion_direction
		self.motion_direction = net_direction

		extra_points = self.return_force(magnitude, self.motion_direction) ## WOULD ALWAYS GIVE POSITIVE VALUES
		tup_force = extra_points.desired_point
		return tup_force
