#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista_linguagens : list = ["Python", "Java", "C++", "JavaScript"]

lista_linguagens.remove("C++")

lista_linguagens.append("Ruby")

print(lista_linguagens)