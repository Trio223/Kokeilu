import math

kanta_str = input("anna kanta:")
korkeus_str = input("anna korkeus:")

korkeus = float(korkeus_str)
kanta = float(kanta_str)

pinta_ala = korkeus*kanta
print(f"pinta ala on {pinta_ala}")
print(f"Piiri on {kanta*2+korkeus*2}")