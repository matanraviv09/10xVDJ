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
a = ['GGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATAC', 'ATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTG', 'CCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGAC', 'GAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGC', 'TCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCAC', 'TTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTT', 'CCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCAACTGATGTGGACATGAATTTTTGAGACT', 'CTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACA', 'ATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACCT', 'GGATAGCAGTTATATTGCTGACAGAAATACTCTGCCAAGTCTTCAGACTGCACATTGCTGATGGTGAGAGTG', 'TCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCT', 'TTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGT', 'GGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTAC', 'CATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATT', 'AGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACA', 'CGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTG', 'ATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACCT', 'GTGAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAA', 'GTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGA', 'CTTCAGACTGCACATTGCTGATGGTGAGAGTGAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGA', 'ACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTG', 'GAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAAT', 'GACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCA', 'GGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACG', 'CTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGG', 'CTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACCTGAGTCTGTGA', 'CGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTG', 'TGAGTCTGTGACTCCATCTTGATGCCCATGCTGATCTGATGTATTTCCCCATATAAGAAAGAATATTCTGCC', 'TACTCTGCCAAGTCTTCAGACTGCACATTGCTGATGGTGAGAGTGAAATCTGTCCCAGATCCACTGCCTGTG', 'GATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATG', 'GCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCC', 'TGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTC', 'AAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGG', 'GCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCC', 'CTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACA', 'ACCACAGCAACATGTATACAAAGACCTGAGTCTGTGACTCCATCTTGATGCCCATGCTGATCTGATGTATTT', 'ACTGCACATTGCTGATGGTGAGAGTGAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCAC', 'GATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTT', 'TTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTC', 'TGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAA', 'GATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTG', 'GATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATG', 'AGGAGATTGCCGTGGGTTCTGTTGATACCAGGCTACAATAGTACCCACATTCAGACTGGCCTTGCAGGTGAC', 'CCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTT', 'CCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAA', 'GGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTAC', 'GATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTT', 'TGAGAGTGAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCG', 'GCGACGGGTGTGGGCAAGAAATTTTTTGACTGGGGGATAACAAAGTGTGCAAAAAAACCCCAAAACCACAGC', 'GCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCC', 'AGGTGGATGGGTGGCAGAAGCCACAACCATACATTCCCAGGTCTGGGTGGGAGACCCAAAGACCTGAGTCTG', 'GAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAAT', 'TCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGA', 'CACACTCACTTGTCGCTCAAGTACTGGGGCTGTTACAACTGGTAACTATGCCAACTGGGTCCAAGAAAAACC', 'CCAGCCAACCACAGCAACATGTATACAAAGACCTGAGTCTGTGACTCCATCTTGATGCCCATGCTGATCTGA', 'CCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGA', 'GACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGA', 'AGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGATTGGCCTTG', 'GCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCC', 'GAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGAC', 'CTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGA', 'CCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCT', 'ACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGAC', 'GATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTT', 'TGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTTGAGACTGGGTCATCACAATGTCT', 'TTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTG', 'CCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGA', 'GAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTACTTTAGGAGATTGCCCTGGTTT', 'TGACAGAAATACTCTGCCAAGTCTTCAGACTGCACATTGCTGATGGTGAGAGTGAAATCTGTCCCAGATCCA', 'GTGAGAGTGAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCC', 'GTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACCTGAGTCTGTGACTCC', 'GGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACG', 'GCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCC', 'GTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCA', 'GTGGGAAGATGGATACAGTTGGTGCAGCATCAGCCCGTTTTATTTCCAGCTTGGTCCCCCCTCCGAACGTGT', 'CCTGGTATCAACAGAAACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTAACCCTG', 'TGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATA', 'GACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAAC', 'TCCGCGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCT', 'TAGGAGATTGCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGA', 'GCCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCC', 'CAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAG', 'CAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCA', 'CCCTGGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCT', 'TGAATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGA', 'GTGAAGCGATCAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGT', 'TCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGATACCAGGC', 'CAGGGACTCCACTGTACCGGTAGGATGCCGAGTAAATCAGTGCTTTAGGAGATTGCCCTGGTTTCTGTTGAT', 'ATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGT', 'AATTTTTGAGACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACC', 'GACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCA', 'GGTTTCTGTTGATACCAGGCTACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCT', 'TACATTAGTACCCACATTCTGACTGGCCTTGCAGGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAA', 'GGTGACGCTGACCCTGTCTCCTACTGATGTGGACATGAATTTTTGAGACTGGGTCATCACAATGTCTCCATA', 'CACATTGCTGATGGTGAGAGTGAAATCTGTCCCAGATCCACTGCCTGTGAAGCGATCAGGGACTCCACTGTA', 'CATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACCTGAGTCTGTGACTCCAT', 'TAGTCTTCAGACTGCACATTGCTGATGGTGAGAGTGAAATATGTCCCAGATCCACTGCCTGTGAAGCGATCA', 'ACTGGGTCATCACAATGTCTCCATCAACACCAGACAACCACAGCAACATGTATACAAAGACCTGAGTCTGTG']
i = 1
for j in a:
    print('>' + str(i))
    i += 1
    print(j)

