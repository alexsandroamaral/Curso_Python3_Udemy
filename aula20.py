#----------------------------------------------------------------------------------------
# Algoritmo para informar qual é o maior valor de dois valores digitados.             
# Autor: Alexsandro Amaral                                              
# Data: 25/02/2023                                                                                                                          # 
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Declaração de variáveis do Algoritmo       
# vlr1 = "Primeiro valor"                                 
# vlr2 = "Segundo valor"                                 
#----------------------------------------------------------------------------------------

vlr1 = input("Digite o primeiro valor: ")
vlr2 = input("Digite o segundo valor ")
fl_vlr1 = float(vlr1)
fl_vlr2 = float(vlr2)

if fl_vlr1 >= fl_vlr2:
    print(f"O primeiro valor digitado {fl_vlr1} é maior ou igual ao segundo valor {fl_vlr2}")
else:
    print(f"O segundo valor digitado {fl_vlr2} é maior que o primeiro valor {fl_vlr1}")


#----------------------------------------------------------------------------------------
# F-Strings => Quebra de linhas                                                                                                                                 # 
#----------------------------------------------------------------------------------------

vlr1 = input("Digite o primeiro valor: ")
vlr2 = input("Digite o segundo valor ")
fl_vlr1 = float(vlr1)
fl_vlr2 = float(vlr2)

if fl_vlr1 >= fl_vlr2:
    print(
        f'{vlr1} é maior ou igual '
        f'a {vlr2}'
    )
else:
    print(
        f'{vlr2} é maior '
        f'do que {vlr1}'
    )    