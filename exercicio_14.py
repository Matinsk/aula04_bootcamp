#Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "Engenharia de dados"

colecao = {}

for letra in texto:
    if letra in colecao:
        colecao[letra] += 1
    else:
        colecao[letra] = 1

print(colecao)

colecao.sort()