kahva = open("merkkijono.txt","r")

luettu = ""
while True:
    luettu = kahva.readline()
    if luettu == "":
        break
    luettu = luettu[:-1]
    if luettu.isalnum() == False:
        print(luettu,"sisältää virheellisiä merkkejä.")
    else:
        print(luettu,"kelpaa salasanaksi.")

kahva.close()
