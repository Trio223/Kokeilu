import math


#str ja input eli voidaan syöttää tekstiä ohjelman aikana eli luvut
kanta_str = input("anna kanta:")
korkeus_str = input("anna korkeus:")

#float eli ilmoittaa desimaalin tarkkuudella tuloksen
korkeus = float(korkeus_str)
kanta = float(kanta_str)

pinta_ala = korkeus*kanta

#f tarkoittaa formatoitua merkkijonoa mahdollistaa komennot tekstissä
#esim {} eivät toimisi ilman merkkiä f edessä

print(f"pinta ala on {pinta_ala:.2f}")

print(f"Piiri on {kanta*2+korkeus*2}")

#:.2f = 2 desimaalin tarkkuudella