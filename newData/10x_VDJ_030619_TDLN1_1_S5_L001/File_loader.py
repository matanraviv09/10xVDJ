class Bucket(object):
    def __init__(self, barcode):
        self.barcode = barcode
        self.start = ""
        self.ends = []

    def add(self, end):
        self.ends.append(end)


    def __str__(self):
        return str(self.ends)

def rem_until(str, char):
    i = 0
    for c in str:
        if c == char:
            return str[i:]

def load_file(dir:str):
    with open(dir) as file:
        b = file.read().split(' barcode: ')[1:]
        b[0] = '0\n' + b[0]
        buckets = []
        for bucket in b:
            app = Bucket(bucket.split('\n')[0])
            ends = bucket.split('Bucket: [')[1].split(",")

            for end in ends:
                end.strip("'")
                print(end)

                buckets.append(app)



        return buckets


c = 0
for i in load_file('Dump1-.txt'):
    c += 1
    print(i)
    if c == 3: break

