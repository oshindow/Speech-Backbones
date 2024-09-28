import matplotlib.pyplot as plt
import os
from pydub import AudioSegment

def get_audio_lengths(file_path):
    audio = AudioSegment.from_file(file_path)
    length_in_seconds = len(audio) / 1000  # Length in seconds
    # audio_lengths.append(length_in_seconds)

    return length_in_seconds

# 初始化字典
spk_dict = {}
acc_dict = {}
length_dict = {'0': [],'1': [],'2': [],'3': []}
acc_spk = {'0': set(),'1': set(),'2':set() ,'3': set()}

# 读取文件并统计
trainfile = '/home/xintong/Speech-Backbones/Grad-TTS/resources/filelists/zh_all/train.dedup.txt'
idx = 0
with open(trainfile, 'r', encoding='utf8') as input_file:
    for line in input_file:
        uid, text, spk, acc = line.strip().split('|')
        spk_dict[spk] = spk_dict.get(spk, 0) + 1
        acc_dict[acc] = acc_dict.get(acc, 0) + 1
        length_dict[acc].append(get_audio_lengths(uid))
        acc_spk[acc].add(spk)

# 打印统计结果
print("acc_dict:", acc_dict)
print("spk_dict:", spk_dict)
# print("length_dict:", length_dict)
print('length_dict')
for values in length_dict.values():
    print(min(values), max(values), sum(values) / len(values))

print("length_dict:", [len(spk) for spk in acc_spk.values()])

# 画柱状图
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# # 绘制 acc_dict 的柱状图
# ax1.bar(acc_dict.keys(), acc_dict.values())
# ax1.set_title('Distribution of Accents')
# ax1.set_xlabel('Accent')
# ax1.set_ylabel('Count')
# ax1.set_xticklabels(acc_dict.keys(), rotation=45)

# # 绘制 spk_dict 的柱状图
# ax2.bar(spk_dict.keys(), spk_dict.values())
# ax2.set_title('Distribution of Speakers')
# ax2.set_xlabel('Speaker')
# ax2.set_ylabel('Count')
# ax2.set_xticklabels(spk_dict.keys(), rotation=45)

# # 调整布局
# plt.tight_layout()
# plt.savefig('data_distribution_dedup.png')
