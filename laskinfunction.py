def nelio(leveys= float(5.0), korkeus = float(8.0)):
    pinta_ala = leveys*korkeus
    return pinta_ala

def main():

#Koska meillä on parametrien oletusarvot,
#voimme jättää joitain parametreja määrittämättä
    pinta_ala1 = nelio()
    pinta_ala2 = nelio(4.0,3.0)
    pinta_ala3 = nelio(10.0)
    pinta_ala4 = nelio(korkeus = 11.0)

    print("Neljä eri tapaa kutsua nelio-funktiota:")
    print(pinta_ala1,pinta_ala2,pinta_ala3,pinta_ala4)

if __name__ == "__main__":
    main()
