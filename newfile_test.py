import time
date = ((":::")+(time.strftime("%X %x"))) #string muotoilu manuaalisesti

def tarkastaja():
    try:
        filename = "muistio.txt"
        tiedosto = open(filename,"r")
        return filename
    except IOError:
        print("Oletusmuistiota ei löydy, luodaan tiedosto.")
        tiedosto = open(filename, "w")

    finally:
        print(tiedosto.name)
        return tiedosto

        
def main():
    while True:
        
        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n\
(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")

        toiminto = input("Mitä haluat tehdä?: ")
        
        if toiminto == "1":
            filename = tarkastaja()
            tiedosto = open(filename.name, "r")
            data = tiedosto.read()
            print(data)
            tiedosto.close()

        elif toiminto == "2":
            filename = tarkastaja()
            tiedosto = open(filename.name,"a")
            data = input("Kirjoita uusi merkintä:")
            tiedosto.write(data)
            tiedosto.write(date)
            tiedosto.write("\n")
            tiedosto.close()

        elif toiminto == "3":
            filename = tarkastaja()
            tiedosto = open(filename.name,"w")
            print("Muistio tyhjennetty.")
            tiedosto.close()    

        elif toiminto == "4":
            filename = muuttuja(tarkastaja)
            

        elif toiminto == "5":
            print("Lopetetaan.")
            break

if __name__ == "__main__":
    main()
