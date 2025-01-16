nimi = input('Hei kuka olet: ')
terve = "Terve, " + nimi + "!"
print(terve)
print(f"moi {nimi}, mitä kuuluu")

#input lukee kaikki syötteet

lukuA_str = input("anna kokonaissluku:")
#merkkijono kokonaisluvuksi
lukuA_str = int(lukuA_str)
lukuB = int(input("anna toinen luku: "))
summa = lukuA + lukuB
print(f"lukujen summa = {summa}")