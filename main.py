import numpy as np

total_de_notas = int(input("A lista possui quantas notas?\n"))
lista_notas = np.zeros(total_de_notas)
for i in range(total_de_notas):
    nota = float(input(f"Qual o valor da {int(i+1)}a nota?\n"))
    lista_notas[i] = nota
print(f"Lista de notas:\n{lista_notas}\n")


def calcular():
    print("As operações possíveis são:\nmedia: Calcula a média aritmética das notas.\ndp: Calcula o Desvio Padrão.\n"
          "min: Imprime a nota mínima.\nmax: Imprime a nota máxima.")
    calculo = input('Selecione a operação que deseja realizar\n')
    running = True
    while running:
        if calculo.lower() == "media":
            print(f"Média = {np.mean(lista_notas)}")
        elif calculo.lower() == "dp":
            print(f"Desvio Padrão = {np.std(lista_notas)}")
        elif calculo.lower() == "min":
            print(f"Nota mínima = {np.min(lista_notas)}")
        elif calculo.lower() == "max":
            print(f"Nota máxima = {np.max(lista_notas)}")
        else:
            print("Operação inválida.")
        continuar = input('Gostaria de continuar? Digite "s" ou "n".\n')
        if continuar.lower() == "n":
            print("O programa será encerrado.")
            running = False
        elif continuar.lower() == "s":
            calculo = input('Selecione a operação que deseja realizar\n')


calcular()
