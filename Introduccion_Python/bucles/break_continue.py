"""
break y continue
"""

# break -> para cuando el rango llega a 5, pero excluye el 5
for n in range(11):
    if n == 5:
        break
    print(n)

print("\n")

# continue -> continua el rango pero excluye el 5 
for n in range(11):
    if n == 5:
        continue
    print(n)