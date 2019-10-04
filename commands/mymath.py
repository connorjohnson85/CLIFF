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

def differentiate(equation):
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

	# Find instances of the quotient rules

	# Find instances of the product rules
	
	# Find instances of a chain rules


