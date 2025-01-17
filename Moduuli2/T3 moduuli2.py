import math


#str eli voidaan syöttää tekstiä
kanta_str = input("anna kanta:")
korkeus_str = input("anna korkeus:")

#float eli ilmoittaa desimaalin tarkkuudella tuloksen
korkeus = float(korkeus_str)
kanta = float(kanta_str)

pinta_ala = korkeus*kanta

#f tarkoittaa formatoitua merkkijonoa
#liittää muuttujien arvot suoraan merkkijonoon

# mahdollistaa arvon muotoilun
print(f"pinta ala on {pinta_ala:.2f}")
print(f"Piiri on {kanta*2+korkeus*2}")