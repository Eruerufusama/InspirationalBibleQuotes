import json, sys

def file_to_list(filepath, split_char=None):
  # DOCUMENTATION
    '''

    Takes a text-file and returns a list of strings.

    '''

  # VALIDATE
    if split_char == None:
        split_char = '\n'

  # LOGIC
    with open(sys.path[0] + filepath) as FILE:
        lines = FILE.read().split(split_char)

    i = 0
    while True:
        if lines[i] == "":
            del lines[i]
        else:
            i += 1

        if i >= len(lines):
            break

    return lines



def open_json(json_file):
  # DOCUMENTATION
    '''

    Returns a dictionary or list based on the loaded json-file.

    '''

  # LOGIC
    with open(sys.path[0] + json_file, encoding="utf-8") as json_file:
        return json.load(json_file)



def write_to_json(filename, dump):
  # DOCUMENTATION
    '''

    Writes a dictionary or list to a json-file with a given filename.

    '''

  # LOGIC
    with open(sys.path[0] + filename, 'w') as filename:
        json.dump(dump, filename)