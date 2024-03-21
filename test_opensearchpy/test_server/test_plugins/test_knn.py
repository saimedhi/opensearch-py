# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.


from __future__ import unicode_literals
from math import e

import random
import time
from urllib import response
from opensearchpy.exceptions import RequestError
from opensearchpy import helpers

from .. import OpenSearchTestCase


class TestKNNPlugin(OpenSearchTestCase):
    def setUp(self) -> None: 
        index_name = "train-index"
        if self.client.indices.exists(index=index_name):
            self.client.indices.delete(index=index_name)
        try:
            self.client.plugins.knn.delete_model(model_id= 'my-model')
        except Exception:
            pass
            
    def tearDown(self) -> None:
        index_name = "train-index"
        if not self.client.indices.exists(self.index_name):
            self.client.indices.delete(index=self.index_name)
        try:
            self.client.plugins.knn.delete_model(model_id= 'my-model')
        except Exception:
            pass
    
    def test_knn_model(self) -> None:

        index_name = "train-index"
        # Create an index with training data
        self.client.indices.create(
            index=index_name,
            body={ "settings": {"number_of_shards": 3,"number_of_replicas": 0 },
                "mappings": {"properties": {"train-field": {"type": "knn_vector", "dimension": 4}}}
                })
            
          
        # Adding data to the index  
        docs = '''
        { "index": { "_index": "train-index", "_id": "1" } }
        { "train-field": [1.5, 5.5, 4.5, 6.4]}
        { "index": { "_index": "train-index", "_id": "2" } }
        { "train-field": [2.5, 3.5, 5.6, 6.7]}
        { "index": { "_index": "train-index", "_id": "3" } }
        { "train-field": [4.5, 5.5, 6.7, 3.7]}
        { "index": { "_index": "train-index", "_id": "4" } }
        { "train-field": [1.5, 5.5, 4.5, 6.4]}
        '''
        self.client.bulk(docs)
        
        self.client.plugins.knn.train_model(model_id= 'my-model', body = {
            "training_index": "train-index",
            "training_field": "train-field",
            "dimension": 4,
            "description": "My model description",
            "method": {
                "name": "ivf",
                "engine": "faiss",
                "space_type": "l2",
                "parameters": {
                "nlist": 4,
                "nprobes": 2
                }
            }
            })
        
        time_out = time.time() + 900  # Waiting for model to train before searching it. 
        
        while time.time() < time_out:
            
            # Fetch the model state
            try:
                response = self.client.plugins.knn.get_model(model_id='my-model')
                if response['state'] != 'training':
                    pass 
            except Exception as error:
                print(f"Error fetching knn model: {error}")
                break
            
            # Sleep for 1 minute before the next attempt
            time.sleep(10)
        
        
        
        
        #self.client.plugins.knn.get_model(model_id= 'my-model')
        
        print("response", response)
        self.client.plugins.knn.delete_model(model_id= 'my-model')