# encoding: utf-8

numero_input = input("Digite um número inteiro: ")
numero = int(numero_input)

dezena = (numero // 10) % 10

print("O dígito das dezenas é", dezena)
