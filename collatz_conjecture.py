def collatz(number):
	while number > 1:
		print(number, end=' ')
		if (number % 2):  # if odd
			number = 3*number + 1
		else:  # if even
			number = number // 2
	print('1')
	return number


def number_input():
	while True:
		try:
			ask_for_number = int(input('Input any whole number: '))
		except ValueError:
			print("Enter a whole number.")
		else:
			return ask_for_number


if __name__ == '__main__':
	collatz(number_input())
