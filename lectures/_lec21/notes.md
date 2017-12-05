
lec16 ending material redux:
mandelbrot.ipynb


if more time:

How do you tell how long your code takes to run?

import time
start = time.time()
myFunc()
end = time.time()
print(str(end-start), " s elapsed.")


linting
pep8/autopep8  # check perms on install


##  SCIPY

import scipy as sp
from scipy.special import j0
x = np.linspace(0,10,101)
y = j0(x)
plt.plot(x,y)
plt.show()


use tests to motivate your new functions

Next week's lab will be built around this idea of arbitrary functions built to certain unit test requirements.  The homework could also be made easier by writing unit tests from Ryan's specifications that your code then needs to pass.
