#Dado um conjunto de números, calcular a média.
import statistics

numeros = [10, 20, 30, 40, 50]

media = statistics.mean(numeros)

primeiro_quartil = statistics.quantiles(numeros)[0]
segundo_quartil = statistics.quantiles(numeros)[1]
terceiro_quartil = statistics.quantiles(numeros)[2]

print(f'Média : {media}, Primeiro_quartil {primeiro_quartil} , Segundo_quartil {segundo_quartil}, Terceiro_quartil {terceiro_quartil}')




