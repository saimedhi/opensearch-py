# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
print("\n\n test_print............. 172")
from unittest import TestCase

from opensearchpy import OpenSearch
from opensearchpy.helpers.test import OPENSEARCH_URL


class TestSecurity(TestCase):
    print("\n\n test_print............. 173")
    def test_security(self):
        client = OpenSearch(
            OPENSEARCH_URL,
            http_auth=("admin", "admin"),
            verify_certs=False,
        )

        info = client.info()
        self.assertNotEqual(info["version"]["number"], "")
        self.assertNotEqual(info["tagline"], "")
        self.assertTrue(
            "build_flavor" in info["version"] or "distribution" in info["version"]
        )
