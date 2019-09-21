import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.rand(100, 1)
y = np.random.rand(100, 1)
z = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1) + z

print("x" ,x)
print("y ",y)

plt.scatter(x, y , s=10)
plt.show()
