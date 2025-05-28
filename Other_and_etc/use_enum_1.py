from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
print(type(Color.GREEN))
print(Color.GREEN)
print(Color.GREEN.name)

for color in Color:
    print(color)