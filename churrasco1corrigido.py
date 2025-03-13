#Crie um aplicativo para simular os custos de um churrasco.
#front: quantidade de adultos(homens e mulheres) e crianças, retorne a quantidade de carne,frango,carvão,refrigerantes e cerveja com os custos , individuais e totais.
#back faca uma simulaçao atribuindo gramas para cada tipo de pessoa, valores diferentes para homens mulheres e crianças , simulaçao com ml e litros, calculos com cada valor para cada item, multiplique tudo e some para calcular o total do churrasco.
#variaveis ,input,print e if 

import math
print('\nPrograma de custos do churrasco')
while True:
    homens = 0
    mulheres = 0
    quant = 0
    try:
        quant = int(input('\nquantas crianças vao ? '))
        print()
        homens = int(input('\nquantos homens estao presentes? '))
        print()
        mulheres = int(input('\nquantas mulheres estao presentes? '))
        print()
        if quant < 0 or homens < 0 or mulheres < 0:
            raise ValueError
    except ValueError:
        print('\nnão digite letras ou valores invalidos apenas numeros inteiros por favor')
    else:
        break
    #QUANTIDADE DE GRAMAS
carne_homem = 400 
carne_mulher = 300
carne_criança = 200
frang_homem = 250
frang_mulher = 150 
frang_criança = 100
cerveja = 2
cerveja_mulher = 1
carvão= math.ceil((quant + homens + mulheres) //5 )* 2.5
#PREÇO DOS ALIMENTOS E BEBIDA
precocarne = 50.19

preco_frango = 39.90 

preco_carvão = 22.99

preco_cerveja = 12.99

custos = 0 

total_carne = 0
total_frango=0
total_cerveja = 0
#CODIGO DA CARNE
try:
    opcao_carne = str(input('gostaria de adicionar carne? responda com sim ou nao ')).strip().lower()
    if opcao_carne == 0:
        raise ValueError 
    print()
    if opcao_carne == 'sim':
        total_carne = (homens*carne_homem + mulheres * carne_mulher + quant * carne_criança)/1000
        custo_carne = total_carne * precocarne
        custos += custo_carne
        print()
        print('total de carne foi {:.2f} KG e o custo da carne foi {:.2f} R$'.format(total_carne,custo_carne))
    elif opcao_carne in ['nao' , 'não']:
        print('nao havera carne')
        print()
except ValueError:
    print('digite sim ou não por favor')
#CODIGO DO FRANGO
try:
    opcao_frango = str(input('gostaria de adicionar frango? responda com sim ou nao ')).strip().lower()
    print()
    if opcao_frango == 'sim':
        total_frango = (homens * frang_homem + mulheres * frang_mulher + quant * frang_criança)/1000
        custo_frango = total_frango * preco_frango
        custos += custo_frango
        print('total de frango foi {:.2f} KG e o custo foi de {:.2f} R$'.format(total_frango , custo_frango))
        print()
    elif opcao_frango in ['nao' , 'não']:
        print('nao havera frango')
        print()
except ValueError:
    print('digite sim ou não por favor')
#CODIGO DA CERVEJA
try:
    opcao_cerveja = str(input('gostaria de adicionar cerveja? responda com sim ou nao ')).strip().lower()
    print()
    if opcao_cerveja == 'sim':
        total_cerveja = (homens * cerveja + mulheres * cerveja_mulher)
        custo_cerveja = total_cerveja * preco_cerveja
        custos += custo_cerveja
        print('o total de cerveja foi de {:.2f} ml e o custo da cerveja foi de {:.2f} R$'.format(total_cerveja,custo_cerveja))
        print()
    elif opcao_cerveja in ['nao' , 'não']:
        print('nao havera cerveja')
except ValueError:
    print('digite sim ou não')
#CONTA DO CARVÃO E CUSTO TOTAL
ccarvao = carvão * preco_carvão
custos += ccarvao
print('--O CUSTO TOTAL DO CHURRASCO--')
print()
print('custo do churrasco juntamente com o preço do carvão foi de {:.3f} R$'.format(custos))