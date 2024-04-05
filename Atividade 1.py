contador = 0
while contador <= 10:
    if contador % 2 != 0:
       print(f'{contador} é ímpar.')
    else:
        print(f'{contador} é par.')

    contador += 1

print("\nDiferença para o for:\n")

# ex.1 = for contador in range(0,11):        #do 0 até o 11 pois é feito a contagem 11 vezes = (0,1,2,3,4,5,6,7,8,9,10)
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for contador in numeros:
    if contador %2 != 0:
        print(f"{contador} é ímpar")
    else:
        print(f"{contador} é par")
    contador += 1   


