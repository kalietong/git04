
import math
import sys

i = 0
a_numbers= []

for argv in sys.argv:
   a_numbers.append(sys.argv[i])
   i = i + 1

del a_numbers[0]

for x in range(0, len(a_numbers)):
        a_numbers[x] = int(a_numbers[x])
Sum = sum(a_numbers)

a_numbers.sort()
n = len(a_numbers)

if n % 2 == 0:
    m1 = a_numbers[n//2]
    m2 = a_numbers[n//2 -1]
    m = (m1 +m2) /2

else:
    m = a_numbers[n//2]
print("Median:" ,str(m))

print("mean:" , Sum/len(a_numbers))

print("Min:" ,min(a_numbers))

print("Max:" ,max(a_numbers))

print("Range:", max(a_numbers) - min(a_numbers))

from collections import Counter
data = Counter(a_numbers)
get_mode = dict(data)
mode = [ k for k, v in get_mode.items () if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: "+ ', '.join(map(str, mode))
print( get_mode)




3import statistics
3for argv in sys.argv:
   a_numbers.append(sys.argv[i])
    i = i+1


