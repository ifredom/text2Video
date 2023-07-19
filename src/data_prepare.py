'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-19 13:50:36
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-19 15:10:44
FilePath: \createVideo\src\data_prepare.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import pandas as pd

def create_data_example():
    df = pd.DataFrame(columns=['id', 'story_framework', 'content',
                      'len_text', 'type', 'en_name', 'cn_name', 'status'])
    story_framework = "标题:死者之书主人公以及人设:古籍专家陈雨，博学多才，对古籍充满热情。故事背景:—本神秘古籍中，记录了一系列令人不寒而栗的谋杀案。故事主线:陈雨破译古籍，试图阻止接下来的谋杀案发生。故事发展:陈雨深入调查古籍背后的故事，逐渐发现了一个隐藏已久的秘密。结局:最后，原来古籍中的案件都与古时王朝的仇杀有关，而这些仇杀正是某个家族所为。陈雨成功阻止了家族复仇计划。"
    story_content = "陈雨疲惫地拍了拍自己的脑门，又拿起一本古籍开始研究，他的目光专注而坚定。这位专家对于古籍的兴趣和热情一直都是无人能及的，而这次他遇到了一本特别的古籍——《死者之书》。《死者之书》记录了一系列让人毛骨悚然的谋杀案，这些案件都匪夷所思，让陈雨不得不重新审视过去的这些案件。他的研究引起了警方的注意，但他并没有放弃，反而更加坚定地要解开这个谜团。陈雨的调查逐渐深入，他发现这些案件都隐藏着一个久远的秘密。随着调查的深入，他意识到自己已经卷入了一个更加危险的局面中。一天晚上，陈雨突然接到了一个神秘的电话，对方声称自己知道《死者之书》的真相，并邀请他前往一个偏远的村庄。陈雨迫不及待地赶往村庄，却发现那里已经是一片废墟，而对方也不见了踪影。陈雨惊恐万分，但他没有放弃，他相信这一切都与古籍有关。他回到了他的实验室，开始重新审视这本神秘的古籍。在一番研究之后，他发现这些案件都与古时王朝的仇杀有关，而这些仇杀正是某个家族所为。陈雨决定阻止这个家族的复仇计划，他开始寻找这个家族的线索，最终找到了目标。在一次危险的行动中，他成功阻止了复仇计划，并将罪犯绳之以法。陈雨的勇气和智慧最终解开了《死者之书》的谜团，他的贡献得到了社会的认可和赞誉。他知道，他的研究不仅仅是为了解开这个谜团，更是为了保护社会的安宁和公正。"
    # 插入数据
    new_row = {"id": 1, "story_framework": story_framework,
               "content": story_content, "len_text": 4,
               "type": "玄幻类", "en_name": "story_1", "cn_name": "死者之书", "status": "未完成"}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    story_framework1 = "标题:我即神话主人公以及人设:少林寺的俗家弟子叶无名，博览群书，精通天文地理，阴阳八卦，穿越到异世界。故事背景:叶无名从体质废柴的败家子，修炼武技功法，一步步达到震烁古今的大能，成为整个宇宙的主宰。故事主线:叶无名面对别人的嘲笑，冷漠与辱骂，一次次的心理打击，磨练心性，每一次都能打败敌人，顺利逆袭。故事发展:叶无名从废柴，到改变家族地位，到离开家乡，踏上求仙之路，一路上打怪升级，在艰难困苦中成为一国之主。结局:最后，叶无名不仅报仇成功，更是成为了楚国的国主。"
    story_content1 = "叶无名是一个少林寺的俗家弟子，他天资聪颖，博览群书，精通天文地理和阴阳八卦。但是他却是一个体质废柴的败家子，没有任何武术天赋，被认为是一个毫无用处的人。然而，一天，他突然穿越到了一个陌生的世界。这个世界与他原来的世界完全不同，有着奇特的生物和神秘的力量。但是，他发现自己身上的废柴属性消失了，取而代之的是强大的力量和无穷的智慧。叶无名开始修炼武技功法，一步步达到震烁古今的大能。他通过不断的战斗和历练，磨练心性，每一次都能打败敌人，顺利逆袭。他越来越强大，成为整个宇宙的主宰。在这个异世界中，他遇到了各种各样的人和生物，有好的，也有坏的。有些人对他友善，有些人则嘲笑和辱骂他。但是，叶无名从来不会被打败，他总能化解每一个心理打击，用智慧和力量证明自己的价值。不知不觉中，叶无名已经在这个异世界中生活了很长一段时间。他从废柴，到改变家族地位，到离开家乡，踏上求仙之路，一路上打怪升级，在艰难困苦中成为一国之主。最后，叶无名不仅报仇成功，更是成为了楚国的国主。他用自己的智慧和勇气，为这个国家带来了繁荣和和平。他成为了一个神话，一个传奇。"  # 插入一行数据
    # 插入数据
    new_row1 = {'id': 2, 'story_framework': story_framework1, 'content': story_content1, 'len_text': 4000, 'type': '修真类', 'en_name': 'story_2', 'cn_name': '我即神话', 'status': '未完成'}
    # df = df.concat(new_row1, ignore_index=True)
    df = pd.concat([df, pd.DataFrame([new_row1])],ignore_index=True)
    # 保存为csv格式
    df.to_csv("data/source_data/example1.csv", index=False, encoding='utf-8')


if __name__ == "__main__":
    create_data_example()