# -*- coding: cp1252 -*-

lista = []
while True:
    valinta = int(input("Haluatko\n(1)Lis�t� listaan\n(2)\
Poistaa listalta vai \n(3)Lopettaa?: "))
    if valinta == 1:
        lisays = input("Mit� lis�t��n?: ")
        lista.append(lisays)
    elif valinta == 2:
        print("Listalla on",len(lista),"alkiota.")
        poisto = input("Monesko niist� poistetaan?: ")
        try:
            lista.pop(int(poisto))
        except Exception:
            print("Virheellinen valinta.")
    elif valinta == 3:
        print("Listalla oli tuotteet:")
        for i in lista:
            print(i)
        break
    else:
        print("Virheellinen valinta.")
          





