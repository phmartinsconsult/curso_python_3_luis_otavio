import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r
g = gera()

for v in g:
    print(v)

print('#' *80)




def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
for v in g:
    print(v)
