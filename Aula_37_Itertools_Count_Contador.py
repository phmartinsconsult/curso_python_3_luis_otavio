'''
Count - Itertools
'''

from itertools import count

contador = count()
for v in contador:
    print(v)

    if v >=11:
        break
print()
contador = count(start=8, step=0.1)
for v in contador:
    print(round(v, 2))

    if v >=11:
        break
print()
print()
contador = count(start=5, step=-0.1)
for v in contador:
    print(round(v, 2))

    if v >=11 or v<=3:
        break








