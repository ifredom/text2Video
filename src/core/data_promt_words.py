'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-19 15:15:16
LastEditors: ifredom ifredomvip@gmail.com
LastEditTime: 2023-07-24 20:45:13
FilePath: \createVideo\src\data_promt_words.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import pandas as pd
import requests
import json

from src.core.data_split import split_data_process


negative = "NSFW,sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy,(long hair:1.4),DeepNegative,(fat:1.2),facing away, looking away,tilted head, {Multiple people}, lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,"

prompt = "best quality,masterpiece,illustration, an extremely delicate and beautiful,extremely detailed,CG,unity,8k wallpaper."

# 调用gpt处理短句


def prompt_generation(param):
    url = 'http://127.0.0.1:8000'
    data = {'prompt': param}
    json_data = json.dumps(data)
    header = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.post(url, data=json_data, headers=header)
    result_json = json.loads(response.text)
    # 结果
    return result_json['response']


prompt_prefix_answer = "Here is a Midjourney Prompt Formula"


def load_data_text(path):
    if not path:
        path = "data/source_data/story1.csv"
        # # 获取当前脚本所在目录的路径
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # # 拼接CSV文件的相对路径
        # path = os.path.join(current_dir, "data\source_data\少年歌行第一章.csv")
    dict = ["index", "content", "prompt", "negative"]
    df = pd.DataFrame(columns=dict)
    df_temp = pd.read_csv(path)

    # TODO 测试
    # result_json = prompt_generation('你好啊')

    for index, row in df_temp.iterrows():
        print(f'当前row内容： {row["content"]}')
        perfeth_train_gpt()

        result_json = prompt_generation(row['content'])
        new_row = {'index': index, 'content': result_json,
                   'prompt': prompt + result_json, 'negative': negative}
        # df = df.append(new_row, ignore_index=True)
        df = pd.concat([df, pd.DataFrame(new_row, index=[0])],
                       ignore_index=True)
    new_path = path.replace("source_data", "data_prompt")

    parent_path = new_path.split('story_')[0].split('.')[0]
    print("parent_path: "+parent_path)

    # split_data_process(new_path)

    if not os.path.exists(parent_path):
        os.makedirs(parent_path)
    df.to_csv(new_path, encoding='utf-8')
    return new_path

# TODO 这里缺少一步 调试chat的步骤
# 设定 chatgot 文本处理规则,并填充源数据 （未完）


def perfeth_train_gpt():
    # TODO 定义chatgot 文本处理规则
    result = ""
    return result


if __name__ == "__main__":
    load_data_text("")
