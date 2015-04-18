
class CaptureImage:

    def __init__(self, msg):
        self.msg = msg

    def trigger(self):
        print self.msg
