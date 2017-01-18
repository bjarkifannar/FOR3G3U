from random import randint

end = False
turnsLeft = 10
numbers = []
numCorrect = 0
numCorrectPlace = 0
debug = False

def resetNumbers():
	global numbers
	numbers = []

	for i in range(0, 5):
		done = False

		while not done:
			tmpNum = randint(1, 8)

			if tmpNum not in numbers:
				numbers.append(tmpNum)
				done = True

	if debug:
		print(numbers)

def checkInput(input):
	global numbers
	global numCorrect
	global numCorrectPlace

	numCorrect = 0
	numCorrectPlace = 0

	validGuess = False
	tmpGuess = input.split()

	if len(tmpGuess) == 5:
		for i in range(0, 5):
			if int(tmpGuess[i]) in numbers:
				numCorrect += 1

				if int(tmpGuess[i]) == numbers[i]:
					numCorrectPlace += 1
		
		validGuess = True
	else:
		print('Please enter 5 numbers seperated by spaces')
	
	return validGuess

resetNumbers()

while not end:
	if turnsLeft > 1:
		print('%s attempts left' % turnsLeft)
	elif turnsLeft == 1:
		print('Last attempt')

	if checkInput(raw_input('Enter numbers: ')):
		turnsLeft -= 1
		print('%s number/numbers correct. %s in the correct place.' % (numCorrect, numCorrectPlace))

	if numCorrectPlace == 5:
		print('You win!')
		end = True
	elif turnsLeft == 0:
		print('Game over!')
		end = True

raw_input('Press Enter to quit...')