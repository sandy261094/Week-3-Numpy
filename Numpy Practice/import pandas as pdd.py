import pandas as pd
import numpy as np
a1 = np.array([1,2,3])
a2 = np.array([
      [4,5,6],
      [7,8,9],
      [10,11,12]])
print(a2 ** 2)
print(np.square(a1))
print(np.log(a2))

import numpy as np 
a6 = np.array([
    [[10,20,30],
     [40,50,60],
     [70,80,90]],
               
    [[100,200,300],
     [400,500,600],
     [700,800,900]]
     ])

np.random.seed(0)
a7 = np.random.randint(10, size = (2,3,3))
#print(a6)
#print(a7)
#print(np.dot(a6, a7))
#print(a6.shape)
#print(a7)
a7_trans = a7.T
#print(a7_trans)
print(np.dot(a6, a7_trans))


import numpy as np
import matplotlib.pyplot as plt
a2 = np.array([
      [4,5,6],
      [7,8,9],
      [10,11,12]])
plt.hist(a2)
plt.show()


import numpy as np 
a4 = np.array([
    [[10,20,30],
     [40,50,60],
     [70,80,90]],
               
    [[100,200,300],
     [400,500,600],
     [700,800,900]]
     ])

a5 = np.array([
    [4,5,6],
    [7,8,9]
    ])
a5_reshape = a5.reshape(2,3,1)
print(a5_reshape)
print(a4)
print(a5)

a5_reshape = a5.reshape(2,3,1)
print(a5_reshape)
print(a5)

print(a4 + a5_reshape)

import numpy as np
massive_array = np.random.random(100000)
print(massive_array[:100000])
print(massive_array[:500])
summ = np.sum(massive_array)
summm = sum(massive_array)
print(summ)
print(summm)