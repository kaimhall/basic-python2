

try:
    nimi = input("Minkäniminen tiedosto luodaan?: ")

    teksti = "313"
    
    kahva = open(nimi,"r")
    sisalto = kahva.read()
    sisalto = int(sisalto)
    kahva.close()

    kahva = open(nimi,"a")
    tulos = kahva.read()
    print("Saatiin tulos ",tulos)

#except IOError:
#    print("Virheellinen tiedostonnimi")

except ValueError:
    print("Tiedoston sisältö virheellinen!")

finally:
   pass
