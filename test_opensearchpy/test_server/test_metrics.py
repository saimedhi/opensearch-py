# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from __future__ import unicode_literals

from opensearchpy.metrics.metrics_events import MetricsEvents

from . import OpenSearchTestCase, get_client


class Metrics(OpenSearchTestCase):
    def test_metrics(self) -> None:
        metrics = MetricsEvents()
        client = get_client(metrics=metrics)
        index_name = "test-index"
        index_body = {"settings": {"index": {"number_of_shards": 4}}}
        client.indices.create(index_name, body=index_body)
        print("metrics.service_time", metrics.service_time)
        assert 1 == 2
