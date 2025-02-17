def calcular_salario(horas_trabalhadas, taxa_por_hora, tipo_trabalho):
    taxas = {1: 1.0, 2: 1.5}
    taxa = taxas.get(tipo_trabalho, 0.0)
    salario = horas_trabalhadas * taxa_por_hora * taxa
    return salario