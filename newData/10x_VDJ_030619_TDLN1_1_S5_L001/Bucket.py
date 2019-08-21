class Bucket(object):
    def __init__(self, barcode):
        self.barcode = barcode
        self.start = ""
        self.ends = []

    def add(self, end):
        self.ends.append(end)


    def __str__(self):
        return str(self.ends)
