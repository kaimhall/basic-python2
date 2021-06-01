def testaa(merkkijono = ""):
    if len(merkkijono) < 8:
        return False
    else:
        return True

def ota_sana():
    syote = input("Syötä uusi salasana: ")
    return syote

def main():
    while True:
        ehdokas = ota_sana()
        tulos = testaa(ehdokas)
        if tulos == False:
            print("Salasana on liian lyhyt.")
            print("Yritä uudelleen.")

        else:
            print("Uusi salasana hyväksytty!")
            print("Lopetetaan.")
            break

if __name__ == "__main__":
    main()
