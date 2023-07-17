'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-17 17:21:42
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-17 17:22:32
FilePath: \createVideo\example\writeText.py
Description: 打开一个视频，将0-10秒得内容剪辑，在视频中添加字幕。
'''

from moviepy.editor import *
 
video = VideoFileClip("auto.mp4").subclip(0,10)
 
# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2023",fontsize=70,color='white')
             .set_position('center')
             .set_duration(3) )
 
result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25)
