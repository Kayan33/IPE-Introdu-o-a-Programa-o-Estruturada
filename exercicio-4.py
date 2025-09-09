
#inicializando variáveis
nome_muni = nome_muni1 = nome_muni2 = nome_muni3 = nome_muni4 = nome_muni5 = nome_muni6 = nome_muni7 = nome_muni8 = nome_muni9 = nome_muni10 = ""
eleitor = eleitor1 = eleitor2 = eleitor3 = eleitor4 = eleitor5 = eleitor6 = eleitor7 = eleitor8 = eleitor9 = eleitor10 = 0
branco = branco1 = branco2 = branco3 = branco4 = branco5 = branco6 = branco7 = branco8 = branco9 = branco10 = 0
nulo = nulo1 = nulo2 = nulo3 = nulo4 = nulo5 = nulo6 = nulo7 = nulo8 = nulo9 = nulo10 = 0 
validos = validos1 = validos2 = validos3 = validos4 = validos5 = validos6 = validos7 = validos8 = validos9 = validos10 = 0

porc_branco = porc_branco1 = porc_branco2 = porc_branco3 = porc_branco4 = porc_branco5 = porc_branco6 = porc_branco7 = porc_branco8 = porc_branco9 = porc_branco10 = 0
porc_nulo = porc_nulo1 = porc_nulo2 = porc_nulo3 = porc_nulo4 = porc_nulo5 = porc_nulo6 = porc_nulo7 = porc_nulo8 = porc_nulo9 = porc_nulo10 = 0
porc_validos = porc_validos1 = porc_validos2 = porc_validos3 = porc_validos4 = porc_validos5 = porc_validos6 = porc_validos7 = porc_validos8 = porc_validos9 = porc_validos10 = 0 


#laço para os 10 municipios
for i in range (10):
    print(f'-----Município {i+1}-----')

    nome_muni = input(f'Nome: ')
    eleitor = int(input(f'Total eleitores: '))
    branco = int(input(f'Total votos em branco: '))
    nulo = int(input(f'Total votos nulos: '))
    validos = int(input(f'Total votos válidos: '))

    
    #estabelecendo porcentagem por variável
    porc_branco = (branco/eleitor)*100
    porc_nulo = (nulo/eleitor)*100
    porc_validos = (validos/eleitor)*100


    #armazenando dados por variavel especifica da sua sequencia
    if i==0:
        nome_muni1 = nome_muni
        eleitor1 = eleitor
        branco1 = branco
        nulo1 =  nulo
        validos1 = validos 
        porc_branco1 = porc_branco
        porc_nulo1 = porc_nulo
        porc_validos1 = porc_validos 
    elif i==1:
        nome_muni2 = nome_muni
        eleitor2 = eleitor
        branco2 = branco
        nulo2 = nulo
        validos2 = validos
        porc_branco2 = porc_branco
        porc_nulo2 = porc_nulo
        porc_validos2 = porc_validos
    elif i==2:
        nome_muni3 = nome_muni
        eleitor3 = eleitor
        branco3 = branco
        nulo3 = nulo
        validos3 = validos
        porc_branco3 = porc_branco
        porc_nulo3 = porc_nulo
        porc_validos3 = porc_validos
    elif i==3:
        nome_muni4 = nome_muni
        eleitor4 = eleitor
        branco4 = branco
        nulo4 = nulo
        validos4 = validos
        porc_branco4 = porc_branco
        porc_nulo4 = porc_nulo
        porc_validos4 = porc_validos
    elif i==4:
        nome_muni5 = nome_muni
        eleitor5 = eleitor
        branco5 = branco
        nulo5 = nulo
        validos5 = validos 
        porc_branco5 = porc_branco
        porc_nulo5 = porc_nulo
        porc_validos5 = porc_validos
    elif i==5:
        nome_muni6 = nome_muni
        eleitor6 = eleitor
        branco6 = branco
        nulo6 = nulo
        validos6 = validos
        porc_branco6 = porc_branco
        porc_nulo6 = porc_nulo
        porc_validos6 = porc_validos
    elif i==6:
        nome_muni7 = nome_muni
        eleitor7 = eleitor
        branco7 = branco
        nulo7 = nulo
        validos7 = validos
        porc_branco7 = porc_branco
        porc_nulo7 = porc_nulo
        porc_validos7 = porc_validos
    elif i==7:
        nome_muni8 = nome_muni
        eleitor8 = eleitor
        branco8 = branco
        nulo8 = nulo
        validos8 = validos
        porc_branco8 = porc_branco
        porc_nulo8 = porc_nulo
        porc_validos8 = porc_validos
    elif i==8:
        nome_muni9 = nome_muni
        eleitor9 = eleitor
        branco9 = branco
        nulo9 = nulo
        validos9 = validos
        porc_branco9 = porc_branco
        porc_nulo9 = porc_nulo
        porc_validos9 = porc_validos
    else:
        nome_muni10 = nome_muni
        eleitor10 = eleitor 
        branco10 = branco
        nulo10 = nulo
        validos10 = validos
        porc_branco10 = porc_branco
        porc_nulo10 = porc_nulo
        porc_validos10 = porc_validos

    #printando dados de cada município
    print(f'|---------------------------------------------------------------------------------------------|')
    print(f'| Município: {nome_muni:<81}|')                                                           
    print(f'|---------------------------------------------------------------------------------------------|')
    print(f'|            TOTAIS            |          QUANTIDADE           |          PORCENTAGEM         |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Eleitores:                   |           {eleitor:<19} |             {porc_branco+porc_nulo+porc_validos:.2}f%          |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Votos em branco:             |           {branco:<18}  |{porc_branco:>18.2f}%           |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Votos nulos:                 |           {nulo:<16}    |{porc_nulo:>18.2f}%           |')
    print(f'|------------------------------|-------------------------------|------------------------------|')
    print(f'| Votos válidos:               |           {validos:<18}  |{porc_validos:>18.2f}%           |')
    print(f'|------------------------------|-------------------------------|------------------------------|')

