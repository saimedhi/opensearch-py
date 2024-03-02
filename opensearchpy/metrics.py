import time
from events import Events

class TimeMetrics:
    def __init__(self):
        self.events = Events()
        self.start_time = 0
        self.end_time = 0
        self.service_time = 0


        # Subscribe to the request_start and request_end events
        self.events.request_start += self.server_request_start
        self.events.request_end += self.server_request_end

    def server_request_start(self):
        print("KKKKK")
        self.start_time = time.time()

    def server_request_end(self):
        print("MMMMMMM")
        self.end_time = time.time()
        self.service_time = self.end_time - self.start_time