import numpy as np
def myrand():
    return np.random.rand(1,1)[0][0]

samples = int(input('number of samples: ')) 
count = 0
for i in range(samples):
    x, y = myrand(), myrand()
    if (x**2 + y**2)**0.5 < 1:
        count += 1
PI = count/samples*4
print('Pi = %f'%PI)
