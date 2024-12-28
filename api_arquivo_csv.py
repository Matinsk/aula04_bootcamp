import csv

arquivo = "exemplo.csv"
with open (file = arquivo, mode = 'r', encoding = 'utf-8') as arquivo_csv:
        leitor_dic = csv.DictReader(arquivo_csv)
        lista_dicionarios = []
        for item in leitor_dic:
                lista_dicionarios.append(item)
        

print(lista_dicionarios)

for valores in lista_dicionarios:
        print(valores['cidade'])