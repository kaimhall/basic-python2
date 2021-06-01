# -*- coding: cp1252 -*-

def valitse():
    import random
    valinta = random.randint(1,3)
    if valinta == 1: valinta = "Jalka"
    if valinta == 2: valinta = "Ydinase"
    if valinta == 3: valinta = "Torakka"
    return valinta

def main():
    voitot = 0
    tasan = 0
    kierrokset = 0
    while True:
        valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
        if valinta not in ["Jalka","Ydinase","Torakka","Lopeta"]:
            print("Virheellinen valinta.")
            continue
        tietokone = valitse()
        if valinta == "Lopeta":
            break
        kierrokset = kierrokset + 1
        print("Sinä valitsit:",valinta)
        print("tietokone valitsi:",tietokone)
        if valinta == tietokone:
            print("Tasapeli!")
            tasan = tasan + 1
            
        elif valinta == "Jalka" and tietokone == "Torakka":
            print("Voitit!")
            voitot = voitot + 1
        elif valinta == "Jalka" and tietokone == "Ydinase":
            print("Hävisit!")

        elif valinta == "Ydinase" and tietokone == "Jalka":
            print("Voitit!")
            voitot = voitot + 1
        elif valinta == "Ydinase" and tietokone == "Torakka":
            print("Hävisit!")
            
        elif valinta == "Torakka" and tietokone == "Ydinase":
            print("Voitit!")
            voitot = voitot + 1
        elif valinta == "Torakka" and tietokone == "Jalka":
            print("Hävisit!")

            
    print("Pelasit ",kierrokset," kierrosta, \
joista voitit ",voitot," ja pelasit tasan ",tasan," peliä.", sep ="")

if __name__ == "__main__":
    main()

