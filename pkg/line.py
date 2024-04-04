from typing import NamedTuple


class Point(NamedTuple):
	x: int | float
	y : int | float


class Line(NamedTuple):
	start: Point
	end: Point


def line_length(line: Line) -> int | float:
	return (line.start.x - line.end.x)**2 + (line.start.y - line.end.y)**2