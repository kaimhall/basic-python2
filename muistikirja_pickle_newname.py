import time
date = ((":::")+(time.strftime("%X %x"))) #string muotoilu manuaalisesti

def tarkastaja(tiedostonimi = "muistio.txt"):#oletusarvo nimelle

    try:
        tiedosto = open(tiedostonimi,"r")
       
    except IOError:
        if tiedostonimi != "muistio.txt":
            print("Tiedostoa ei löydy, luodaan tiedosto")
            print("Käytetään muistiota:", tiedostonimi)
            return tiedostonimi
           
        else:
            print("Oletusmuistiota ei löydy, luodaan tiedosto.")
            tiedosto = open(tiedostonimi, "w")
            print("Käytetään muistiota:", tiedostonimi)
            return tiedostonimi
            
    else:
        print("Käytetään muistiota:", tiedostonimi)
        return tiedostonimi
        tiedosto.close()
        
def main():
    while True:
    
        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n\
(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")

        toiminto = input("Mitä haluat tehdä?: ")
        
        if toiminto == "1":
            tiedosto = open(tarkastaja(),"r")
            data = tiedosto.read()
            print(data)
            tiedosto.close()

        elif toiminto == "2":
            
            tiedosto = open(tarkastaja(),"a")
            data = input("Kirjoita uusi merkintä:")
            tiedosto.write(data)
            tiedosto.write(date)
            tiedosto.write("\n")
            tiedosto.close()

        elif toiminto == "3":
            print("Muistio tyhjennetty.") 
            tiedosto = open(tarkastaja(),"w")
            tiedosto.close()    

        elif toiminto == "4":       
            uusinimi = input("Anna tiedostonimi:" )
            tarkastaja(uusinimi)
            tiedosto =open(tarkastaja())

        elif toiminto == "5":
            print("Lopetetaan.")
            break

if __name__ == "__main__":
    main()
