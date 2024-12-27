#Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

lista_idade = [i for i in range(108)]

lista_maior_de_idade = [idade for idade in lista_idade if idade >= 18]

print(lista_maior_de_idade)