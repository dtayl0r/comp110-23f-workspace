"""Testing Point Methods."""

from lessons.CQ07.point import Point

og_point: Point = Point(2.0, 5.0)

print("Original Point:")
print(og_point)

og_point.scale_by(2)

print("New Point: ")
print(og_point)

new_point: Point = Point(2.0, 5.0)

print("Original Point: ")
print(new_point)

print("New Point: ")
print(new_point.scale(2))