from datetime import datetime
import time


class Logger:
    """Debug logger"""

    def __init__(self, path, do_write):
        """Constructor, set file name for logging"""
        self.path = path
        self.currentLog = None
        self.openFile = None
        self.do_write = do_write

    def open(self):
        """Start file logging, add header to file"""
        self.currentLog = self.path + "/debug.log"
        self.openFile = open(self.currentLog, 'a', 1)  # line buffered file

    def write(self, data):
        """Record data row"""

        if not self.do_write:
            return

        timestamp = time.time()
        if self.openFile is not None:
            row = "[" + datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + "] " + data
            self.openFile.write(row + "\n")
            print(row)

    def close(self):
        """End logging"""
        if self.openFile is not None:
            self.openFile.close()
            self.openFile = None

