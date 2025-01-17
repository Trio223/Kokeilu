import math


#float input voi kirjoittaa kyseisellä tavoin

leivikset = float(input("leiviksien määrä:"))
naulat = float(input("naulojen määrä:"))
luodit = float(input("luotien määrä:"))

#alla vakiot joissa sääntö että isolla näitä ei yleensä muokkailla
#kun luetaan koodia

LEI1 = 20 * naulat
NAU1 = 20 * luodit
LUO1 = 13.3

gr = LEI1 * leivikset + NAU1 * naulat + LUO1 * luodit

kg = int(gr / 1000)
gramma = int(gr % 1000)

#int = kokonaisluvut ilman desimaalia
# %  modulo eli tässä tilanteessa kilojen ylijäämä esim kg ei ilmoita grammoja
#niin monta kertaa 1000 menee vaikka 1200 joten 1kg ja 200 gramma


print(f"Kiloa: {kg}")
print(f"grammaa:{gramma}")

#tehtävä on aika opettajan avuin tehty mutta hyvää hahmotusta sain.
#tein aluksi lyhenteillä esim luo,lei,nau mutta kokonais tekstinä selvempi
#tein muita tehtäviä uudelleen näiden vinkkien avuin, kiitos