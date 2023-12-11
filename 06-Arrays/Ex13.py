import sys
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["By car", "Public transport", "By bike", "By foot"])
y = np.array([25,19, 32, 7])

plt.bar(x,y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()