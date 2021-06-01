
kierrokset = int(input("Kuinka monta kierrosta?: "))#input

tulos = int(0) #tässä vaiheessa nolla

for i in range(0, kierrokset):#0-input
    tulos = tulos + i # kumuloituva kierrosnumroiden summa

print("Kertymäksi saatiin:", tulos)
