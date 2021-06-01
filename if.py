kayttajanimi = input("Anna nimi: ")

if kayttajanimi == "Erkki": 

    salasana = input("Anna Salasana: ")#pyydä SS jos KN oikein.

    if salasana != "Esimerkki":
        print("Salasana oli väärin.") #printtaa väärä salasana viesti.

    else:
        print("Salasana ja nimi oli oikein!") #kaikki oikein kunnossa.
    	
else:
    print("Nimi oli väärin.") #printtaa jos SS väärin.
