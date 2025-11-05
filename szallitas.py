targyak = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
targyosz = 0
for i in targyak:
    targyosz += i
print(targyosz)
dobozok = 1
doboztoltseg = 0

doboz_lista = []
for i in targyak:
    if doboztoltseg + i <= 20:
        doboztoltseg += i
    else:
        doboz_lista.append(doboztoltseg)
        dobozok += 1
        doboztoltseg = i

doboz_lista.append(doboztoltseg)
print(dobozok)