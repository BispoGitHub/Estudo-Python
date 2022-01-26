# # # # # # # # # # # # # # # # # # # # # # #
# Autor: Marcus Vinicius Bispo Barbosa      #
# Data de criação: 26/01/2022               #
#                                           #
# Descrição: Este programa foi feito para   #
# exibir conceitos relacionados a           #
# estruturas de repetição                   #
# # # # # # # # # # # # # # # # # # # # # # #

idadeMae = int(input("Digite a idade da sua mãe: "))
idadePai = int(input("Digite a idade do seu pai: "))

if idadeMae < idadePai:
    print("A mãe é mais nova que o pai.")
elif idadePai < idadeMae:
    print("O pai é mais novo que a mãe.")
else:
    print("A mãe e o pai têm a mesma idade.")