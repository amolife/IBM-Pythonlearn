import numpy as np
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2

x = np.arange(-11, 11)
y = x ** 2 + 2 * x + 1
plt1.title("Matplotlib demo123")
plt1.xlabel("x axis caption")
plt1.ylabel("y axis caption")
plt1.plot(x, y,'--')
plt1.show()

