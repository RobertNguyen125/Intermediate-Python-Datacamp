import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tail = []
for x in range(1000):
    tail = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tail.append(tail[x] + coin)
    final_tail.append(tail[-1])
plt.hist(final_tail, bins = 10)
plt.show()
