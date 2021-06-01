tiedosto = open(input("Minkäniminen tiedosto luodaan?: "),"w")

teksti = input("Mitä kirjoitetaan tiedostoon?: ")
tiedosto.write(teksti)

print("Luotiin tiedosto", (tiedosto.name), "ja siihen tallennettiin teksti:", teksti)

tiedosto.close()
