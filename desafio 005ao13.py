n1 = int(input('Digite um numero: ')) #exercicio 05
print(f'O numero digitado foi {n1}, o seu antecessor é {n1-1} e o sei sucessor é {n1+1}')

n2 = int(input('Digite um segundo numero: ')) #exercicio6
print(f'O Numero digitado foi: {n2}, o dobro deste numero é {n2*2}, o seu triplo é {n2*3} e sua raiz quadrada é {n2**(1/2):.2f}')

n3 = float(input('Digite a nota 1: ')) #exercicio7
n4 = float(input('Digite a nota 2: '))
print(f'A média do aluno é: {(n3+n4)/2}')

n5 = float(input('Digite um valor em metros: ')) #exercicio8
print(f'{n5:.2f} metros equivale á {n5*100:.1f} centimetros e equivale á {n5*1000} milimetros')

n6 = int(input('Digite um valor para calcular a tabuada: ')) #exercicio9
print(f' {n6} x 1 = {n6*1} \n {n6} x 2 = {n6*2} \n {n6} x 3 = {n6*3} \n {n6} x 4 = {n6*4} \n {n6} x 5 = {n6*5} \n {n6} x 6 = {n6*6} \n {n6} x 7 = {n6*7}\n {n6} x 8 = {n6*8} \n {n6} x 9 = {n6*9} \n {n6} x 10 = {n6*10}')

n7 = float(input('Qual o valor vocÊ tem em sua carteira: ')) #exercicio10
print(f'Com {n7:.2f} Reais é possivel comprar {n7/3.27:.2f} dolares')

n8 = float(input('Digite a largura da parede: ')) #exercicio11
n9 = float(input('Digite a altura da parede: '))
areaparede = n8*n9
print(f'A àrea da parede é: {areaparede}m²')
print(f'Você precisa de {areaparede/2} litros de tinta para pintar a parede.')

n10 = float(input('Digite o preço do produto: ')) #exercicio12
cincoporcento = (n10*5)/100
valordesconto = n10-cincoporcento
print(f'O valor deste produto com desconto é de: {valordesconto}')

n11 = int(input('Digite o salario: ')) #exercicio13
quinzeporcento = (n11*15)/100
valorsalario = n11+quinzeporcento
print(f'O valor do salario com 15% de aumento é de: {valorsalario}')

n12 = float(input('Digite a temperatura em ºC:')) #Exercicio14
convertetemp = ((n12*9)/5)+32
print(f'{n12}ºC equivale à {convertetemp:.2f}ºF')