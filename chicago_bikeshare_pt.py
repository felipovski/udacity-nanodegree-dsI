# coding: utf-8

import csv
import matplotlib.pyplot as plt

print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

print("Número de linhas:")
print(len(data_list))

print("Linha 0: ")
print(data_list[0])

print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(2, 21):
    print("Linha {}:".format(i))
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

input("Aperte Enter para continuar...")


# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i, line in enumerate(data_list[:20], start=1):
    print(f"Line : {i}\tGender: {line[-2]}")


input("Aperte Enter para continuar...")


# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(d_list, col_index):
    """
          Função que, a partir de um data list, retorna uma nova lista contendo apenas a coluna desejada.
          Argumentos:
              d_list: Data list.
              index: Índice da coluna desejada.
          Retorna:
              Uma lista com os dados desejados.
    """
    column_list = []
    for row_index in range(len(d_list)):
        column_list.append(d_list[row_index][col_index])
    return column_list


print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
    1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

male = female = 0

for item in data_list:
    if item[-2] == 'Male':
        male += 1
    elif item[-2] == 'Female':
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.


def count_gender(d_list):
    """
          Esta função conta os gêneros presentes no dataset e retorna uma lista com respectivas quantidades.
          Argumentos:
              d_list: Data list.
          Retorna:
              Lista de int com a quantidade total de indivíduos dos gêneros masculino e feminino.
    """
    male = female = 0

    for item in d_list:
        if item[-2] == 'Male':
            male += 1
        elif item[-2] == 'Female':
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[
    1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(d_list):
    """
          Função que seleciona o gênero mais popular na lista passada como parâmetro e retorna uma string.
          Argumentos:
              d_list: Data list a ser avaliada.
          Retorna:
              String com o nome do gênero: 'Male', 'Female' ou 'Equal'.
    """
    male, female = count_gender(d_list)
    if male > female:
        return 'Male'
    elif male < female:
        return 'Female'
    else:
        return 'Equal'


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

def count_user_type(d_list):
    """
          Esta função conta os tipos de usuários presentes no dataset e retorna uma lista com respectivas quantidades.
          Argumentos:
              d_list: Data list.
          Retorna:
              Lista de int com a quantidade total de subscribers e customers.
    """
    # no futuro, pode-se utilizar a função da Tarefa 12 para descobrir todos os tipos.
    subscriber = customer = dependent = 0

    for item in d_list:
        if item[5] == 'Subscriber':
            subscriber += 1
        elif item[5] == 'Customer':
            customer += 1
        elif item[5] == 'Dependent':
            dependent += 1

    return [subscriber, customer, dependent]


def most_popular_user_type(d_list):
    """
          Função que seleciona o tipo de usuário mais popular na lista passada como parâmetro e retorna uma string.
          Argumentos:
              d_list: Data list a ser avaliada.
          Retorna:
              String com o nome do tipo de usuário: 'Subscriber', 'Customer' ou 'Equal'.
    """
    subscriber, customer, dependent = count_user_type(d_list)
    if dependent < subscriber and dependent < customer:
        if subscriber > customer:
            return 'Subscriber'
        elif subscriber < customer:
            return 'Customer'
        else:
            return 'Equal'
    else:
        return 'Dependent'

print("\nTAREFA 7: Verifique o gráfico!")
user_types_list = column_to_list(data_list, 5)
types = ["Subscriber", "Customer", "Dependent"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A condição acima é falsa porque existem campos da lista em que o gênero do usuário não foi identificado."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

max_n = 0
min_n = int(trip_duration_list[0])
sorted_trip_duration_list = []

for item in trip_duration_list:
    item = int(item)
    if min_n > item:
        min_n = item
    elif max_n < item:
        max_n = item
    sorted_trip_duration_list.append(item)

sorted_trip_duration_list = sorted(sorted_trip_duration_list)
metade_lista = len(sorted_trip_duration_list) // 2

min_trip = min_n
max_trip = max_n

trips_sum = 0
for item in sorted_trip_duration_list:
    trips_sum += item
mean_trip = trips_sum / len(sorted_trip_duration_list)

if metade_lista % 2 == 0:
    median_trip = (sorted_trip_duration_list[metade_lista] + sorted_trip_duration_list[metade_lista + 1]) / 2
else:
    median_trip = sorted_trip_duration_list[metade_lista]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 10
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")


# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    """
          Esta função conta os gêneros presentes no dataset e retorna uma lista com respectivas quantidades.
          Argumentos:
              column_list: Dataset com apenas uma coluna.
          Retorna:
              Duas listas, uma de string (items únicos do dataset) e outra de int (respectivas quantidades totais).
    """
    item_types = list(set(x for x in column_list if x != " "))
    count_items =  [0 for _ in item_types]
    for i in range(len(item_types)):
        for x in column_list:
            if x == item_types[i]:
                count_items[i] += 1
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

    column_list = column_to_list(data_list, 5)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)