#comparando para achar municipio com MAIS ELEITORES
if (eleitor1>eleitor2 
    and eleitor1>eleitor3
    and eleitor1>eleitor4
    and eleitor1>eleitor5
    and eleitor1>eleitor6
    and eleitor1>eleitor7
    and eleitor1>eleitor8
    and eleitor1>eleitor9
    and eleitor1>eleitor10):
    mais_eleitor = (nome_muni1, eleitor1)
elif (eleitor2>eleitor1
    and eleitor2>eleitor3
    and eleitor2>eleitor4
    and eleitor2>eleitor5
    and eleitor2>eleitor6
    and eleitor2>eleitor7
    and eleitor2>eleitor8
    and eleitor2>eleitor9
    and eleitor2>eleitor10):
    mais_eleitor = (nome_muni2, eleitor2)
elif (eleitor3>eleitor1
    and eleitor3>eleitor2
    and eleitor3>eleitor4
    and eleitor3>eleitor5
    and eleitor3>eleitor6
    and eleitor3>eleitor7
    and eleitor3>eleitor8
    and eleitor3>eleitor9
    and eleitor3>eleitor10):
    mais_eleitor = (nome_muni3, eleitor3)
elif (eleitor4>eleitor1
    and eleitor4>eleitor2
    and eleitor4>eleitor3
    and eleitor4>eleitor5
    and eleitor4>eleitor6
    and eleitor4>eleitor7
    and eleitor4>eleitor8
    and eleitor4>eleitor9
    and eleitor4>eleitor10):
    mais_eleitor = (nome_muni4, eleitor4)
elif (eleitor5>eleitor1
    and eleitor5>eleitor2
    and eleitor5>eleitor3
    and eleitor5>eleitor4
    and eleitor5>eleitor6
    and eleitor5>eleitor7
    and eleitor5>eleitor8
    and eleitor5>eleitor9
    and eleitor5>eleitor10):
    mais_eleitor = (nome_muni5, eleitor5)
