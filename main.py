from pkg.line import *
from pkg.circle import circle_square


new_line = Line(
	start = Point(x=4.34, y=10.1),
	end = Point(x=1, y=2)
)

print(line_length(new_line))

radius_line = Line(
	start = Point(x=0, y=0),
	end = Point(x=50, y=2)
)

radius = line_length(radius_line)
square = circle_square(radius)

print(square)