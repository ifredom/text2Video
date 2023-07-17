'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-17 14:49:52
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-17 23:54:11
FilePath: \createVideo\test.py
Description: # https://zhuanlan.zhihu.com/p/180514710
'''
import ipykernel
import numpy as np
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
from gtts import gTTS
from types import SimpleNamespace
from moviepy.video.VideoClip import TextClip


config = SimpleNamespace(
    TITLE={
        "color": "white",
        "font": "Arial",
        "font-size": 48
    },
    SUBTITLE={
        "color": "yellow",
        "font": "Arial",
        "font-size": 24
    },
    ENDING={
        "color": "white",
        "font": "Arial",
        "font-size": 36
    }
)
# 使用`gTTS`库将文本转换为音频文件


def text2wav(text):
    tts = gTTS(text)
    wav_filename = "dist/output.wav"
    tts.save(wav_filename)
    return wav_filename


def get_vtuber(duration):
    # 这里可以返回您想要的视频片段或图像
    # 您可以使用MoviePy库来加载和处理视频片段或图像
    # 例如：return VideoFileClip("vtuber.mp4").subclip(0, duration)
    return VideoFileClip("assets/vtuber.mp4").subclip(0, duration)
    # return None  # 如果您不需要视频片段或图像，则返回None


def generate_text_clip(text):
    # 使用TextClip创建一个文本片段
    text_clip = TextClip(
        text, color=config.ENDING['color'], font=config.ENDING['font'], fontsize=config.ENDING['font-size'])

    size = (1280, 720)
    video = CompositeVideoClip([text_clip], size=size)

    # 可以根据需要对文本片段进行其他设置，例如位置、持续时间等
    return video


def load_video(filename):
    # 使用VideoFileClip加载视频文件
    video_clip = VideoFileClip(filename)
    # 可以根据需要对视频片段进行其他设置，例如剪辑、调整大小等
    return video_clip

# 内容解析


def parse(filename):
    result = {
        "title": "",
        "content": []
    }
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    title = lines[0].strip('#').strip()
    result['title'] = title
    content = list(filter(lambda x: x.strip() != '', lines[1:]))
    i = 0
    while i < len(content):
        s = content[i]
        currentLine = getCurrentLine(content[i+1])

        i += 2

        if currentLine["link"].endswith(".mp4") or currentLine["link"].endswith(".gif"):

            result['content'].append({
                'link': currentLine["link"],
                'text': currentLine["text"],
                'type': 'video'
            })

        else:
            subtitle = s.strip('##').strip()

            result['content'].append({
                'link': currentLine["link"],
                'text': currentLine["text"],
                'subtitle': subtitle,
                'type': 'image'
            })

    return result


def getCurrentLine(s):
    link = s[s.find("(")+1:s.find(")")]
    text = s[s.find("[") + 1:s.find("]")]
    return {
        "link": link,
        "text": text
    }

# 生成片头


def generate_title(title):

    def cascade(screenpos, i):
        v = np.array([0, -1])
        def d(t): return 1 if t < 0 else abs(np.sinc(t) / (1 + t ** 4))
        return lambda t: screenpos + v * 400 * d(t - 0.15 * i)

    def move_letters(letters, funcpos):

        return [letter.set_pos(funcpos(letter.screenpos, i))
                for i, letter in enumerate(letters)]

    size = (1280, 720)
    title_clip = TextClip(title, color=config.TITLE['color'],
                          font=config.TITLE['font'], kerning=5,
                          fontsize=config.TITLE['font-size'])
    cvc = CompositeVideoClip([title_clip.set_pos('center')], size=size)

    letters = findObjects(cvc)

    # 22
    audio = AudioFileClip(text2wav(title))

    print("audio.duration: {audio.duration}")
    vtuber_clip = get_vtuber(audio.duration)

    x1 = move_letters(letters, cascade)
    print("x====: {x1}")
    
    # clip = CompositeVideoClip([move_letters(letters, cascade), vtuber_clip.set_pos(('right', 'bottom'))])
    # cc = CompositeVideoClip([clip_right.set_pos('right').volumex(0.4),
    #                      clip_left.set_pos('left').volumex(0.4)],
    #                      size = (W,H))

    clip = CompositeVideoClip(move_letters(letters, cascade), size=size).subclip(0, 5)

    return clip

# magick wizard: wizard.jpg
# 视频片段生成


def generate_clip_with_subtitle(image_path, text):

    clip = ImageClip(image_path)

    audio = AudioFileClip(text2wav(text))

    txt_clip = TextClip(text.replace(" ", ""), font=config.SUBTITLE['font'],
                        color=config.SUBTITLE['color'], fontsize=config.SUBTITLE['font-size'])
    vtuber_clip = get_vtuber(audio.duration)

    video = CompositeVideoClip([clip, txt_clip.set_pos(('center', 'bottom')),
                                vtuber_clip.set_pos(('right', 'bottom'))])
    video.audio = audio
    video.duration = audio.duration
    return video

# 生成片尾


def generate_ending(text="听说点赞带来好运"):

    size = (1280, 720)
    title_clip = TextClip(text, color=config.ENDING['color'], font=config.ENDING['font'],
                          kerning=5, fontsize=config.ENDING['font-size'])
    clip = CompositeVideoClip([title_clip.set_pos('center')], size=size)
    clip.duration = 1
    return clip

# 完整视频合成


def generate_vlog(filename, output_path):
    clips = []
    result = parse(filename)

    title_clip = generate_title(result['title'])

    clips.append(title_clip)
    for item in result['content']:
        # if item['text']:
        #     clips.append(generate_text_clip(item['text']))
        if item['type'] == 'image':
            clips.append(generate_clip_with_subtitle(
                item['link'], item['subtitle']))
        elif item['type'] == 'video':
            clips.append(load_video(item['link']))
    clips.append(generate_ending())
    print("最终========{clips}")
    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_path, fps=24, audio_codec="aac")
