# # # # # # # # # # # # # # # # # # # # # # #
# Autor: Marcus Vinicius Bispo Barbosa      #
# Data de criação: 27/01/2022               #
#                                           #
# Descrição: Este programa foi feito para   #
# apresentar os conceitos em torno das      #
# listas em python.                         #
# # # # # # # # # # # # # # # # # # # # # # #

listaVazia1 = list()
listaVazia2 = []
listaComum = [1, 2, 3]

print(listaVazia1) # []
print(listaVazia2) # []
print(listaComum)  # [1, 2, 3]

listaComum.append(4)

print(listaComum)  # [1, 2, 3, 4]

listaComum.remove(1)

print(listaComum)  # [2, 3, 4]

