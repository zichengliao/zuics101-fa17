import numpy as np
def myrand():
    return np.random.rand(1,1)[0][0]

samples = 1000000
count = 0
for i in range(samples):
    x, y = myrand(), myrand()
    if ((x-0.5)**2 + (y-0.5)**2)**0.5 < 0.5:
        count += 1
PI = count/samples*4
print('Pi = %f'%PI)
