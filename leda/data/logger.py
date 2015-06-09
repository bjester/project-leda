#So as to not waste tremendous amounts of memory, do we
#  need to write our data in 512kb blocks because of
#  SD card????


import datetime
import time
import csv

class Logger():
    """Data logger, writes as CSV"""

    def __init__(self, fileName):
        """Constructor, set file name for logging"""
        self.fileName = fileName
        self.currentLog = None
        self.openFile = None #required by close()
        self.fileHandle = None #csv file

    def __enter__(self):
        """Start file logging, add header to file"""
        self.currentLog = self.fileName + " " + time.asctime(time.localtime()) + ".csv" # timestamp ensures unique file name each run 
        self.openFile = open(self.currentLog, 'w')
        self.fileHandle = csv.writer(self.openFile)

    def append(self, data):
        """Record data row"""
        if self.fileHandle is not None:
            now = datetime.datetime.now()
            row = [[time.mktime(now.timetuple())],
                   [data]]
            self.fileHandle.writerow(row)
        else:
            print("Must call Logger.begin() before Logger.append()")

    def closeLog(self):
        """End logging"""
        print("__exit__ was called")
        if self.fileHandle is not None:
            self.openFile.close()
            self.fileHandle = None
            self.openFile = None

    def __exit__(self):
        """Demonstration of (basic) decoding of log file"""
        if self.currentLog is not None:
            f = open(self.currentLog, 'r')
            try:
                reader = csv.reader(f)
                lineCount = 1
                for row in reader:
                    line = ""
                    try:
                        flt = float(row[0][1:-1])
                        stamp = datetime.datetime.fromtimestamp(flt)
                    except ValueError:
                        stamp = "Invalid timestamp"
                    line += str(stamp)
                    line += "     "
                    line += row[1][1:-1]
                    print(line)
            finally:
                f.close()


	
#log = Logger("test")
#log.__enter__()
#log.append(45)
#log.append(872)
#log.append(6)
#log.__exit__()
#log.printLog()

