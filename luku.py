print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n")
toiminto = input("Mitä haluat tehdä?:")

if toiminto == "1":
    tiedosto = open("muistio.txt","r")
    sisalto = tiedosto.read()
    print(sisalto)
    tiedosto.close()
