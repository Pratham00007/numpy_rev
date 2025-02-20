import numpy as np
# -and + close to 0
arr=np.random.randn(5)
print(arr)
# 0 to 1 but 0 and 1 excluded total 4 no
arr= np.random.ranf(4)
print(arr)
# 5 min to 20 max total 5 no 
arr=np.random.randint(5,20,5)
print(arr)