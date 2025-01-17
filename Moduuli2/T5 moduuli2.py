import math


#float input voi kirjoittaa kyseisellä tavoin
leivikset = float(input("leiviksien määrä:"))
naulat = float(input("naulojen määrä:"))
luodit = float(input("luotien määrä:"))
#alla vakiot joissa sääntö että isolla näitä ei yleensä muokkailla
LEI1 = 20 * naulat
NAU1 = 20 * luodit
LUO1 = 13.3

gr = LEI1 * leivikset + NAU1 * naulat + LUO1 * luodit

kg = int(gr / 1000)
gramma = int(gr % 1000)
#int = kokonaisluvut ilman desimal
print(f"Kiloa: {kg}")
print(f"grammaa:{gramma}")
#tehtävä on aika opettajan avuin tehty mutta hyvää hahmotusta sain.
#tein aluksi lyhenteillä esim luo,lei,nau mutta kokonais tekstinä selvempi