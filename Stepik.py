from random import *

n = sample([str(i).ljust(3) for i in range(1, 76)], 25)
n[12] = str('0  ')
for _ in range(5):
    x = ' '.join(n[0:5])
    print(x)
    del n[0:5]


