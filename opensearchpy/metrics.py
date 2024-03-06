# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.


import time

from events import Events


class TimeMetrics:
    def __init__(self) -> None:
        self.events = Events()
        self.start_time = None
        self.end_time = None
        self.service_time = 0

        # Subscribe to the server_request_start and server_request_end events
        self.events.server_request_start += self.server_request_start
        self.events.server_request_end += self.server_request_end

    def server_request_start(self) -> None:
        self.start_time = time.perf_counter()

    def server_request_end(self) -> None:
        self.end_time = time.perf_counter()
        self.service_time = self.end_time - self.start_time
