from typing import NamedTuple


class Point(NamedTuple):
	x: int
	y : int


class Line(NamedTuple):
	start: Point
	end: Point


# This function returns length of a line
def length(line: Line) -> int:
	return (line.start.x - line.end.x)**2 + (line.start.y - line.end.y)**2