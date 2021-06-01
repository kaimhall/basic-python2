
class Kilpailija:
    def __init__(self, pisteet =0, vari=""):
        self.pisteet = pisteet
        self.vari = vari
        

        pisteet = 0
        vari = ""    

        def tilanne(self):
            print("Olen", vari, "ja minulla on", pisteet, "pistettä!")

        def maali(self):
            pisteet += 1
    
def main():

    eka=kilpailija(10,"sininen")

    print(eka.tulos)

if __name__ == "__main__":
    main()
