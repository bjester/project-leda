from datetime import datetime
import time
import csv


class Logger():
    """Data logger, writes as CSV"""

    def __init__(self, path):
        """Constructor, set file name for logging"""
        self.path = path
        self.currentLog = None
        self.openFile = None 

    def open(self):
        """Start file logging, add header to file"""
        self.currentLog = self.path + "/rawdata.csv"
        self.openFile = open(self.currentLog, 'w', 1)  # line buffered file

    def append(self, data, timeStamp):
        """Record data row"""
        if self.openFile is not None:
            row = datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S') + "," + data
            self.openFile.write(row)
        else:
            print("Must call Logger.open() before Logger.append()")

    def close(self):
        """End logging"""
        if self.openFile is not None:
            self.openFile.close()
            self.openFile = None

