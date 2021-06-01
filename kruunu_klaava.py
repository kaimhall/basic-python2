import random

numerot = []

for i in range(5):
    luku = random.randint(0,1)
    numerot.append(luku)

print("Heitetään kolikkoa viidesti:")

for i in numerot:
    if i == 0:
        print("Klaava!")

    else:
        print("Kruuna!")
