
def gera():
    for n in range(100):
        r = []
        a = n + 0.97
        #b = a + 0.89
        r.append(a)
        for i in r:
            if i % 2 == 0:
                print(f'O número {a:.2f} é par')
            else:
                print(f'O número {a:.2f} é impar.')
        print(r)
gera()




