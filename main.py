'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-17 18:58:02
LastEditors: ifredom ifredomvip@gmail.com
LastEditTime: 2023-07-24 02:13:58
FilePath: \createVideo\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from src.data_promt_words import load_data_text
from src.generate_vlog import generate_vlog

# 设置输入文件路径和输出文件路径
filename = "assets/input.txt"
output_path = "dist/output.mp4"



if __name__ == '__main__':
  # generate_vlog(filename, output_path)
  load_data_text("")
