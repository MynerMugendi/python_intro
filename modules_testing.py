import math
import functions_2
# import functions_2 as dodo
# print(functions_2.sorted_by_age)

# from functions_2 import sorted_by_age
# print(sorted_by_age)

# from oop4 import Employee
from my_package import shapes
print(shapes.triangle_area(3,4,5))

from my_package.shapes import triangle_area
print(triangle_area(3, 4, 5))

from my_package.shapes import triangle_area as area
print(area(3, 4, 5))

print(dir(math))
print(dir(functions_2))

