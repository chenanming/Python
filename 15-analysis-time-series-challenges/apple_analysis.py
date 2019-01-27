# -*- coding:utf-8 -*-

import pandas as pd

def quarter_volume():
    df = pd.read_csv('apple.csv',header=0)
    a = df.Volume
    a.index = pd.to_datetime(df.Date)
    second_volume = a.resample('Q').sum().sort_values()[-2]

    return second_volume
