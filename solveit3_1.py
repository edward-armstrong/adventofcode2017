import math

def solveit_3(_input):
	print(math.ceil((math.ceil(math.sqrt(_input)))/2)-(_input%(math.ceil(math.sqrt(_input)))) + (((math.ceil(math.sqrt(_input)))-1)//2))

solveit_3(368078)

