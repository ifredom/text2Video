'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-19 13:50:36
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-22 02:50:18
FilePath: \createVideo\src\data_prepare.py
Description: 处理content文本文件内容
'''
import pandas as pd
from prettytable import PrettyTable


def prepare_data():
    read_data_content("assets/content.txt")


def read_data_content(path):

    with open(path, 'r', encoding="utf-8") as file:
        content = file.readlines()
        table = format_content(content)
        save_to_csv("assets/content_output.csv", table)
    return content


def save_to_csv(file_path, table):
    # df = pd.DataFrame(table[1:], columns=table[0])
    # df = pd.DataFrame(['title', 'subtitle', 'content',
    #                     'en_name', 'cn_name', 'prompt'])
    
    table_data = [table.field_names] + [row for row in table]
    print(table_data)
    df = pd.DataFrame(table_data[1:], columns=table_data[0])
    # df.to_csv(file_path, index=False)


def format_content(content):
    table = PrettyTable(['title', 'subtitle', 'content',
                        'en_name', 'cn_name', 'prompt'])
    for line in content:
        if "" != line.strip():
            table.add_row(['', '', line.strip(), '', '', ''])
    # return table
    table_data = [table.field_names] + [row.split() for row in table.get_string().split('\n') if row.strip()]
    return table_data[1:]  # 去除表头行


if __name__ == "__main__":
    prepare_data()
