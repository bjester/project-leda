import csv

class Logger():
    """Data logger, writes as CSV"""

    def __init__(self, fileName):
        """Constructor, set file name for logging"""
        self.fileName = fileName
        self.fileHandle = None

    def begin(self, header):
        """Start file logging, add header to file"""
        self.fileHandle = open(self.fileName, 'wb')

    def append(self, data):
        """Record data row"""
        self.fileHandle.write(data)

    def end(self):
        """End logging"""
        if self.fileHandle is not None:
            self.fileHandle.close()
            self.fileHandle = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
	
