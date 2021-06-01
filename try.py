nimi = input("Minkäniminen tiedosto luodaan?: ")

try:
    
    teksti = "313"
    
    kahva = open(nimi,"r")
    sisalto = kahva.read()
    kahva.close()

    kahva = open(nimi,"a")
    sisalto = kahva.read()
    sisalto = int(sisalto)

    kahva.write(teksti)
    kahva.close()

except IOError:
   pass
    


