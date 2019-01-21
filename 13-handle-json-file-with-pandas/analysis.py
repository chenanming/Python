# /usr/bin/env python
import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    
    f = open(file)
    data = json.load(f)
    for item in data:
        if item['user_id'] != user_id:
            continue
        times += 1
        minutes += item['minutes']
    f.close()
    return times, minutes
