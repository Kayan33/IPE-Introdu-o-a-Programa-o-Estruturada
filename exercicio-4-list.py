municipio = []
eleitor = []
branco = []
nulo = []
valido = []

porcent_branco = []
porcent_nulo = []
porcent_valido = []

for i in range (3):

    nome_muni = input(f'Nome município {i+1}: ')
    total_eleitor = int(input(f'Total eleitores: '))
    votos_branco = int(input(f'Total votos em branco: '))
    votos_nulo = int(input(f'Total votos nulos: '))
    votos_valido = int(input(f'Total votos válidos: '))

    #armazenando dados digitados
    municipio.append(nome_muni)
    eleitor.append(total_eleitor)
    branco.append(votos_branco)
    nulo.append(votos_nulo)
    valido.append(votos_valido)

    #estabelecendo porcentagem por variável
    porc_branco = (votos_branco/total_eleitor)*100
    porc_nulo = (votos_nulo/total_eleitor)*100
    porc_valido = (votos_valido/total_eleitor)*100

    porcent_branco.append(porc_branco)
    porcent_nulo.append(porc_nulo)
    porcent_valido.append(porc_valido)

    #printando dados de cada município
    print(f'|---------------------------------------------------------------------------------------------|')
    print(f'| Município: {nome_muni:<81}|')                                                           
    print(f'|---------------------------------------------------------------------------------------------|')
    print(f'|            TOTAIS            |          QUANTIDADE           |          PORCENTAGEM         |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Eleitores:                   |           {total_eleitor:<19} |              100%            |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Votos em branco:             |           {votos_branco:<18}  |{porc_branco:>18.2f}%           |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Votos nulos:                 |           {votos_nulo:<16}    |{porc_nulo:>18.2f}%           |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Votos válidos:               |           {votos_valido:<18}  |{porc_valido:>18.2f}%           |')
    print(f'|------------------------------|-------------------------------|------------------------------|')

#armazenando o maior valor de cada variável
max_eleitor = eleitor.index(max(eleitor))
max_branco = branco.index(max(branco))
max_nulo = nulo.index(max(nulo))
max_valido = valido.index(max(valido))


#printando resumo dos municípios
print(f'|---------------------------------------------------------------------------------------------------------------------------------------------|')
print(f'|                                                   RESUMO DOS MUNICÍPIOS                                                                     |')
print(f'|---------------------------------------------------------------------------------------------------------------------------------------------|')
print(f'|          TOTAIS            |                 NOME                 |             QUANTIDADE            |           PORCENTAGEM               |')
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Município mais eleitores:  |                 {municipio[max_eleitor]:<19}  |               {eleitor[max_eleitor]:<13}       |              100%                   |')
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Mais votos em branco:      |                 {municipio[max_branco]:<18}   |               {branco[max_branco]:<11}         |              {porcent_branco[max_branco]:.2f}%                  |')      
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Mais votos nulos:          |                 {municipio[max_nulo]:<16}     |               {nulo[max_nulo]:<7}             |              {porcent_nulo[max_nulo]:.2}%                 |')
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Mais votos válidos:        |                 {municipio[max_valido]:<18}   |               {valido[max_valido]:<11}         |              {porcent_valido[max_valido]:.2f}%                 |')
print(f'|---------------------------------------------------------------------------------------------------------------------------------------------|')