elif (eleitor6>eleitor1
    and eleitor6>eleitor2
    and eleitor6>eleitor3
    and eleitor6>eleitor4
    and eleitor6>eleitor5
    and eleitor6>eleitor7
    and eleitor6>eleitor8
    and eleitor6>eleitor9
    and eleitor6>eleitor10):
    mais_eleitor = (nome_muni6, eleitor6)
elif (eleitor7>eleitor1
    and eleitor7>eleitor2
    and eleitor7>eleitor3
    and eleitor7>eleitor4
    and eleitor7>eleitor5
    and eleitor7>eleitor6
    and eleitor7>eleitor8
    and eleitor7>eleitor9
    and eleitor7>eleitor10):
    mais_eleitor = (nome_muni7, eleitor7)
elif (eleitor8>eleitor1
    and eleitor8>eleitor2
    and eleitor8>eleitor3
    and eleitor8>eleitor4
    and eleitor8>eleitor5
    and eleitor8>eleitor6
    and eleitor8>eleitor7
    and eleitor8>eleitor9
    and eleitor8>eleitor10):
    mais_eleitor = (nome_muni8, eleitor8)
elif (eleitor9>eleitor1
    and eleitor9>eleitor2
    and eleitor9>eleitor3
    and eleitor9>eleitor4
    and eleitor9>eleitor5
    and eleitor9>eleitor6
    and eleitor9>eleitor7
    and eleitor9>eleitor8
    and eleitor9>eleitor10):
    mais_eleitor = (nome_muni9, eleitor9)
else:
    mais_eleitor = (nome_muni10, eleitor10)

#comparando para achar municipio com MAIS VOTOS EM BRANCO
if (branco1>branco2
    and branco1>branco3
    and branco1>branco4
    and branco1>branco5
    and branco1>branco6
    and branco1>branco7
    and branco1>branco8
    and branco1>branco9
    and branco1>branco10):
    mais_branco = (nome_muni1, branco1, porc_branco1)
elif (branco2>branco1
    and branco2>branco3
    and branco2>branco4
    and branco2>branco5
    and branco2>branco6
    and branco2>branco7
    and branco2>branco8
    and branco2>branco9
    and branco2>branco10):
    mais_branco = (nome_muni2, branco2, porc_branco2)
elif (branco3>branco1
    and branco3>branco2
    and branco3>branco4
    and branco3>branco5
    and branco3>branco6
    and branco3>branco7
    and branco3>branco8
    and branco3>branco9
    and branco3>branco10):
    mais_branco = (nome_muni3, branco3, porc_branco3)
elif (branco4>branco1
    and branco4>branco2
    and branco4>branco3
    and branco4>branco5
    and branco4>branco6
    and branco4>branco7
    and branco4>branco8
    and branco4>branco9
    and branco4>branco10):
    mais_branco = (nome_muni4, branco4, porc_branco4)
elif (branco5>branco1
    and branco5>branco2
    and branco5>branco3
    and branco5>branco4
    and branco5>branco6
    and branco5>branco7
    and branco5>branco8
    and branco5>branco9
    and branco5>branco10):
    mais_branco = (nome_muni5, branco5, porc_branco5)
elif (branco6>branco1
    and branco6>branco2
    and branco6>branco3
    and branco6>branco4
    and branco6>branco5
    and branco6>branco7
    and branco6>branco8
    and branco6>branco9
    and branco6>branco10):
    mais_branco = (nome_muni6, branco6, porc_branco6)
elif (branco7>branco1
    and branco7>branco2
    and branco7>branco3
    and branco7>branco4
    and branco7>branco5
    and branco7>branco6
    and branco7>branco8
    and branco7>branco9
    and branco7>branco10):
    mais_branco = (nome_muni7, branco7, porc_branco7)
