import math

def luvunkorjaaja():
    while True:
      
        while True:
            luku1 = 0
        
            try:
                luku1 = int(input("Anna ensimmäinen luku: "))
                luku1 = int(luku1)
                return luku1
            
            except ValueError:
                print("Virheellinen syöte!")

    while True:

        while True:
            luku2 = 0
            
            try:
                luku2 = int(input("Anna toinen luku: "))
                luku2 = int(luku2)
                return luku2    
            
            except ValueError:
                print("Virheellinen syöte!")

def main():

    while True:

    #valinta
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n\
(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta")

        print("Valitut luvut: ", luvunkorjaaja(luku1), luvunkorjaaja(luku2)) #näyttää luvut

        valinta = input("Tee valinta (1-8): ") #if-elif,else ehtoihin

        if valinta == "1":
            tulos = luku1+luku2
            print("Tulos on:", tulos)

        elif valinta == "2":
            tulos = luku1-luku2
            print("Tulos on:", tulos)

        elif valinta == "3":
            tulos = luku1*luku2
            print("Tulos on:", tulos)

        elif valinta == "4":
            tulos = luku1/luku2
            print("Tulos on:", tulos)

        elif valinta == "5":
            tulos = math.sin(luku1/luku2)
            print("Tulos on:", tulos)

        elif valinta == "6":
            tulos = math.cos(luku1/luku2)
            print("Tulos on:", tulos)

        elif valinta == "8": #break
            break

        else:
            print("Valintaa ei tunnistettu.")


if __name__ == "__main__":
    main()




    
    

