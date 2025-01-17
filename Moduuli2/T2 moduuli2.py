import math

#import math aina matikka hommiin

#str = string eli merkkijono
#merkkijonot voivat olla joko vakioita (kiinteitä tekstejä) tai
#muuttujia, joihin voi tallentaa tekstiä ohjelman aikana

#input = ohjelma esim kysyy ohjelman aikana jotakin esim syötä nro
säde_str = input("syötä ympyrän säde")

#float=liukuluku ilmoittaa desimaalien tarkkuudella
säde = float(säde_str)

#potenssin merkki on **

pinta_ala = math.pi * säde**2

print ("pinta ala on", pinta_ala)
#.2f desimaalit 2 tarkkuudella mutta en tajua miten sen saisi tähän