import csv

class Logger():
    """Data logger, writes as CSV"""

    def __init__(self, fileName):
        """Constructor, set file name for logging"""
        self.fileName = None
        self.fileIndex = 0
        self.bites = 0
        self.limit = 1024*1024*1024
        self.fileHandle = None
        self.fileName = fileName
        self.fileHandle = open(self.fileName, 'w')
        self.csvHandle = csv.writer(self.fileHandle)

    def begin(self, header):
        """Start file logging, add header to file"""
        self.csvHandle.writerow(header)
        pass

    def record(self, row):
        """Record data row"""
        # self.bytes += self.csvHandle.writerows(data)
        self.csvHandle.writerows(row)

        # How to get bytes added with each addition? Rotate files, can we use linux util?
        if self.bites > self.limit:
            self.end()
            self.fileIndex += 1
            self.fileName = "%s.%d" % (self.fileName, self.fileIndex)
            self.start()

    def end(self):
        """End logging"""
        if self.fileHandle is not None:
            self.fileHandle.close()
            self.fileHandle = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
