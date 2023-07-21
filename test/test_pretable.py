'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-21 23:46:13
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-22 01:33:12
FilePath: \createVideo\test\test_pretable.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from prettytable import PrettyTable
import pandas as pd
# 传入的 name、age、country 相当于表头


def add_row():
    tb = PrettyTable(["name", "age", "country"])
    # 调用 add_row 添加行记录
    tb.add_row(["Jack Morrison", 49, "America"])
    tb.add_row(["Shimada Genji", 35, "Japan"])
    tb.add_row(["Shimada Hanzo", 38, "Japan"])
    tb.add_row(["Angela Ziegler", 37, "Switzerland"])
    print(tb)

# 读取


def read_CSV_data(path='data.csv'):
    if not path:
        path = 'data.csv'  # 使用相对路径，文件在当前目录下

    df = pd.read_csv(path)
    table = PrettyTable(["name", "age", "country"])
    # print(df.head())

    row_index = 0
    while row_index < len(df):
        row = df.iloc[row_index]
        table.add_row(row)
        row_index += 1
    print(table)

    

def write_csv(path):
    if not path:
        path = 'data.csv'  # 使用相对路径，文件在当前目录下
    df = pd.DataFrame(columns=["name",'age','country'])




if __name__ == "__main__":
    read_CSV_data('data.csv')
