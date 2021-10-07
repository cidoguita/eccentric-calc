# pt-br: Primeiro esboço da Calculadora 'Excêntrica' (PENSAR UM NOME MAIS ADEQUADO)
# en:    First Sketch of the 'Eccentric' Calculator (FIND A BETTER NAME)

#=========================================================================================#

# pt-br: Ideia: Ao imprimir o resultado da operação, incluir um insulto aleatório
#        Exemplo: '1 - 1 = 0 (também conhecido como o número de vezes que você transou na vida)'

# en:    Idea: When printing the result of the operation, include a random insult
#        Example: '1 - 1 = 0 (a.k.a. the number of times you've had sex in your life)'


#=========================================================================================#

while True:
	
	# TODO: Fix --> number divided by ZERO
	
	ope = input ('Digite a operação (+, -, *, /) que você deseja fazer ou \'q\' para sair: ')
	# ope = input ('Input the operation (+, -, *, /) that you want or \'q\' to quit: ')
	if ope == 'q' or ope == 'Q':
		break
	elif ope == '+' or ope == '-' or ope == '*' or ope == '/':
		num1 = int(input('Digite um número: '))
		# num1 = int(input('Input a number: '))
		num2 = int(input('Digite outro número: '))
		# num2 = int(input('Input another number: '))
	else:
		print('Operação inválida, cara de cu com cãibra!')
		# print('Invalid operation, dumbass!')


	# Frases aleatórias
	# Random phrases
	fra1 = 'o número de vezes que você repetiu o jardim de infância.'
	# fra1 = 'the number of times you repeated kindergarten.'
	fra2 = 'quantos milhões você deve pra sua sogra.'
	# fra2 = 'how many millions you owe to your mother-in-law.'
	fra3 = 'o número de bilhões de neurônios conflitantes no seu cérebro.'
	# fra3 = 'the of billions of conflicting neurons in your brain.'
	fra4 = 'o número de vezes que você cagou nas calças.'
	# fra4 = 'the number of times you shit your pants.'
	fra5 = 'quantas horas você chorou no chuveiro.'
	# fra5 = 'how many hours did you cry in the shower.'
	fra6 = 'o número de vezes que você decepcionou seus pais.'
	# fra6 = 'the number of times you've let your parents down.'

	# Frases para resultados iguais à ZERO
	# Phrases for results equal to ZERO
	zer1 = 'o número de pessoas que gostam de você.'
	# zer1 = 'the number of people who like you.'
	zer2 = 'o número de amigos que você possui.'
	# zer2 = 'the number of friends you have.'
	zer3 = 'o número de vezes que você transou na vida.'
	#zer3 = 'the number of times you've had sex in your life'

	# Frases para resultados menores que ZERO
	men1 = 'o saldo da sua conta bancária.'

	import random

	fraList = [fra1, fra2, fra3, fra4, fra5, fra6]
	zerList = [zer1, zer2, zer3]
	menList = [men1]

	if ope == '+':
		tot = num1 + num2
		if (tot == 0):
			print(tot, 'ou', random.choice(zerList))
			# print(tot, 'or', random.choice(zerList))
		elif (tot < 0):
			print(tot, 'ou', random.choice(menList))
			# print(tot, 'or', random.choice(menList))
		else:
			print(tot, 'ou', random.choice(fraList))
			# print(tot, 'or', random.choice(fraList))
	
	elif ope == '-':
		tot = num1 - num2
		if (tot == 0):
			print(tot, 'ou', random.choice(zerList))
			# print(tot, 'or', random.choice(zerList))
		elif (tot < 0):
			print(tot, 'ou', random.choice(menList))
			# print(tot, 'or', random.choice(menList))
		else:
			print(tot, 'ou', random.choice(fraList))
			# print(tot, 'or', random.choice(fraList))
	
	elif ope == '*':
		tot = num1 * num2
		if (tot == 0):
			print(tot, 'ou', random.choice(zerList))
			# print(tot, 'or', random.choice(zerList))
		elif (tot < 0):
			print(tot, 'ou', random.choice(menList))
			# print(tot, 'or', random.choice(menList))
		else:
			print(tot, 'ou', random.choice(fraList))
			# print(tot, 'or', random.choice(fraList))
			
	
	elif ope == '/':
		tot = num1 / num2
		if (tot == 0):
			print(tot, 'ou', random.choice(zerList))
			# print(tot, 'or', random.choice(zerList))
		elif (tot < 0):
			print(tot, 'ou', random.choice(menList))
			# print(tot, 'or', random.choice(menList))
		else:
			print(tot, 'ou', random.choice(fraList))
			# print(tot, 'ou', random.choice(fraList))