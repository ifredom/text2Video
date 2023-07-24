'''
Author: ifredom ifredomvip@gmail.com
Date: 2023-07-24 20:30:45
LastEditors: ifredom ifredomvip@gmail.com
LastEditTime: 2023-07-24 20:42:06
FilePath: \createVideo\src\core\data_split.py
Description: Description: 将语料进行切割，按照中文的句号进行切割，并保存到指定位置
'''
import pandas as pd
import os

def split_data_process(path):
    data_csv_path = ""
    df = pd.read_csv(path)
    for i in range(len(df)):
        type_path = df["type"][i]
        # 读取整段文本 并且按照中文的句号进行切分
        content = df["content"][i].split('。')
        content = [x.strip().replace("\n", "")
                   for x in content if len(x.strip()) > 0]
        # 创建新的文件保存切割后的文件
        each_df = pd.DataFrame(content, columns=["text"])

        # TODO windows无法创建文件夹。
        data_csv_path = os.path.join("data/data_split", type_path)

        csv_save_path = os.path.join(data_csv_path, df["en_name"][i] + ".csv")
        csv_save_path = csv_save_path.replace("\\", "/")

        print(csv_save_path)
        each_df.to_csv(csv_save_path, index=False)
    return "data/data_split"


if __name__ == '__main__':
    split_data_process("data/source_data/example.csv")
    print(pd.__version__)
