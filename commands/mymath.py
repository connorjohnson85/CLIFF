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

def powerDifferentiate(equation):
	plus_terms = equation.split('+')
	terms = []
	# apply the summation rule
	# Split it appart by + and -
	for item in plus_terms:
		if item.find('-') != -1:
			for row in item.split('-'):
				if row != item.split('-')[0]:
					row = '-' + row
				terms.append(row)
		else:
			terms.append(item)
	# Find instances of just the power rule
	newTerms = []
	for item in terms: 
		item = item.upper()
		numOfXs = item.split('X')
		if len(numOfXs)-1 == 1:
			coefficent = numOfXs[0]
			power = numOfXs[1]
			powerTerm = power.split('^')[1]
			
			newCoefficent = int(powerTerm) * int(coefficent)
			newPower = int(powerTerm) - 1 
			newTerm = str(newCoefficent) + 'x' + '^' + str(newPower)
			newTerms.append(newTerm)

	powerRuleDifferentiatedEquation = ' + '.join(newTerms)
	return powerRuleDifferentiatedEquation

def productRule(equation):
	
	firstEquation = equation[equation.index('(')+1: equation.index(')')]
	secondEquation = equation[equation.rindex('(')+1: equation.rindex(')')]
	differentiatedTerm = '({0})({1}) + ({2})({3})'.format(firstEquation, powerDifferentiate(secondEquation), secondEquation, powerDifferentiate(firstEquation))
	return differentiatedTerm


def quotientRule(equation):
	firstEquation = equation[equation.index('(')+1: equation.index(')')]
	secondEquation = equation[equation.index('/')+2:equation.rindex(')')]
	differentiatedTerm = '(({0})({1}) - ({2})({3}))/({1}^2)'.format(firstEquation, powerDifferentiate(secondEquation), secondEquation, powerDifferentiate(firstEquation))
	return differentiatedTerm

