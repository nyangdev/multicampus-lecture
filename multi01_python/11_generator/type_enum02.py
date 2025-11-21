from enum import Enum

color = Enum("Color", ["RED", "BLUE", "GREEN"])

print(color)
print(color.RED)
print(color.RED.name)
print(color.RED.value)