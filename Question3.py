import sys
import json

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

obj_string=input("Enter object :")   ##obj = {"x": {"y": {"z" : "a"}}}
obj = json.loads(obj_string)

user_key_string=input("Enter key: ") ## key = x/y/z
key=user_key_string.split('/').pop()

for k, v in recursive_items(obj):
    if(k != key):
        continue;
    print(v)   ## a
    break;