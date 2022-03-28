# Javascript Object Notation (JSON) is a common format for data transfer objects (dto)
# NB JSON is NOT Javascript - it is TEXT
import json


a = [{'name':'PC', 'cost':500, 'detail':{'a':'True', 'b':[1,2,3,4]}},{'name':'Screen','cost':250, 'detail':{'a':'False', 'b':[9,8,7,6]}}]

# convert this structure to JSON
a_j = json.dumps(a)
# convertthe json back into a Python structure
b = json.loads(a_j)
print(a)
print(a_j) # the json version of our construct
print(b)