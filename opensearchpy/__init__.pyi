# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import sys
from typing import Tuple

from . import connections as connections
from .aggs import A as A
from .analysis import Analyzer, CharFilter, Normalizer, TokenFilter, Tokenizer
from .client import OpenSearch as OpenSearch
from .connection import AsyncHttpConnection as AsyncHttpConnection
from .connection import Connection as Connection
from .connection import RequestsHttpConnection as RequestsHttpConnection
from .connection import Urllib3HttpConnection as Urllib3HttpConnection
from .connection_pool import ConnectionPool as ConnectionPool
from .connection_pool import ConnectionSelector as ConnectionSelector
from .connection_pool import RoundRobinSelector as RoundRobinSelector
from .document import Document as Document
from .document import InnerDoc as InnerDoc
from .document import MetaField as MetaField
from .exceptions import AuthenticationException as AuthenticationException
from .exceptions import AuthorizationException as AuthorizationException
from .exceptions import ConflictError as ConflictError
from .exceptions import ConnectionError as ConnectionError
from .exceptions import ConnectionTimeout as ConnectionTimeout
from .exceptions import IllegalOperation as IllegalOperation
from .exceptions import ImproperlyConfigured as ImproperlyConfigured
from .exceptions import NotFoundError as NotFoundError
from .exceptions import OpenSearchDeprecationWarning as OpenSearchDeprecationWarning
from .exceptions import OpenSearchDslException as OpenSearchDslException
from .exceptions import OpenSearchException as OpenSearchException
from .exceptions import OpenSearchWarning as OpenSearchWarning
from .exceptions import RequestError as RequestError
from .exceptions import SerializationError as SerializationError
from .exceptions import SSLError as SSLError
from .exceptions import TransportError as TransportError
from .exceptions import UnknownDslObject as UnknownDslObject
from .exceptions import ValidationException as ValidationException
from .faceted_search import DateHistogramFacet as DateHistogramFacet
from .faceted_search import Facet as Facet
from .faceted_search import FacetedResponse as FacetedResponse
from .faceted_search import FacetedSearch as FacetedSearch
from .faceted_search import HistogramFacet as HistogramFacet
from .faceted_search import NestedFacet as NestedFacet
from .faceted_search import RangeFacet as RangeFacet
from .faceted_search import TermsFacet as TermsFacet
from .field import Binary as Binary
from .field import Boolean as Boolean
from .field import Byte as Byte
from .field import Completion as Completion
from .field import CustomField as CustomField
from .field import Date as Date
from .field import DateRange as DateRange
from .field import DenseVector as DenseVector
from .field import Double as Double
from .field import DoubleRange as DoubleRange
from .field import Field as Field
from .field import Float as Float
from .field import FloatRange as FloatRange
from .field import GeoPoint as GeoPoint
from .field import GeoShape as GeoShape
from .field import HalfFloat as HalfFloat
from .field import Integer as Integer
from .field import IntegerRange as IntegerRange
from .field import Ip as Ip
from .field import IpRange as IpRange
from .field import Join as Join
from .field import Keyword as Keyword
from .field import Long as Long
from .field import LongRange as LongRange
from .field import Murmur3 as Murmur3
from .field import Nested as Nested
from .field import Object as Object
from .field import Percolator as Percolator
from .field import RangeField as RangeField
from .field import RankFeature as RankFeature
from .field import RankFeatures as RankFeatures
from .field import ScaledFloat as ScaledFloat
from .field import SearchAsYouType as SearchAsYouType
from .field import Short as Short
from .field import SparseVector as SparseVector
from .field import Text as Text
from .field import TokenCount as TokenCount
from .field import construct_field as construct_field
from .function import SF as SF
from .index import Index as Index
from .index import IndexTemplate as IndexTemplate
from .mapping import Mapping as Mapping
from .query import Q as Q
from .search import MultiSearch as MultiSearch
from .search import Search as Search
from .serializer import JSONSerializer as JSONSerializer
from .transport import Transport as Transport
from .update_by_query import UpdateByQuery as UpdateByQuery
from .utils import AttrDict as AttrDict
from .utils import AttrList as AttrList
from .utils import DslBase as DslBase
from .wrappers import Range as Range

try:
    if sys.version_info < (3, 6):
        raise ImportError

    from ._async.client import AsyncOpenSearch as AsyncOpenSearch
    from ._async.http_aiohttp import AIOHttpConnection as AIOHttpConnection
    from ._async.http_aiohttp import AsyncConnection as AsyncConnection
    from ._async.transport import AsyncTransport as AsyncTransport
    from .helpers import AWSV4SignerAsyncAuth as AWSV4SignerAsyncAuth
    from .helpers import AWSV4SignerAuth as AWSV4SignerAuth
except (ImportError, SyntaxError):
    pass

VERSION: Tuple[int, int, int]
__version__: Tuple[int, int, int]
__versionstr__: str
