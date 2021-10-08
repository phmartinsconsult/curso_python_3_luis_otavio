'''
Combinations, Permutations and Products - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - ordem importa e repete valores únicos
'''

from itertools import combinations
from itertools import permutations
from itertools import product
pessoas = ['Luis', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

# Combinations - A ordem não importa
for grupo in combinations(pessoas, 2):
    print(grupo)

# Permutations - A ordem importa
for grupo in permutations(pessoas, 2):
    print(grupo)

# Product - Pega todas as pessoas, todas as combinações mesmo
for grupo in product(pessoas, repeat=2):
    print(grupo)







