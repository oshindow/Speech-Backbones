import matplotlib.pyplot as plt
import os
from pydub import AudioSegment
from collections import defaultdict

# 1. prepare 3 testsets (seen speaker - 200 (100 north, 100 south), unseen speaker - 200 (100 north, 100 south), SG speakers - 200)
# 2. input from /data2/ output to /data2/
# 3. text 

def get_audio_lengths(file_path):
    audio = AudioSegment.from_file(file_path)
    length_in_seconds = len(audio) / 1000  # Length in seconds
    # audio_lengths.append(length_in_seconds)

    return length_in_seconds

wavscp = open('wav.scp', 'w', encoding='utf8')
text = open('text.txt', 'w', encoding='utf8')
import json
content = {}
with open('/home/xintong/Speech-Backbones/Grad-TTS/resources/filelists/magichub_sg/raw.txt', 'r', encoding='utf8') as input:
    for line in input:
        uid = line.strip().split('|')[0]
        content[uid] = line.strip().split('|')[1]
with open('phonemes2pinyin.json', 'r', encoding='utf8') as input:
    phonemes2pinyin = json.load(input)

with open('token_list', 'r', encoding='utf8') as input:
    token_list = [token.strip() for token in input.readlines()]

with open('/home/xintong/Speech-Backbones/Grad-TTS/G0004_part1_label.json', 'r', encoding='utf8') as input:
    data = json.load(input)
    for file in data.keys():
        
        wavscp.write(file[:-4] + ' /data2/xintong/magichub_singapore/wav_24k/G0004/' + file + '\n') 
        phonemes = content[file[:-4]].split(' ')
        pinyins = []

        idx = 0
        while idx < len(phonemes):
            if phonemes[idx] == 'sil':
                pinyin = 'sil'
                # pinyin.append('sil')
                idx += 1
            elif " ".join(phonemes[idx:idx+2]) in phonemes2pinyin:
                pinyin = phonemes2pinyin[" ".join(phonemes[idx:idx+2])]
                idx += 2
            else:
                pinyin = "".join(phonemes[idx:idx+2])
                idx += 2

            pinyins.append(pinyin)

        text.write(file[:-4] + '|' + " ".join(pinyin) + '\n')

text.close()
wavscp.close()

def write_text_magichubsg():
    import json
    content = {}
    with open('/home/xintong/Speech-Backbones/Grad-TTS/resources/filelists/magichub_sg/raw.txt', 'r', encoding='utf8') as input:
        for line in input:
            uid = line.strip().split('|')[0]
            content[uid] = line.strip().split('|')[1]
    wavscp = open('/data2/xintong/accent_testsets/magichub-sg/wav.scp', 'w', encoding='utf8')
    text = open('/data2/xintong/accent_testsets/magichub-sg/text', 'w', encoding='utf8')
    with open('/data2/xintong/magichub_singapore/G0004_part2_test.json', 'r', encoding='utf8') as input:
        data = json.load(input)
        for uid in data.keys():
            if uid[:-4] in content: 
                text.write(uid[:-4] + '|' + content[uid[:-4]] + '\n')
                wavscp.write(uid[:-4] + ' /data2/xintong/magichub_singapore/wav_16k/G0004/' + uid + '\n') 
    text.close()
    wavscp.close()
    
def dump_text_aishell():
    content = {}
    with open('/home/xintong/fastspeech2/data/train_val_test_data/testList.txt.bk', 'r', encoding='utf8') as input:
        for line in input:
            data = line.strip().split('|')
            uid = data[0]
            content[uid] = data[1]
    output = open('/data2/xintong/accent_testsets/aishell3_seen/text', 'w', encoding='utf8')
    with open('/data2/xintong/accent_testsets/aishell3_seen/wav.scp', 'r', encoding='utf8') as input:
        for line in input:
            uid = line.strip().split(' ')[0]
            if uid in content:
                output.write(uid + '|' + content[uid] + '\n')

    output.close()
    output = open('/data2/xintong/accent_testsets/aishell3_unseen/text', 'w', encoding='utf8')
    with open('/data2/xintong/accent_testsets/aishell3_unseen/wav.scp', 'r', encoding='utf8') as input:
        for line in input:
            uid = line.strip().split(' ')[0]
            if uid in content:
                output.write(uid + '|' + content[uid] + '\n')

    output.close()

