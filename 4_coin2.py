import numpy as np
np.random.seed(123)
tail = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tail.append(tail[x] + coin)
print(tail)

#the result is how often tail is rolled (the last item of the list)
