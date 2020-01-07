import numpy as np
np.random.seed(123)
outcome = []
for x in range(10):
    coin = np.random.randint(0,2)
    print(coin)
    if coin == 0:
        print('head')
        outcome.append('head')
    else:
        print('tail')
        outcome.append('tail')
print(outcome)
