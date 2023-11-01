if __name__ == '__main__':
	# Definició de variables
	num1 = int()
	num2 = int()
	num3 = int()
	aux = int()

	# Inicialització de variables
	print('Entra el primer dels nombres a ordenar: ', end='')
	num1 = int(input())

	print('Entra el segon dels nombres a ordenar: ', end='')
	num2 = int(input())

	print('Entra el tercer dels nombres a ordenar: ', end='')
	num3 = int(input())
	
	if (num1<num2):
		aux = num1
		num1 = num2
		num2 = aux
	if (num2<num3):
		aux = num2
		num2 = num3
		num3 = aux
	if (num1<num2):
		aux = num1
		num1 = num2
		num2 = aux
	print(num1)
	print(num2)
	print(num3)