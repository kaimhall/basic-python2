x = int(input("Anna luku: "))
y = int(input("Anna toinen luku: "))

if x % 2 == 0 and y % 2 == 1:
    print("Toinen luku on parillinen.")
elif x % 2 == 0 and y % 2 == 0:
    print("Molemmat luvut ovat parillisia.")
    
else:
    print("Molemmat luvut ovat parittomia.")

