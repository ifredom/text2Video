'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-21 23:46:13
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-21 23:51:35
FilePath: \createVideo\test\test_pretable.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from prettytable import PrettyTable

# 传入的 name、age、country 相当于表头
tb = PrettyTable(["name", "age", "country"])
# 调用 add_row 添加行记录
tb.add_row(["Jack Morrison", 49, "America"])
tb.add_row(["Shimada Genji", 35, "Japan"])
tb.add_row(["Shimada Hanzo", 38, "Japan"])
tb.add_row(["Angela Ziegler", 37, "Switzerland"])

print(tb)


with open('data.csv', 'w') as file:
    file.write(tb.get_csv_string())
