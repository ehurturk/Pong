import turtle


class Pong(turtle.Turtle):

	init_pos = [(-280, 0), (280, 0)]

	def __init__(self, pos_index):
		super().__init__("rectangle")
		self.init_pong(pos_index)

	def init_pong(self, pos_index):
		self.hideturtle()
		self.color("white")
		self.penup()
		self.goto(self.init_pos[pos_index])
		self.showturtle()

	def up(self):
		print(self.ycor())

		if (not self.ycor() > 199 ):
			y = self.ycor() + 40
		else:
			y = 200
		self.goto(self.xcor(), y)

	def down(self):
		print(self.ycor())
		if (not self.ycor() < -159):
			y = self.ycor() - 40
		else:
			y = -160
		self.goto(self.xcor(), y)
