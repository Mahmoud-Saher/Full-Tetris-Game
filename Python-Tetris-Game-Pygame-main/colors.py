
class Colors:
	them=1
	dark_grey = (26, 31, 40)
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)
	dark_orang=(218,165,32)
	@classmethod
	def get_cell_colors(cls):
		if Colors.them==1:
			return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]

		if Colors.them==2:
			return [cls.green,cls.dark_grey,  cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]