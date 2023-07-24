'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-19 15:15:16
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-19 18:07:44
FilePath: \createVideo\src\data_promt_words.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import requests
import json

# 简化操作，固定提示词

negative = "NSFW,sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy,(long hair:1.4),DeepNegative,(fat:1.2),facing away, looking away,tilted head, {Multiple people}, lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, normal quality,jpegartifacts,signature, watermark, username,blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,"

prompt = "best quality,masterpiece,illustration, an extremely delicate and beautiful,extremely detailed,CG,unity,8k wallpaper, "


def create_sd_prompt(content="宫崎骏风格的小镇"):
    # TODO 这里的提示词暂时使用的是符合mj的规则，需要替换为sd 规则的
    result = "Here"
    return result

# 生成chatgpt约束提示词 （第一步）
def create_chatgpt_prompt():
    result = "根据下面的内容描述，你需要为我生成AI绘画软件stable diffution的提示词，回答的形式是：\nHere is a Stable Diffution Prompt Formula: (image we\'re prompting), (7 descriptivekeywords), (camera type), (camera lenstype), (time of day), (style of photograph)(type of film), (type of Advanced rendering technology), (Types of Game Engine), (Hd degree).\n"

    result += "这是一段按照上述形式的示例问答：\n问题：\n参考以上 Stable Diffution Prompt Formula， 写1个 Stable Diffution prompt内容，用中文和英文回复，不要括号，结尾加上:(masterpiece:1,2),best quality,masterpiece,highres,original,extremely detailed wallpaper,perfect lighting,(extremely detremely detailed CG:1.2),drawing,paintbrush, NSFW."

    result += "问题的内容：宫崎骏风格的春天小镇\n"
    
    result += "回答：\n"

    result += "1.中文：宫崎骏风格的小镇，柳绿花红，微风徐来梦幻色彩、奇幻元素、童话般的情境、温暖气息、平稳画面，长焦镜头，傍晚时分拍摄，正片胶片，采用VR技术，CD4引擎，4K超高清。(杰作: 1, 2)，最佳质量，杰作，高分辨率，原创，非常详细的壁纸，完美的照明，(非常非常详细的CG: 1.2)，绘画，画笔，NSFW.\n"

    result += "英文：Miyazaki Hayao-style town, Green willow and red flowers, breeze coming, dreamy colors, fantastic elements, fairy-tale situation, warm breath, smooth picture, telephoto lens, shooting in the evening, positive film, Using VR technology, CD4 engine, 4K ultra HD.(masterpiece: 1, 2), best quality, masterpiece, highres, original, extremely detailed wallpaper, perfect lighting, (extremely detremely detailed CG: 1.2), drawing, paintbrush, NSFW.\n"

    result += "现在严格参考以上的示例回答形式和风格（这很重要），根据以下的内容生成提示词(直接以中文和英文输出，需要补全): 宫崎骏风格的春天小镇\n"

    result += "Please respond with \"yes\" if you understandthe formula."

    return result

# 生成chatgpt约束提示词 （第二步）
def create_chatgpt_prompt_request(question):
    result = f"参考以上Stable Diffution Prompt Formula，根据以下内容生成3个Stable Diffution Prompt prompts，用中文和英文回复(需要补全)，不要括号，结尾加上 (masterpiece:1,2),best quality,masterpiece,highres,original,extremely detailed wallpaper,perfect lighting,(extremely detremely detailed CG:1.2),drawing,paintbrush, NSFW.，内容：{question}"

    return result

if __name__ == "__main__":
    create_chatgpt_prompt()
