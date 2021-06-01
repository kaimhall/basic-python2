
def pituusmitta(merkkijono):
        if merkkijono == 0:
            return False

        elif merkkijono == "Lopeta":
            return "Lopeta"
        
        else:
            return len(merkkijono)

def main():

    while True:

        #kutsuu function ja tuloksen
        tulos = pituusmitta(input("Anna syöte (Lopeta lopettaa): "))

        if tulos == "Lopeta": #break täytyy olla if. 
            break
        
        elif tulos == False:
            print("Et antanut syötettä")

        else:
            print( "Antamasi syöte oli", tulos, "merkkiä pitkä.")

if __name__=="__main__":
    main()
