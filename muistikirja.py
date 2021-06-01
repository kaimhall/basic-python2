import time
date = ((":::")+(time.strftime("%X %x"))) #string muotoilu manuaalisesti

def tarkastaja()
    


def main()
    while True:

        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n")
        toiminto = input("Mitä haluat tehdä?: ")

        if toiminto == "1":
            tiedosto = open("muistio.txt","r")
            data = tiedosto.read()
            print(data)
            tiedosto.close()

        elif toiminto == "2":
            tiedosto = open("muistio.txt","a")
            data = input("Kirjoita uusi merkintä:")
            tiedosto.write(data)
            tiedosto.write(date)
            tiedosto.write("\n")
            tiedosto.close()

        elif toiminto == "3":
            print("Muistio tyhjennetty.")
            tiedosto = open("muistio.txt","w")
            tiedosto.close()    

        elif toiminto == "4":
            print("Lopetetaan.")
            break
