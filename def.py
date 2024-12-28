# até 2.259,20 = isento 
# até 2.826,65 = aliquota de 7,5% - 169,44
# até 3.751,05 = aliquota de 15% - 381,44
# até R$ 4.664,68 = aliquota 22,5% - 662,77
# acima de 4.664,68 = aliquota 27,5% - 896,00


def imposto_renda(salario : float):
    if salario <= 2259.20:
        deducao = 0
    elif salario <= 2826.65:
        deducao = round((salario * 0.075) - 169.44,2)
    elif salario <= 3751.05:
        deducao = round((salario * 0.15) - 381.44,2)
    elif salario <= 4664.68:
        deducao = round((salario * 0.225) - 662.77,2)
    else:
        deducao = round((salario * 0.275) - 896.00,2)
    
    return print(f'Salario {salario} ---- Deduções: {deducao} ----- Salário líquido {salario - deducao}')

imposto_renda(30000)