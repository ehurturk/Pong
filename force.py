import math

class Force:
	def __init__(self, mag, _dir): # Direction must be above the horziontal, when E = 0, N = 90, W = 180, S = 270

		self.dir = (_dir / 180) * math.pi
		self.des_dir = 0

		try:
			if self.dir <= 90:   ## FOR BOUNCE NOPEEEE DOPEEEE
				self.des_dir = self.dir
				self.x_comp = mag * math.cos(self.dir)
				self.y_comp = mag * math.sin(self.dir)

			elif self.dir > 90 and 180 >= self.dir:  # OK FOR 229 (cos(-131) = -0.656) BOUNCE
				self.des_dir = 180-self.dir
				self.temp_x = math.cos(self.dir - 180)
				self.temp_y = math.sin(self.dir - 180)

				self.x_comp = mag * 2 * (self.temp_x/2 - self.temp_x)
				self.y_comp = mag * self.temp_y


			elif self.dir > 180 and 270 >= self.dir:
				self.des_dir = self.dir - 180
				self.temp_x = math.cos(self.dir - 180)
				self.temp_y = math.sin(self.dir - 180)

				self.x_comp = mag * 2 * (self.temp_x/2 - self.temp_x)
				self.y_comp = mag * 2 * (self.temp_y/2 - self.temp_y)

			elif self.dir > 270 and 360 >= self.dir:
				self.des_dir = 360 - self.dir
				self.x_comp = mag * math.cos(360-self.dir)
				self.temp_y = mag * math.sin(360-self.dir)

				self.y_comp = 2 * (self.temp_y / 2 - self.temp_y)

		except Exception as e:
			raise e




		self.desired_point = self.calculate_desired_point(self.x_comp, self.y_comp)


	def calculate_desired_point(self, x_comp, y_comp):

		desired_point = (round(x_comp, 3), round(y_comp, 3))
		return desired_point