def ramdom_select_data():
    root = '/data2/xintong/aishell3/'
    spk_in_train = os.listdir(os.path.join(root, 'train', 'wav_16k'))
    spk_in_test = os.listdir(os.path.join(root, 'test', 'wav_16k'))

    print(len(spk_in_test), len(spk_in_train))
    spk_unseen = {} # 44
    spk_seen = {} # 170
    for spk in spk_in_test:
        if spk not in spk_in_train:
            spk_unseen[spk] = {}
        else:
            spk_seen[spk] = {}

    for spk in spk_in_train:
        if spk not in spk_in_test:
            print(spk)
    # SSB0748
    # SSB1096
    # SSB0426
    # SSB1567
    with open(os.path.join(root, 'seen_speakers.txt'), 'w', encoding='utf8') as output:
        for spk in spk_seen.keys():
            output.write(spk + '\n')

    with open(os.path.join(root, 'unseen_speakers.txt'), 'w', encoding='utf8') as output:
        for spk in spk_unseen.keys():
            output.write(spk + '\n')

    import json
    count_south = 0
    count_north = 0
    with open('resources/spk2accent.json', 'r', encoding='utf8') as input:
        spk2accent = json.load(input)
        for spk in spk_seen.keys():
            spk_seen[spk]['accent'] = spk2accent[spk]
            if spk2accent[spk] == 'south':
                count_south += 1
            elif spk2accent[spk] == 'north':
                count_north += 1
            else:
                print(spk2accent[spk])

            samples = len(os.listdir(os.path.join(root, 'test', 'wav_16k', spk)))
            spk_seen[spk]['samples'] = samples

    print(count_north, count_south) # test unseen: 37 7, test seen: 127 42
    with open(os.path.join(root, 'seen_speakers_samples.json'), 'w', encoding='utf8') as output:
        json.dump(spk_seen, output, indent=2)

    # random pick 200 from seen, 200 from unseen

    unseen_files = []
    seen_files = []
    for spk in spk_unseen.keys():
        for file in os.listdir(os.path.join(root, 'test', 'wav_16k', spk)):
            unseen_files.append(file)

    for spk in spk_seen.keys():
        for file in os.listdir(os.path.join(root, 'test', 'wav_16k', spk)):
            seen_files.append(file)

    import random
    random.shuffle(seen_files)
    random.shuffle(unseen_files)

    final_unseen_count = {}
    final_seen_count = {}
    with open('/data2/xintong/accent_testsets/aishell3_seen/wav.scp', 'w', encoding='utf8') as output:
        for file in seen_files[:200]:
            output.write(file[:-4] + ' ' + os.path.join(root, 'test', 'wav_16k', file[:7], file) + '\n')
            spk = file[3:7]
            if spk in final_seen_count:
                final_seen_count[spk] += 1
            else:
                final_seen_count[spk] = 1
    with open('/data2/xintong/accent_testsets/aishell3_unseen/wav.scp', 'w', encoding='utf8') as output:
        for file in unseen_files[:200]:
            output.write(file[:-4] + ' ' + os.path.join(root, 'test', 'wav_16k', file[:7], file) + '\n')
            spk = file[3:7]
            if spk in final_unseen_count:
                final_unseen_count[spk] += 1
            else:
                final_unseen_count[spk] = 1


    import matplotlib.pyplot as plt
    # import matplotlib.pyplot as plt
    import matplotlib

    # 全局设置字体为 Times New Roman
    matplotlib.rcParams['font.family'] = 'Times New Roman'
    # Example data: replace this with your actual data
    speakers = range(1, len(final_seen_count.keys())+1)
    counts = final_seen_count.values()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(speakers, counts, color='skyblue', edgecolor='black')
    plt.xlabel('Speakers', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    # plt.title('Seen Speaker Distribution', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(range(1, len(final_seen_count.keys())+1, 1),rotation=45,  fontsize=9)
    # Display the chart
    plt.tight_layout()
    plt.savefig('Seen Speaker Distribution.png')
    plt.close()

    # Example data: replace this with your actual data
    speakers = range(1, len(final_unseen_count.keys())+1)
    counts = final_unseen_count.values()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(speakers, counts, color='skyblue', edgecolor='black')
    plt.xlabel('Speakers', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    # plt.title('Unseen Speaker Distribution', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(range(1, len(final_unseen_count.keys())+1, 1),rotation=45,  fontsize=9)
    # Display the chart
    plt.tight_layout()
    plt.savefig('Unseen Speaker Distribution.png')

    # Data for seen speakers
    speakers_seen = range(1, len(final_seen_count.keys()) + 1)
    counts_seen = final_seen_count.values()

    # Data for unseen speakers
    speakers_unseen = range(1, len(final_unseen_count.keys()) + 1)
    counts_unseen = final_unseen_count.values()

    # Create a figure with two rows
    plt.figure(figsize=(12, 10))

    # First subplot for Seen Speaker Distribution
    plt.subplot(2, 1, 1)  # (rows, columns, index)
    plt.bar(speakers_seen, counts_seen, color='skyblue', edgecolor='black')
    plt.xlabel('Speakers', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.title('Distribution of Seen Speakers', fontsize=16)
    plt.xticks(range(1, len(final_seen_count.keys()) + 1), final_seen_count.keys(), rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Second subplot for Unseen Speaker Distribution
    plt.subplot(2, 1, 2)  # (rows, columns, index)
    plt.bar(speakers_unseen, counts_unseen, color='skyblue', edgecolor='black')
    plt.xlabel('Speakers', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.title('Distribution of Unseen Speakers', fontsize=16)
    plt.xticks(range(1, len(final_unseen_count.keys()) + 1), final_unseen_count.keys(), rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adjust layout and save the figure
    plt.tight_layout()
    plt.savefig('Speaker_Distributions.png')
# for file in os.listdir(root):
#     if '.wav' in file:
#         filepath = os.path.join(root, file)
#         # uid, text, acc = line.strip().split('|')
#         spk = filepath.split('/')[-2]
#         spk_dict[spk] = spk_dict.get(spk, 0) + 1
#         # acc_dict[acc] = acc_dict.get(acc, 0) + 1
#         length_dict[file] = get_audio_lengths(filepath)
#         # acc_spk[acc].add(spk)
# import json
# # 打印统计结果
# print("acc_dict:", acc_dict)
# print("spk_dict:", spk_dict)
# # print("length_dict:", length_dict)
# print('length_dict', sum(length_dict.values())/ 60)
# # with open('G0001_lengths.json', 'w', encoding='utf8') as output:
#     json.dump(length_dict, output, indent=2)