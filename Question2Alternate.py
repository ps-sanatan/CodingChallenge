#!/usr/bin/env python
import requests
import json
from nested_lookup import nested_lookup

# Azure freature to get metadata of an instance. Needs to be run on a VM
nested_json_data = curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq

#The data key from User
key = input('Enter the data key\n') 

#Nested_lookup package provides many Python functions for working with deeply nested documents. 
#pip install nested-lookup

#Print the key with value
results = nested_lookup(
    key = '$key',
    document = nested_json_data,
    wild = True,
    with_keys = True,
)

print(results)