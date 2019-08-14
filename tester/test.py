# import time
# import numpy as np
# import Bio
#
# t = 0
# val = 1000
# arr = []
# for o in range(int(input('number: '))):
#     t = time.time()
#
#     for i in range(val):
#         for j in range(val):
#             for k in range(val):
#                 np.sin(i*j/(k + 1))
#     arr.append(time.time() - t)
#     print("Test Result: " + str(arr[o]) + " seconds")
#
# print("avg = " + str(np.average(arr)) + " seconds")
# input()

import time
save_num = 0
with open("Dump" + str(sa)ve_num) + '.txt', 'w') as dump:
    dump.write('a'