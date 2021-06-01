import math




while True:
    
    while True:
      try:
         luku1 = int(input("Anna luku1: "))
      except ValueError:
         print("Ei vitussa ole luku!")
         continue
      else:
         break
    
    
    while True:
      try:
         luku2 = int(input("Anna luku2: "))
      except ValueError:
         print("Ei vitussa ole luku!")
         continue
      else:
         break
    
    print ("(1)+\n(2)-\n(3)*\n(4)/\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta\n")
    valinta = int(input("Valitse: "))
    
    if valinta == 7: exit
    if valinta == 8: break
    print ("Tulos on:")
    if valinta == 1: print (luku1+luku2)
    if valinta == 2: print (luku1-luku2)
    if valinta == 3: print (luku1*luku2)
    if valinta == 4: print (luku1/luku2)
    if valinta == 5: print (math.sin(luku1/luku2))
    if valinta == 6: print (math.cos(luku1/luku2))
