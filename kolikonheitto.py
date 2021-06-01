mport random

print("Heitetään kolikkoa viidesti:")
for i in range(0,5):
    tulos = random.randint(0,1)
    if tulos == 0:
        print("Klaava!")
    else:
        print("Kruuna!")
