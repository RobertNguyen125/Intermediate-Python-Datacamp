import numpy as np
np.random.seed(123)
#print(np.random.rand())
step = 50
#because rand(),seed(),randint() belong to random packagke

dice = np.random.randint(1,7)

if dice <= 2:
    step = step -1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)

print(dice)
print(step)
