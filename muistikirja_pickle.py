import time
date = ((":::")+(time.strftime("%X %x"))) #string muotoilu manuaalisesti

nimi= "muistio.txt"

def tarkastaja(nimi):
    try:
        tiedostonimi = nimi
        tiedosto = open(tiedostonimi,"r")
        print(tiedosto)
        tiedosto.close()
                  
    except IOError:
        
        print("Oletusmuistiota ei löydy, luodaan tiedosto.")
        tiedosto = open(tiedostonimi, "w")

    finally:
        
        return nimi
        print("Käytetään muistiota:", tiedostonimi)
        
def main():
    while True:
        
        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n\
(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")
        toiminto = input("Mitä haluat tehdä?: ")
        
        if toiminto == "1":
            tiedostonimi = tarkastaja(nimi)
            tiedosto = open(tiedostonimi, "r")
            data = tiedosto.read()
            print(data)
            tiedosto.close()

        elif toiminto == "2":
            tiedostonimi = tarkastaja(nimi)
            tiedosto = open(tiedostonimi, "a")
            data = input("Kirjoita uusi merkintä:")
            tiedosto.write(data)
            tiedosto.write(date)
            tiedosto.write("\n")
            tiedosto.close()

        elif toiminto == "3":
            print("Muistio tyhjennetty.")
            tiedostonimi = tarkastaja(nimi)
            tiedosto = open(tiedostonimi,"w")
            tiedosto.close()    

        elif toiminto == "4":
            tiedostonimi = input("Anna tiedoston nimi: ")
            tiedostonimi = tarkastaja(tiedostonimi)

        elif toiminto == "5":
            print("Lopetetaan.")
            break

if __name__ == "__main__":
    main()
