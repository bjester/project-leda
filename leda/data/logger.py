#So as to not waste tremendous amounts of memory, do we
#  need to write our data in 512kb blocks because of
#  SD card????


from datetime import datetime
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

    def openLog(self):
        """Start file logging, add header to file"""
        self.currentLog = self.fileName + " " + time.asctime(time.localtime()) + ".csv" # timestamp ensures unique file name each run 
        self.openFile = open(self.currentLog, 'w')
        self.fileHandle = csv.writer(self.openFile)

    def append(self, data, timeStamp):
        """Record data row"""
        if self.fileHandle is not None:
            row = [[time.mktime(timeStamp.timetuple())],
                   [data]]
            self.fileHandle.writerow(row)
        else:
            print("Must call Logger.begin() before Logger.append()")

    def closeLog(self):
        """End logging"""
        if self.fileHandle is not None:
            self.openFile.close()
            self.fileHandle = None
            self.openFile = None

    def decodeLastLog(self):
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
                        stamp = datetime.fromtimestamp(flt)
                    except ValueError:
                        stamp = "Invalid timestamp"
                    line += str(stamp)
                    line += "     "
                    line += row[1][1:-1]
                    print(line)
            finally:
                f.close()


	
#log = Logger("test")
#log.openLog()
#log.append(45, datetime.now())
#log.append(872, datetime.now())
#log.append(6, datetime.now())
#log.closeLog()
#log.decodeLastLog()

