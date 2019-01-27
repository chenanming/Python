# -*- coding:utf-8 -*-

import pandas as pd

def quarter_volume():
    df = pd.read_csv('apple.csv',header=0)
    '''
    1.使用pandas选择数据Volume
    2.转换为时间序列
    3.按季度重新采样并排序
    '''
    a = df.Volume
    a.index = pd.to_datetime(df.Date)
    second_volume = a.resample('Q').sum().sort_values()[-2]

    return second_volume
