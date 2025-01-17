import math

lukuA_str = input("syötä lukuA:")
lukuB_str = input("syötä lukuB:")
lukuC_str = input("syötä lukuC:")

lukuA = float(lukuA_str)
lukuB = float(lukuB_str)
lukuC = float(lukuC_str)

summa = (lukuA+lukuB+lukuC)
keski = summa/3
print(f"summa = {summa}")
print(f"keskiarvo = {keski}")

#float(input("syötä lukuA:")) olisi voinut käyttää
#harjoittelen alle float ja inputin yhdistämistä tein ensimmäiseksi
#ylemmän tekstin

#onko tässä tarvetta merkata muodolla _str?
#se taitaa olla hahmotus sääntö koodin lukemiseen vai?

luku1 = float(input("syötä luku a:"))
luku2 = float(input("syötä luku b:"))
luku3 = float(input("syötä luku c:"))

summa2 = luku1+luku2+luku3
keski2 = summa2/3
print(f"summa on: {summa2}")
print(f"keskiarvo on: {keski2:.2f}")

#muista :.2f desimaalit