# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

import json

with open('csv_file.txt','r') as file:
    lines = [line.strip() for line in file.readlines()]


object_list = []

for line in lines:
    line_split = line.split(',')
    dict_object = {"club": line_split[0],
                   "city": line_split[1],
                   "country": line_split[2]
                   }
    object_list.append(dict_object)

with open('json_file.txt', 'w') as file:
    json.dump(object_list, file)




