# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from abc import ABC, abstractmethod


class Metrics(ABC):
    @abstractmethod
    def request_start(self) -> None:
        pass

    @abstractmethod
    def request_end(self) -> None:
        pass

    @property
    @abstractmethod
    def start_time(self) -> float:
        pass

    @property
    def end_time(self) -> float:
        pass

    @property
    @abstractmethod
    def service_time(self) -> float:
        pass
