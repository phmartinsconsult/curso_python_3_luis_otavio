'''
SHALLOW COPY - CÓPIA RASA: NÃO É UMA CÓPIA REAL
'''
d1 = {
    1: 'a',
    2:'b',
    3:'c',
    'd':['Luis','Otávio']
}
v=d1.copy()
v[1]='Luis' ## Só altera na cópia
v['d'][0]='João' ## Vai alterar nos dois dicionários
print(d1)
print(v)

'''
CÓPIA REAL
'''
# Módulo: Copy
import copy
v1 = copy.deepcopy(d1)
print(v1)
v1['d'][0]='Paulo' ## Vai alterar apenas em v1
print(v1)














