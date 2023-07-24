'''
Author: ifredom ifredomvip@gmail.com
Date: 2023-07-24 20:14:01
LastEditors: ifredom ifredomvip@gmail.com
LastEditTime: 2023-07-24 20:16:15
FilePath: \createVideo\test\test_ffmpg.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import ffmpeg

import sys;
print(sys.executable)

def get_video_resolution(filename):
    probe = ffmpeg.probe(filename)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    width = int(video_info['width'])
    height = int(video_info['height'])
    return width, height

filename = '22.mp4'
width, height = get_video_resolution(filename)
print(f"视频分辨率为: {width}x{height}")
