#nomes = ['Ana', "João","Maria","Paulo"]
#for nome in nomes:
    #i = 1
    #print(f"{nome}. {nomes}")
    #i+=1                          DIFICIL DE FAZER PARA FICAR = 1.ANA 2.JOAO

nomes = ['Ana', "João","Maria","Paulo"]
for i in range(0,len(nomes)):
    print(f"{i+1}. {nomes[i]}")    #nome[i] para posição de cada valor no vetor