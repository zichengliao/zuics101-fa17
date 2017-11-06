import numpy as np
W = 250
C = 250
print('Day 0: %i for Western food, %i for Chinese foot'%(W,C))

for day in range(1,31):
    nextW, nextC = W, C
    for i in range(W):
        if np.random.randint(10) < 3:
            nextW -= 1
            nextC += 1
    for i in range(C):
        if np.random.randint(10) < 2:
            nextW += 1
            nextC -= 1
    W, C = nextW, nextC
    print('Day %i: %i for Western food, %i for Chinese foot'%(day, W,C))
