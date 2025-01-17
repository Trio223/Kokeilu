import math

#import math aina matikka hommiin

#str = string eli merkkijono eli vihreä teksti sulkujen sisällä
#merkkijonot voivat olla joko vakioita (kiinteitä tekstejä)
#joihin voi kirjoittaa tekstiä ohjelman aikana

#input = ohjelma esim kysyy ohjelman aikana jotakin esim syötä nro
säde_str = input("syötä ympyrän säde")

#float=liukuluku ilmoittaa desimaalien tarkkuudella
säde = float(säde_str)

#potenssin merkki on **

pinta_ala = math.pi * säde**2

print ("pinta ala on", pinta_ala)
#.2f desimaalit 2 tarkkuudella mutta en tajua miten sen saisi tähän

#yllä ihan ensimmäinen yritys koitetaas laadukkaammin

säde2_str = float(input("Syötä ympyrän säde:"))

pinta_ala2 = math.pi * säde2_str**2

print(f"ympyrän pinta ala on: {pinta_ala2:.2f}")