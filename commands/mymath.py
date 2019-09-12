import math

def add(num1, num2):
	return (num1 + num2)
def subtract(num1, num2):
	return (num1 - num2)
def multiply(num1, num2):
	return (num1 * num2) 
def divide(num1, num2):
	return (num1 / num2) 
def quad(num1, num2, num3):
	answer1 = (-num2 + math.sqrt(num2**2 - 4 * num1 * num3))/(2 * num1) 
	print(answer1)
	answer2 = (-num2 - math.sqrt(num2**2 -4 * num1 * num3))/(2*num1)
	print(answer2)