elif (branco8>branco1
    and branco8>branco2
    and branco8>branco3
    and branco8>branco4
    and branco8>branco5
    and branco8>branco6
    and branco8>branco7
    and branco8>branco9
    and branco8>branco10):
    mais_branco = (nome_muni8, branco8, porc_branco8)
elif (branco9>branco1
    and branco9>branco2
    and branco9>branco3
    and branco9>branco4
    and branco9>branco5
    and branco9>branco6
    and branco9>branco7
    and branco9>branco8
    and branco9>branco10):
    mais_branco = (nome_muni9, branco9, porc_branco9)
else:
    mais_branco = (nome_muni10, branco10, porc_branco10)

#comparando para achar municipio com MAIS VOTOS NULOS
if (nulo1>nulo2
    and nulo1>nulo3
    and nulo1>nulo4
    and nulo1>nulo5
    and nulo1>nulo6
    and nulo1>nulo7
    and nulo1>nulo8
    and nulo1>nulo9
    and nulo1>nulo10):
    mais_nulo = (nome_muni1, nulo1, porc_nulo1)
elif (nulo2>nulo1
    and nulo2>nulo3
    and nulo2>nulo4
    and nulo2>nulo5
    and nulo2>nulo6
    and nulo2>nulo7
    and nulo2>nulo8
    and nulo2>nulo9
    and nulo2>nulo10):
    mais_nulo = (nome_muni2, nulo2, porc_nulo2)
elif (nulo3>nulo1
    and nulo3>nulo2
    and nulo3>nulo4
    and nulo3>nulo5
    and nulo3>nulo6
    and nulo3>nulo7
    and nulo3>nulo8
    and nulo3>nulo9
    and nulo3>nulo10):
    mais_nulo = (nome_muni3, nulo3, porc_nulo3)
elif (nulo4>nulo1
    and nulo4>nulo2
    and nulo4>nulo3
    and nulo4>nulo5
    and nulo4>nulo6
    and nulo4>nulo7
    and nulo4>nulo8
    and nulo4>nulo9
    and nulo4>nulo10):
    mais_nulo = (nome_muni4, nulo4, porc_nulo4)
elif (nulo5>nulo1
    and nulo5>nulo2
    and nulo5>nulo3
    and nulo5>nulo4
    and nulo5>nulo6
    and nulo5>nulo7
    and nulo5>nulo8
    and nulo5>nulo9
    and nulo5>nulo10):
    mais_nulo = (nome_muni5, nulo5, porc_nulo5)
elif (nulo6>nulo1
    and nulo6>nulo2
    and nulo6>nulo3
    and nulo6>nulo4
    and nulo6>nulo5
    and nulo6>nulo7
    and nulo6>nulo8
    and nulo6>nulo9
    and nulo6>nulo10):
    mais_nulo = (nome_muni6, nulo6, porc_nulo6)
elif (nulo7>nulo1
    and nulo7>nulo2
    and nulo7>nulo3
    and nulo7>nulo4
    and nulo7>nulo5
    and nulo7>nulo6
    and nulo7>nulo8
    and nulo7>nulo9
    and nulo7>nulo10):
    mais_nulo = (nome_muni7, nulo7, porc_nulo7)
elif (nulo8>nulo1
    and nulo8>nulo2
    and nulo8>nulo3
    and nulo8>nulo4
    and nulo8>nulo5
    and nulo8>nulo6
    and nulo8>nulo7
    and nulo8>nulo9
    and nulo8>nulo10):
    mais_nulo = (nome_muni8, nulo8, porc_nulo8)
elif (nulo9>nulo1
    and nulo9>nulo2
    and nulo9>nulo3
    and nulo9>nulo4
    and nulo9>nulo5
    and nulo9>nulo6
    and nulo9>nulo7
    and nulo9>nulo8
    and nulo9>nulo10):
    mais_nulo = (nome_muni9, nulo9, porc_nulo9)
else:
    mais_nulo = (nome_muni10, nulo10, porc_nulo10)

