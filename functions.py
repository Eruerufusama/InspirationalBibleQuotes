import json, sys

def file_to_list(filepath):
    with open(sys.path[0] + filepath) as FILE:
        FILE_LIST = FILE.read().split('\n')
        if FILE_LIST[-1] == '':
            del FILE_LIST[-1]
        return FILE_LIST

def json_to_dict(json_file):
    with open(sys.path[0] + json_file, encoding="utf-8") as json_file:
        return dict(json.load(json_file))

def json_to_list(json_file):
    with open(sys.path[0] + json_file, encoding="utf-8") as json_file:
        return list(json.load(json_file))

def write_to_json(json_file, dct):
    with open(sys.path[0] + json_file, 'w') as json_file:
        json.dump(dct, json_file)