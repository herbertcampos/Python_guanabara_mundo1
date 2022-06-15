import math
num = float(input('Digite um numero Real:')) #Exercicio16
print (f'O numero inteiro digitado foi {num}, e sua porção inteira é {num:.0f}')
print (f'O numero inteiro digitado foi {num}, e sua porção inteira é {int(num)}')
print (f'O numero inteiro digitado foi {num}, e sua porção inteira é {math.trunc(num)}')

cata = float(input('Digite o valor do Cateto a:'))
catb = float(input('Digite o valor do Cateto b:'))
hipa = ((cata ** 2) + (catb ** 2)) ** (1/2)
print(f'O valor da hipotenusa é: {hipa}')
hipb = math.pow(cata,2) + math.pow(catb,2)
hipbfinal = hipb ** (1/2) #muita papagaiada fazer assim mano...
print(f'O valor da hipotenusa é: {hipbfinal}')
hipc = math.hypot(cata, catb)
print(f'O valor da hipotenusa é: {hipc}')