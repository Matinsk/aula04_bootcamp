#Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

# ordenando as pessoas pelo nome 

pessoas.sort(key = lambda pessoa: pessoa["nome"])

print(pessoas)

# ordendando as pessoas pela idade

pessoas.sort(key = lambda pessoa : pessoa ["idade"])

print(pessoas)