#comparando para achar municipio com MAIS VOTOS VALIDOS
if (validos1>validos2
    and validos1>validos3
    and validos1>validos4
    and validos1>validos5
    and validos1>validos6
    and validos1>validos7
    and validos1>validos8
    and validos1>validos9
    and validos1>validos10):
    mais_validos = (nome_muni1, validos1, porc_validos1)
elif (validos2>validos1
    and validos2>validos3
    and validos2>validos4
    and validos2>validos5
    and validos2>validos6
    and validos2>validos7
    and validos2>validos8
    and validos2>validos9
    and validos2>validos10):
    mais_validos = (nome_muni2, validos2, porc_validos2)
elif (validos3>validos1
    and validos3>validos2
    and validos3>validos4
    and validos3>validos5
    and validos3>validos6
    and validos3>validos7
    and validos3>validos8
    and validos3>validos9
    and validos3>validos10):
    mais_validos = (nome_muni3, validos3, porc_validos3)
elif (validos4>validos1
    and validos4>validos2
    and validos4>validos3
    and validos4>validos5
    and validos4>validos6
    and validos4>validos7
    and validos4>validos8
    and validos4>validos9
    and validos4>validos10):
    mais_validos = (nome_muni4, validos4, porc_validos4)
elif (validos5>validos1
    and validos5>validos2
    and validos5>validos3
    and validos5>validos4
    and validos5>validos6
    and validos5>validos7
    and validos5>validos8
    and validos5>validos9
    and validos5>validos10):
    mais_validos = (nome_muni5, validos5, porc_validos5)
elif (validos6>validos1
    and validos6>validos2
    and validos6>validos3
    and validos6>validos4
    and validos6>validos5
    and validos6>validos7
    and validos6>validos8
    and validos6>validos9
    and validos6>validos10):
    mais_validos = (nome_muni6, validos6, porc_validos6)
elif (validos7>validos1
    and validos7>validos2
    and validos7>validos3
    and validos7>validos4
    and validos7>validos5
    and validos7>validos6
    and validos7>validos8
    and validos7>validos9
    and validos7>validos10):
    mais_validos = (nome_muni7, validos7, porc_validos7)
elif (validos8>validos1
    and validos8>validos2
    and validos8>validos3
    and validos8>validos4
    and validos8>validos5
    and validos8>validos6
    and validos8>validos7
    and validos8>validos9
    and validos8>validos10):
    mais_validos = (nome_muni8, validos8, porc_validos8)
elif (validos9>validos1
    and validos9>validos2
    and validos9>validos3
    and validos9>validos4
    and validos9>validos5
    and validos9>validos6
    and validos9>validos7
    and validos9>validos8
    and validos9>validos10):
    mais_validos = (nome_muni9, validos9, porc_validos9)
else:
    mais_validos = (nome_muni10, validos10, porc_validos10)

#printando resumo dos municípios
print(f'|---------------------------------------------------------------------------------------------------------------------------------------------|')
print(f'|                                                   RESUMO DOS MUNICÍPIOS                                                                     |')
print(f'|---------------------------------------------------------------------------------------------------------------------------------------------|')
print(f'|          TOTAIS            |                 NOME                 |             QUANTIDADE            |           PORCENTAGEM               |')
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Município mais eleitores:  |                 {mais_eleitor[0]:<19}  |               {mais_eleitor[1]:<13}       |              100%                   |')
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Mais votos em branco:      |                 {mais_branco[0]:<18}   |               {mais_branco[1]:<11}         |              {mais_branco[2]:.2f}%                 |')      
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Mais votos nulos:          |                 {mais_nulo[0]:<16}     |               {mais_nulo[1]:<7}             |              {mais_nulo[2]:.2f}%                 |')
print(f'|----------------------------|--------------------------------------|-----------------------------------|-------------------------------------|')
print(f'| Mais votos válidos:        |                 {mais_validos[0]:<18}   |               {mais_validos[1]:<11}         |              {mais_validos[2]:.2f}%                 |')
print(f'|---------------------------------------------------------------------------------------------------------------------------------------------|')
