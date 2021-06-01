import random

#kopat.
voitot = []
tasapelit = []
kierrokset = []

while True:
    #oma valinta.
    
    valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
    if valinta == "Lopeta":
        break
    print("Sinä valitsit:", valinta)
    
    if valinta == "Jalka":
        kayttaja = 1

    elif valinta == "Torakka":
        kayttaja = 3

    elif valinta == "Ydinase":
        kayttaja = 2
    
    #tietokoneen valinta.
        
    tietokone = random.randint(1,3)

    if tietokone == 1:
        valinta2 = "Jalka"
        
    elif tietokone == 3:
        valinta2 = "Torakka"
        
    elif tietokone == 2:
        valinta2 = "Ydinase"
    
    print("tietokone valitsi:", valinta2)

    kierrokset.append(1)

    #boolean laskenta.

    if ((kayttaja == 1 and tietokone == 3) or (kayttaja == 2 and tietokone == 1)\
        or (kayttaja == 3 and tietokone == 2)):
        print("Voitit!")
        voitot.append(1)

    elif ((kayttaja == 1 and tietokone == 2) or (kayttaja == 3 and tietokone == 1)\
        or (kayttaja == 2 and tietokone == 3)):
        print("Hävisit!")

    else:
        print("Tasapeli!")
        tasapelit.append(1)
   

print("Pelasit",len(kierrokset), "kierrosta, joista voitit",len(voitot), "ja pelasit tasan",len(tasapelit), "peliä.")



