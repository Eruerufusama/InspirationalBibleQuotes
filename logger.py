import sys
from datetime import datetime


def log(verse_index, header_index):
    log_entry = f'{datetime.now()} | {verse_index} | {header_index} |'
    with open(sys.path[0] + '/bin/log.txt', 'a+') as log_file:
        log_file.write(log_entry + '\n')
