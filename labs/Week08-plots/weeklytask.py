#displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 4))
ypoints = xpoints
ypoints = xpoints * xpoints
ypoints = xpoints * xpoints * xpoints

plt.plot(xpoints, ypoints, label='f')
plt.plot(xpoints, ypoints, label ='g')
plt.plot(xpoints, ypoints, label ='h')
plt.show()