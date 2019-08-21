from Bio.SeqIO.QualityIO import FastqGeneralIterator
from zipfile import ZipFile
from File_loader import *
import datetime

def add_end(i, dir="10x_VDJ_030619_TDLN1_1_S5_L001_R2_001.fastq"):
    ind = 0
    for title, seq, qual in FastqGeneralIterator(open(dir)):
        ind += 1
        if ind == i:
            return seq


def save_dump(dir, buckets, index, unq_bar):
    with open(dir, 'w') as f:
        print('Number of reads: %i', index)
        f.write('Number of reads: ' + str(index) + '\n')

        print('Buckets: %i', len(buckets))
        f.write('Buckets: ' + str(len(buckets)) + '\n')

        print('Unique Barcodes: %i', len(set(unq_bar)))
        f.write('Unique Barcodes: ' + str(len(set(unq_bar))) + '\n')

        print(buckets)
        for num, i in enumerate(buckets):
            f.writelines('\n' + str(num) + " barcode: " + i + "\n Bucket: " + str(buckets[i]))

        umi_num = []
        for l, i in enumerate(buckets):
            print(i + str(len(buckets[i].ends)))
            f.write(i + str(len(buckets[i].ends)))

            if buckets[i].start[16:26] not in umi_num:
                umi_num.append(buckets[i].start[16:26])

            print(str(l) + str(len(umi_num)))
            f.write(str(l) + str(len(umi_num)))
            umi_num = []

        print('UMI_num: ' + str(len(umi_num)))
        f.write('UMI_num: ' + str(len(umi_num)))


index = 0
buckets = {}
unq_bar = []

save_num = 1
with open("10x_VDJ_030619_TDLN1_1_S5_L001_R1_001.fastq") as in_handle:
    for title, seq, qual in FastqGeneralIterator(in_handle):
        index += 1
        bar = seq[:16] + seq[25:]
        unq_bar.append(bar[:16])
        if bar not in buckets:
            buckets[bar] = Bucket(bar)
            if buckets[bar].start == "":
                buckets[bar].start = seq

        buckets[bar].ends.append(add_end(index))

        if index % 10000 == 0:
            save_dump("Dump" + str(save_num) + '-' + '.txt', buckets, index, unq_bar)
            save_num += 1

save_dump('save.txt', buckets, index, unq_bar)
