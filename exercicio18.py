import math
angulo = float(input('Digite o ângulo:'))
cossintan = math.radians(angulo)
cosrad = math.cos(cossintan)
print (f'O valor do consseno é: {cosrad:.2f}')
sinrad = math.sin(cossintan)
print (f'O valor do Seno é: {sinrad:.2f}')
tanrad = math.tan(cossintan)
print (f'O valor da tangente é: {tanrad:.2f}')