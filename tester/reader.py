from Bio import SeqIO


count = 0
reads = 0

for record in SeqIO.parse(r'C:\Users\USER\Desktop\10xVDJ\1_S2_L003_R1_001.fastq', "fastq"):
    count += 1

    if "tttcttatatggg" in str(record.seq).lower():
        pass