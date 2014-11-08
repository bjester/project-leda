import csv

class Logger():
    """Data logger, writes as CSV"""
    fileName = None
    fileIndex = 0
    bytes = 0
    limit = 1024*1024*1024
    fileHandle = None

    def __init__(self, fileName):
        """Constructor, set file name for logging"""
        self.fileName = fileName

    def begin(self, header):
        """Start file logging, add header to file"""
        self.bytes = 0
        self.fileHandle = open(self.fileName, 'w', newline='')

        self.csvHandle = csv.writer(self.fileHandle)
        self.csvHandle.writerow(header)

    def record(self, row):
        """Record data row"""
        # self.bytes += self.csvHandle.writerows(data)
        self.csvHandle.writerows(row)

        # How to get bytes added with each addition? Rotate files, can we use linux util?
        if self.bytes > self.limit:
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
