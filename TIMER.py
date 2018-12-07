
import timeit
setup = """

from homework2 import quickSort
from homework2 import mergeSort


import random
lst = random.sample(range(50), 10)
lst1 = random.sample(range(500), 100)
lst2 = random.sample(range(5000), 1000)
lst3 = random.sample(range(50000), 10000)
"""

t=timeit.Timer('quickSort(lst)', setup = setup)
t1=timeit.Timer('quickSort(lst1)', setup = setup)
t2=timeit.Timer('quickSort(lst2)', setup = setup)
t3=timeit.Timer('quickSort(lst3)', setup = setup)
t4=timeit.Timer('mergeSort(lst)', setup = setup)
t5=timeit.Timer('mergeSort(lst1)', setup = setup)
t6=timeit.Timer('mergeSort(lst2)', setup = setup)
t7=timeit.Timer('mergeSort(lst3)', setup = setup)
print('quickSort time:',t.timeit(5))
print('quickSort time:',t1.timeit(5))
print('quickSort time:',t2.timeit(5))
print('quickSort time:',t3.timeit(5))
print('mergeSort time:',t4.timeit(5))
print('mergeSort time:',t5.timeit(5))
print('mergeSort time:',t6.timeit(5))
print('mergeSort time:',t7.timeit(5))


import matplotlib.pyplot as plt

plt.plot([0.0001781684488641163, 0.0020487661749422695,  0.03294748408025583, 0.4855480081895931], 'b-^', label='quicksort')
plt.plot([ 0.00026400392038983256,  0.004112579205450828, 0.06228030308470789, 0.7884880611750431], 'r-*', label= 'mergesort')
plt.xlabel('t, t1, t2, t3, t4, t5, t6, t7')
plt.ylabel('time')
plt.legend()
plt.show()



