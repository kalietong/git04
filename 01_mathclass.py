
import math
import sys

numbers= []
i = 0

for argv in sys.argv:
    numbers.append(sys.argv[i])
    i = i + 1

del numbers[0]

for x in range(0, len(numbers)):
        numbers[x] = int(numbers[x])

print(min(numbers))
print(max(numbers))
print(max(numbers) - min(numbers))
