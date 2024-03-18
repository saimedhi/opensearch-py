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
    def request_start(self) -> None:
        pass

    @abstractmethod
    def request_end(self) -> None:
        pass


class MetricsEvents(Metrics):
    def __init__(self) -> None:
        self.events = Events()
        self.service_time = 0.0

        # Subscribe to the request_start and request_end events
        self.events.request_start += self._on_request_start
        self.events.request_end += self._on_request_end

    def request_start(self) -> None:
        self.events.request_start()

    def _on_request_start(self) -> None:
        self.start_time = time.perf_counter()

    def request_end(self) -> None:
        self.events.request_end()

    def _on_request_end(self) -> None:
        self.end_time = time.perf_counter()
        self.service_time = self.end_time - self.start_time
