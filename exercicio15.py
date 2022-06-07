kmpercorridos = float(input(('Digite a quantidade de Km percorridos:')))
diasalugados = float(input('Digite a quantidade de dias alugados:'))
preçosdiarias = 60*diasalugados
preçoskm = 0.15*kmpercorridos
totalapagar = preçoskm+preçosdiarias
print(f'O carro foi alugado por {diasalugados:.0f} Dias e rodou o total de {kmpercorridos} Km \nO valor total a pagar é de R$: {totalapagar}')