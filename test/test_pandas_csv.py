'''
Author: “ifredom” ifredomvip@gmail.com
Date: 2023-07-19 14:02:27
LastEditors: “ifredom” ifredomvip@gmail.com
LastEditTime: 2023-07-19 14:49:49
FilePath: \createVideo\test\test_pandas_csv.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%A
'''
import pandas as pd


# 读取
def load_data_csv(filePath):
    if filePath == "":
        filePath = "data/source_data/测试例子.csv"

    df_temp = pd.read_csv(filePath)
    print(df_temp)

# 读取 并 固定格式
def load_data_csv_with_dataframe(filePath):
    if filePath == "":
        filePath = "data/source_data/测试例子.csv"

    df = pd.DataFrame(columns=["title", "subtitle", "content"])

    story_data_title = "标题:死者之书。"
    story_data_subtitle = "子标题:悬疑故事."
    story_data_content = "陈雨疲惫地拍了拍自己的脑门。"

    new_row = {'id': 1, 'title': story_data_title, 'subtitle': story_data_subtitle, 'content': story_data_content}
    df = df.append(new_row, ignore_index=True)
    print(df)
    print(df.dtypes)
    print(df.index)

# 保存为csv
def save_data_to_csv(filePath):
    if filePath == "":
        filePath = "data/source_data/测试例子.csv"

    df = pd.DataFrame(columns=["title", "subtitle", "content"])
    df_temp = pd.read_csv(filePath)

    story_data_title = "标题:死者之书主人公以及人设:古籍专家陈雨，博学多才，对古籍充满热情。故事背景:—本神秘古籍中，记录了一系列令人不寒而栗的谋杀案。故事主线:陈雨破译古籍，试图阻止接下来的谋杀案发生。故事发展:陈雨深入调查古籍背后的故事，逐渐发现了一个隐藏已久的秘密。结局:最后，原来古籍中的案件都与古时王朝的仇杀有关，而这些仇杀正是某个家族所为。陈雨成功阻止了家族复仇计划。"
    story_data_subtitle = "子标题:悬疑故事爱"
    story_data_content = "陈雨疲惫地拍了拍自己的脑门，又拿起一本古籍开始研究，他的目光专注而坚定。这位专家对于古籍的兴趣和热情一直都是无人能及的，而这次他遇到了一本特别的古籍——《死者之书》。《死者之书》记录了一系列让人毛骨悚然的谋杀案，这些案件都匪夷所思，让陈雨不得不重新审视过去的这些案件。他的研究引起了警方的注意，但他并没有放弃，反而更加坚定地要解开这个谜团。陈雨的调查逐渐深入，他发现这些案件都隐藏着一个久远的秘密。随着调查的深入，他意识到自己已经卷入了一个更加危险的局面中。一天晚上，陈雨突然接到了一个神秘的电话，对方声称自己知道《死者之书》的真相，并邀请他前往一个偏远的村庄。陈雨迫不及待地赶往村庄，却发现那里已经是一片废墟，而对方也不见了踪影。陈雨惊恐万分，但他没有放弃，他相信这一切都与古籍有关。他回到了他的实验室，开始重新审视这本神秘的古籍。在一番研究之后，他发现这些案件都与古时王朝的仇杀有关，而这些仇杀正是某个家族所为。陈雨决定阻止这个家族的复仇计划，他开始寻找这个家族的线索，最终找到了目标。在一次危险的行动中，他成功阻止了复仇计划，并将罪犯绳之以法。陈雨的勇气和智慧最终解开了《死者之书》的谜团，他的贡献得到了社会的认可和赞誉。他知道，他的研究不仅仅是为了解开这个谜团，更是为了保护社会的安宁和公正。"

    new_row = {'id': 1, 'title': story_data_title, 'subtitle': story_data_subtitle, 'content': story_data_content,
               'len_text': 4000, 'type': '玄幻类', 'en_name': 'story_1', 'cn_name': '死亡之书', 'status': '未完成'}
    df = df.append(new_row, ignore_index=True)


    df.to_csv("example.csv", index=False)


if __name__ == "__main__":
    load_data_csv_with_dataframe("")
