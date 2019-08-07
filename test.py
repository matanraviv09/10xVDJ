import time
import numpy as np

t = 0
val = 100
arr = []
for o in range(int(input('number: '))):
    t = time.time()

    for i in range(val):
        for j in range(val):
            for k in range(val):
                np.sin(i*j/(k + 1))
    arr.append(time.time() - t)
    print("Test Result: " + str(arr[o]) + " seconds")

print("avg = " + str(np.average(arr)) + " seconds")
input()
