'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-19 13:50:36
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-22 02:30:08
FilePath: \createVideo\src\data_prepare.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import pandas as pd
from prettytable import PrettyTable


def create_data_example(path=""):
    if not path:
        path = 'data/source_data/template_example.csv'

    dict = ['id', 'story_framework', 'content',
            'len_text', 'type', 'en_name', 'cn_name', 'status']

    df_temp = pd.read_csv(path)

    table = PrettyTable(dict)
    table = read_df_to_table(df_temp,table)
    return table

def read_df_to_table(df,table):
    row_index = 0
    while row_index < len(df):
        row = df.iloc[row_index]
        table.add_row(row)
        row_index += 1
    return table

if __name__ == "__main__":
    create_data_example()
