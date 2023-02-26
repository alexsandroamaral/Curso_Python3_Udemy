nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso "))
imc = peso / (altura * altura)
# F-strings 
print(f'{nome} tem {altura:.2f} de altura') # {altura:.2f} = :.2 => Qtd de casas decimais.
