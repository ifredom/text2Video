'''
Author: ifredom ifredomvip@gmail.com
Date: 2023-07-24 19:29:07
LastEditors: ifredom ifredomvip@gmail.com
LastEditTime: 2023-07-24 20:09:36
FilePath: \createVideo\test\test_download_youtube.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pytube import YouTube

# 视频的URL
url = "https://www.youtube.com/watch?v=8ao1NAOVKTU&t=31s"

# 创建YouTube对象
yt = YouTube(url)

# 获取视频的所有可用格式
formats = yt.streams
print(formats)

# 选择要下载的清晰度（这里选择最高清晰度）
video = formats.get_highest_resolution()

# 选择要下载的格式（这里选择第一个）
video = formats[6]

# 开始下载
video.download()
