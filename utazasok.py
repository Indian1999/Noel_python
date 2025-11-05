n = int(input())

tavolsag_lista = []
ar_lista = []
for i in range(n):
    sor = input() # pl.: "50 30000"
    sor = sor.split(" ")    # ["50", "30000"]
    tavolsag = int(sor[0])
    ar = int(sor[1])
    tavolsag_lista.append(tavolsag)
    ar_lista.append(ar)

eredmenyek = []
for i in range(len(ar_lista)):
    if ar_lista[i] / tavolsag_lista[i] > 100:
        eredmenyek.append(i + 1)

kimenet = str(len(eredmenyek))
for i in range(len(eredmenyek)):
    kimenet += " "
    kimenet += str(eredmenyek[i])

print(kimenet)