
with open("merkkijono.txt","r")as merkkijono:
    for row in merkkijono:
        merkki = row.strip()
        if merkki.isalnum():
            print(merkki, "kelpaa salasanaksi.")

        else:
            print(merkki, "sisältää virheellisiä merkkejä.")


 
