import  random
nome1 = str(input('Digite o nome do primeiro aluno:'))
nome2 = str(input('Digite o nome do segundo aluno:'))
nome3 = str(input('Digite o nome do terceiro aluno:'))
nome4 = str(input('Digite o nome do quarto aluno:'))
nomes = [nome1, nome2, nome3, nome4]
#def selectRandom(nomes)
#    return random.choice(nomes)
selecao = random.choice(nomes)
print(f'O Aluno selecionado foi:', selecao)