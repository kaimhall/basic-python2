
#def main():

lista = []

while True:

    valinta = input("Haluatko\n(1)Lisätä listaan\n\
(2)Poistaa listalta vai\n(3)Lopettaa?:")

    

    if valinta == "1":    
        
        lista.append(input("Mitä lisätään?: "))

    elif valinta == "2":
        alkiot = len(lista)
        print("Listalla on ",alkiot, "alkiota")

        try:
            lista.pop(int(input("Monesko niistä poistetaan?:")))

        except IndexError:
            print("Virheellinen valinta")
            continue

    elif valinta == "3":
        print("Listalla oli tuotteet:")  
        for i in lista:
            print(i)
        break

    else:
        print("Virheellinen valinta")
        


#if __name__ == "__main__":
#    main()
    
