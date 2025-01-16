import math
#float input voi kirjoittaa kyseisellä tavoin
lei = float(input("leiviksien määrä:"))
nau = float(input("naulojen määrä:"))
luo = float(input("luotien määrä:"))
#alla vakiot
lei1 = 20 * nau
nau1 = 20 * luo
luo1 = 13.3

gr = lei1 * lei + nau1*nau + luo1 * luo

kg = int(gr / 1000)
gramma = int(gr % 1000)
#int = kokonaisluvut ilman desimal
print(f"Kiloa: {kg}")
print(f"grammaa:{gramma}")