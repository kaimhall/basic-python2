def funktio(tiedostonimi = "what a fuck.txt"):
    tiedosto = open(tiedostonimi,"w")
    print(tiedosto.name)
    
tiedostonimi= "ti.txt"

funktio()
funktio("yeah.txt")
funktio(tiedostonimi)
