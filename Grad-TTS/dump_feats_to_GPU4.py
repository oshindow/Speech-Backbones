# Copyright (C) 2021. Huawei Technologies Co., Ltd. All rights reserved.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the MIT License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# MIT License for more details.

import argparse
import json
import datetime as dt
import numpy as np
from scipy.io.wavfile import write
from utils import write_hdf5
import torch
import os
import params_ori as params
from model import GradTTSORI
from text import text_to_sequence, cmudict
from text.symbols import symbols
from utils import intersperse

import sys
sys.path.append('./hifi-gan/')
from env import AttrDict
from models import Generator as HiFiGAN


HIFIGAN_CONFIG = './checkpts/hifigan-config.json'
HIFIGAN_CHECKPT = './checkpts/hifigan.pt'

# python dump_feats_to_GPU4.py -f resources/filelists/synthesis.txt -c logs/new_exp/grad_1518.pt -o logs/new_exp/gen_grad_1518/raw
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True, help='path to a file with texts to synthesize')
    parser.add_argument('-c', '--checkpoint', type=str, required=True, help='path to a checkpoint of Grad-TTS')
    parser.add_argument('-t', '--timesteps', type=int, required=False, default=10, help='number of timesteps of reverse diffusion')
    parser.add_argument('-s', '--speaker_id', type=int, required=False, default=None, help='speaker id for multispeaker model')
    parser.add_argument('-o', '--output_dir', type=str, required=True, default=None, help='speaker id for multispeaker model')
    args = parser.parse_args()
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # if not isinstance(args.speaker_id, type(None)):
    #     assert params.n_spks > 1, "Ensure you set right number of speakers in `params.py`."
    #     spk = torch.LongTensor([args.speaker_id]).cuda()
    # else:
    #     spk = None
    
    print('Initializing Grad-TTS...')
    generator = GradTTSORI(len(symbols)+1, params.n_spks, params.spk_emb_dim,
                        params.n_enc_channels, params.filter_channels,
                        params.filter_channels_dp, params.n_heads, params.n_enc_layers,
                        params.enc_kernel, params.enc_dropout, params.window_size,
                        params.n_feats, params.dec_dim, params.beta_min, params.beta_max, params.pe_scale)
    generator.load_state_dict(torch.load(args.checkpoint, map_location=lambda loc, storage: loc))
    _ = generator.cuda().eval()
    print(f'Number of parameters: {generator.nparams}')
    
    # print('Initializing HiFi-GAN...')
    # with open(HIFIGAN_CONFIG) as f:
    #     h = AttrDict(json.load(f))
    # vocoder = HiFiGAN(h)
    # vocoder.load_state_dict(torch.load(HIFIGAN_CHECKPT, map_location=lambda loc, storage: loc)['generator'])
    # _ = vocoder.cuda().eval()
    # vocoder.remove_weight_norm()
    texts = []
    utt_ids = []
    spk_ids = []
    with open(args.file, 'r', encoding='utf-8') as f:
        for line in f:
            texts.append(line.strip().split('|')[1])
            utt_ids.append(line.strip().split('|')[0])
            spk_ids.append(line.strip().split('|')[2])

    cmu = cmudict.CMUDict('./resources/cmu_dictionary')
    print(utt_ids, texts)
    with torch.no_grad():
        for i, text in enumerate(texts):
            
            print(f'Synthesizing {i} text...', utt_ids[i], text)
            x = torch.LongTensor(intersperse(text_to_sequence(text, dictionary=cmu), len(symbols))).cuda()[None]
            print(x)
            x_lengths = torch.LongTensor([x.shape[-1]]).cuda()
            spk = torch.LongTensor([int(spk_ids[i])]).cuda()
            t = dt.datetime.now()
            y_enc, y_dec, attn = generator.forward(x, x_lengths, n_timesteps=args.timesteps, temperature=1.5,
                                                   stoc=False, spk=spk, length_scale=0.91)
            y_dec = y_dec.squeeze(0).transpose(0, 1).cpu().numpy()
            # print(y_dec.max(), y_dec.min())
            y_dec = np.exp(y_dec)
            y_dec = np.log10(y_dec)
            print(y_dec.shape, y_dec.max(), y_dec.min())

            write_hdf5(
                os.path.join(args.output_dir, f"{utt_ids[i]}.h5"),
                "feats",
                y_dec.astype(np.float32),
            )
            audio = torch.rand(y_dec.shape[0] * 256)
            print(torch.max(audio), torch.min(audio))
            write_hdf5(
                os.path.join(args.output_dir, f"{utt_ids[i]}.h5"),
                "wave",
                audio.cpu().numpy().astype(np.float32),
            )
            # h5filepath = os.path.join(args.output_dir, f"{utt_ids[i]}.h5")
    
    # cmd = "rsync --info=progress2 " + args.output_dir + ' xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/ -r'
    # print(cmd)
    # os.system(cmd)

            