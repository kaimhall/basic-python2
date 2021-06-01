
print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n")
toiminto = input("Mitä haluat tehdä?:")

if toiminto == "2":
    tiedosto = open("muistio.txt","a")
    print(tiedosto)
    lisays = input("Kirjoita uusi merkintä: ")
    print(lisays)
    tiedosto.write(lisays)
    tiedosto.write("\n")
    tiedosto.close()
    
