
file = open("sanoja.txt", "r")
lista = file.readlines()#strip toimii muistista- uuteen listaan!!.

sortatut = lista.sort()#muista sortata ALKUPERÄINEN lista!!

leikattu = []
print("Sanat laitettuna aakkosjärjestykseen:")
for i in lista:

    leikattu.append(i.strip())#muista nyt vitussa. .STRIP lyhentää
    #!!!!!!!!!listaan lisää iteraatio!!!!!!

for i in leikattu:
    print(i)




