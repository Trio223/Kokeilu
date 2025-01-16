import math
#float input voi kirjoittaa kyseisellä tavoin
lei = float(input("leiviksien määrä:"))
nau = float(input("naulojen määrä:"))
luo = float(input("luotien määrä:"))
#alla vakiot joissa sääntö että isolla näitä ei yleensä muokkailla
LEI1 = 20 * nau
NAU1 = 20 * luo
LUO1 = 13.3

gr = LEI1 * lei + NAU1*nau + LUO1 * luo

kg = int(gr / 1000)
gramma = int(gr % 1000)
#int = kokonaisluvut ilman desimal
print(f"Kiloa: {kg}")
print(f"grammaa:{gramma}")
#tehtävä on aika opettajan avuin tehty mutta hyvää hahmotusta sain.