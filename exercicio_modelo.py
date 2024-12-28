from typing import Dict, Any
livros01: Dict[str,Any] = {
   "Título":"Game of Thrnoes",
   "Autor" :"Estagiário",
   "Ano":2005

}

livros02: Dict[str,Any] = {
   "Título":"Game of Thrnoes",
   "Autor" :"Estagiário",
   "Ano":2005

}

lista_de_livros = []
lista_de_livros.append(livros01)
lista_de_livros.append(livros02)




lista_de_livros_usando_dict:dict =  {
    "livro_01" : { "Título":"Game of Thrnoes",
   "Autor" :"Estagiário",
   "Ano":2005
},
    "livro_02" : {"Título":"Game of Thrnoes",
   "Autor" :"Estagiário",
   "Ano":2005
}
}

print(lista_de_livros_usando_dict["livro_01"])