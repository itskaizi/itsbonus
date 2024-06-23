print('Welcome to the simple calculator program!')

#設定需要使用的數值和運算規則
first = float(input('Enter the first number:'))
second = float(input('Enter the second number:'))
oper = input('Select an arithmetic operation(+, -, *, /):')

#設立遊戲規則
if second == 0:
	if oper == '+':
		print('Result: ', first + second)
	elif oper == '-':
		print('Result: ', first - second)
	elif oper == '*':
		print('Result: ', first * second)
	elif oper == '/':
		print('Error.Division by zero.')
elif second != 0:
	if oper == '+':
		print('Result: ', first + second)
	elif oper == '-':
		print('Result: ', first - second)
	elif oper == '*':
		print('Result: ', first * second)
	elif oper == '/':
		print('Result: ', first / second)

#詢問使用者是否想要繼續遊戲
z = input('Do you want to perform another calculation? (yes or no):')

while z == 'yes':
	first = float(input('Enter the first number:'))
	second = float(input('Enter the second number:'))
	oper = input('Select an arithmetic operation(+, -, *, /):')

	if second == 0:
		if oper == '+':
			print('Result: ', first + second)
		elif oper == '-':
			print('Result: ', first - second)
		elif oper == '*':
			print('Result: ', first * second)
		elif oper == '/':
			print('Error.Division by zero.')
	elif second != 0:
		if oper == '+':
			print('Result: ', first + second)
		elif oper == '-':
			print('Result: ', first - second)
		elif oper == '*':
			print('Result: ', first * second)
		elif oper == '/':
			print('Result: ', first / second)

	z = input('Do you want to perform another calculation? (yes or no):')

print('Goodbye!')