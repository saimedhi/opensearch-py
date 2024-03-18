# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.


import time
from abc import ABC, abstractmethod 
from events import Events

class Metrics(ABC):      
    @abstractmethod
    def request_start(self):
       pass

    @abstractmethod
    def request_end(self):
       pass

       
class MetricsEvents(Metrics):
    def __init__(self) -> None:
        self.events = Events()
        current_time = time.perf_counter()
        self.start_time = current_time
        self.end_time = current_time
        self.service_time = 0.0

        # Subscribe to the server_request_start and server_request_end events
        self.events.request_event_start += self.request_event_start
        self.events.request_event_end += self.request_event_end

    def request_start(self) -> None:
        self.events.request_event_start()

    def request_event_start(self) -> None:
        self.start_time = time.perf_counter()

    def request_end(self) -> None:
        self.events.request_event_end()

    def request_event_end(self) -> None:
        self.end_time = time.perf_counter()
        self.service_time = self.end_time - self.start_time

