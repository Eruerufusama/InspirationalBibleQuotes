import sys
from datetime import datetime

def log(success, verse_index, header_index, image_num, time_spent, comment):
    time = datetime.now()
    time = time.strftime("%Y-%m-%d %H:%M")
    log_entry = f'{success} | {time} | {verse_index} | {header_index} | {image_num} | {time_spent} | {comment}'
    
    with open(sys.path[0] + '/bin/log.txt', 'a+') as log_file:
        log_file.write(log_entry + '\n')