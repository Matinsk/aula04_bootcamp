#Dados dois dicionários, fundi-los em um único dicionário

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
dicionario3 = {"e":4,"f":10,"g":20}

dicionario_geral = {**dicionario1,**dicionario2,**dicionario3}

print(dicionario_geral)

