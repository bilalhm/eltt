
# generate random integer values
from numpy.random import seed
from numpy.random import randint
import pandas as pd
import numpy as np
# seed random number generator
seed(1)
# generate some integers
priority = randint(1, 4, 100)
print(priority)

max_con = randint(0, 50000, 100)
print(max_con)

h=np.random.uniform(low=1.09, high=1.4, size=100).tolist()
print(h)

v=np.random.uniform(low=36.12, high=36.24, size=100).tolist()
print(v)

name=[i for i in range(1,101)]
print(name)

a=pd.DataFrame({'name':name,'v':v ,'h':h,'max_con':max_con,'priority':priority})
print(a)
a.to_csv('D:\\electrique.csv')