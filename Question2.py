#!/usr/bin/env python
import requests
import json

# Azure freature to get metadata of an instance. Needs to be run on a VM
nested_json_data = curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq

#The data key from User
key = input('Enter the data key\n') 

#Method to iterate over json for the key
def findall(v, k):
  if type(v) == type({}):
     for k1 in v:
         if k1 == k:
            print(v[k1])
         findall(v[k1], k)

#Calling method
findall(nested_json_data, key)