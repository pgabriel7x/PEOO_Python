
vetorh = []
vetorm = []
vetorf = []
vetorp = []
a = 0

while a < 15:
    print("-    -   -   -   -   -   -   -")

    h = float(input("Qual sua altura? "))
    vetorh.append(h)

    p = float(input("Qual seu peso? "))
    vetorp.append(p)

    m = str(input("Qual seu gênero? \nM - macho / F - fêmea --> "))
    if m == 'M':
        vetorm.append(m)
    elif m == 'F':
        vetorf.append(m)
    else:
        print("Por favor, siga a regra!")

    a += 1
#MEDIA
mhh = sum(vetorh)
mh = mhh/len(vetorh)
print("A média da altura do grupo é %.2f m" %mh)
#PORCENTAGEM
pm = (100/15) * len(vetorm)
pf = (100/15) * len(vetorf)


print("A porcentagem de mulheres são {} % e de homens {} % " .format(pm, pf) )



print("NÃO CONSEGUI FAZER O RESTO")



