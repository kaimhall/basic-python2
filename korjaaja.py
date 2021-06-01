def korjaaja():

    while True:
        while True:
            try:
                luku1 = int(input("Anna luku: "))
                return luku1
            
            except ValueError:
                print("Virheellinen syöte!")   
    
        while True:
            try:
                luku2 = int(input("Anna luku: "))
                return luku2
            except ValueError:
                print("Virheellinen syöte")
            
            else:
                return luku2
