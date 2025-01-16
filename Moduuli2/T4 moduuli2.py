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