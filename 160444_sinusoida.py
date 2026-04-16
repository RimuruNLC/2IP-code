import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5, 100)
x = np.sin(x)
x*=100
list1 = []
for i in range(len(x)):
    for _ in range(int(x[i])):
        list1.append(i)
print(list1)
plt.hist(list1, bins=len(x))
plt.grid()
plt.show()
