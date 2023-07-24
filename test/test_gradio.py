'''
Author: ifredom ifredomvip@gmail.com
Date: 2023-07-24 18:19:52
LastEditors: ifredom ifredomvip@gmail.com
LastEditTime: 2023-07-24 18:19:55
FilePath: \createVideo\test\test_gradio.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
demo.launch()   
