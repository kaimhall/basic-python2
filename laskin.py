import math

luku1 = int(input("Anna ensimmäinen luku: ")) # voi tehdä myös int(input()) 
luku2 = int(input("Anna toinen luku: ")) # kokonaisluvuille.

while True:

#valinta
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n\
(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")

    print("Valitut luvut: ", luku1, luku2) #näyttää luvut
    valinta = input("Tee valinta (1-8): ") #if-elif,else ehtoihin

    if valinta == "1":
        tulos = (luku1) + (luku2)
        print("Tulos on:", tulos)

    elif valinta == "2":
        tulos = (luku1) - (luku2)
        print("Tulos on:", tulos)

    elif valinta == "3":
        tulos = (luku1) * (luku2)
        print("Tulos on:", tulos)

    elif valinta == "4":
        tulos = (luku1) / (luku2)
        print("Tulos on:", tulos)

    elif valinta == "5":
        tulos = math.sin(luku1/luku2)
        print("Tulos on:", tulos)

    elif valinta == "6":
        tulos = math.cos(luku1/luku2)
        print("Tulos on:", tulos)

    elif valinta == "7": #aseta luku1 ja luku2 uusiin arvoihin
        luku1 = int(input("Anna uusi ensimmäinen luku: "))
        luku2 = int(input("Anna uusi toinen luku: "))

    elif valinta == "8": #break
        break

    else:
        print("Valintaa ei tunnistettu.")




    
    

