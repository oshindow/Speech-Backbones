# # % Grad-TTS (spk-MCD) & logs/new_exp_sg P1
# echo "% Grad-TTS (spk-MCD) & logs/new_exp_sg P1"
# python dump_feats_to_GPU4_P1.py -f resources/filelists/synthesis_zh_acc_paper.txt -c logs/new_exp_sg/grad_400.pt -o logs/new_exp_sg/gen_grad_400/raw

# input_path=new_exp_sg/gen_grad_400/raw 
# output_path=gen_grad_400_P1/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# # % Grad-TTS (spk/acc-MCD+MC) & logs/new_exp_sg_acc P2
# echo "% Grad-TTS (spk/acc-MCD+MC) & logs/new_exp_sg_acc P2"
# python dump_feats_to_GPU4_zh_acc.py -f resources/filelists/synthesis_zh_acc_paper.txt -c logs/new_exp_sg_acc/grad_270.pt -o logs/new_exp_sg_acc/gen_grad_270/raw

# input_path=new_exp_sg_acc/gen_grad_270/raw 
# output_path=gen_grad_270_P2/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# # % Grad-TTS (spk/acc-MCD+MC-blk) & logs/new_exp_sg_acc_blk P3 
# echo "% Grad-TTS (spk/acc-MCD+MC-blk) & logs/new_exp_sg_acc_blk P3"
# python dump_feats_to_GPU4_zh_acc_blank.py -f resources/filelists/synthesis_zh_acc_paper.txt -c logs/new_exp_sg_acc_blank_E3/grad_30.pt -o logs/new_exp_sg_acc_blank_E3/gen_grad_30/raw

# input_path=new_exp_sg_acc_blank_E3/gen_grad_30/raw 
# output_path=gen_grad_30_P3/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# !!!! # % Grad-TTS-Conformer (spk/acc-MCD+MC-blk) & logs/new_exp_sg_acc_blk_conformer P4 - blank conformer
# echo "% Grad-TTS-Conformer (spk/acc-MCD+MC-blk) & logs/new_exp_sg_acc_blk_conformer P4"
# python dump_feats_to_GPU4_zh_conformer.py -f resources/filelists/synthesis_zh_acc_paper.txt -c logs/new_exp_sg_acc_blank_conformer_E4/grad_30.pt -o logs/new_exp_sg_acc_blank_conformer_E4/gen_grad_30/raw

# input_path=new_exp_sg_acc_blank_conformer_E4/gen_grad_30/raw 
# output_path=gen_grad_30_P4/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# % Proposed Model E16
# echo "% Proposed Model E16"
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl_E16.py -f resources/filelists/synthesis_zh_acc_paper.txt -c logs/new_exp_sg_acc_blank_conformer_gst_E16/grad_400.pt -o logs/new_exp_sg_acc_blank_conformer_gst_E16/gen_grad_400/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E16/gen_grad_400/raw 
# output_path=gen_grad_400_E16_ours/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# # ablation
# # w/o gst loss: 
# # w/o phoneme-level accent tokens: E7
echo "w/o phoneme-level accent tokens: E7"
python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss.py -f resources/filelists/synthesis_zh_acc_paper.txt -c logs/new_exp_sg_acc_blank_conformer_gst_E7/grad_330.pt -o logs/new_exp_sg_acc_blank_conformer_gst_E7/gen_grad_330/raw

input_path=new_exp_sg_acc_blank_conformer_gst_E7/gen_grad_330/raw 
output_path=gen_grad_330_E7/
rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# input_path=new_exp_sg_acc_blank_conformer_gst_E7/gen_grad_334/raw
# output_path=gen_grad_334_E7/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r


## E8
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln.py -f resources/filelists/synthesis_zh_acc.txt -c logs/new_exp_sg_acc_blank_conformer_gst_E8/grad_400.pt -o logs/new_exp_sg_acc_blank_conformer_gst_E8/gen_grad_400/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E8/gen_grad_400/raw 
# output_path=gen_grad_400_E8/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# E16
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl_E16.py -f resources/filelists/synthesis_zh_acc.txt -c logs/new_exp_sg_acc_blank_conformer_gst_E16/grad_400.pt -o logs/new_exp_sg_acc_blank_conformer_gst_E16/gen_grad_400/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E16/gen_grad_400/raw 
# output_path=gen_grad_400_E16/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# E10
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl.py -f resources/filelists/synthesis_zh_acc.txt -c logs/new_exp_sg_acc_blank_conformer_gst_E10/grad_300.pt -o logs/new_exp_sg_acc_blank_conformer_gst_E10/gen_grad_300/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E10/gen_grad_300/raw 
# output_path=gen_grad_300_E10/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# E12
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl_E12.py \
#     -f resources/filelists/synthesis_zh_acc.txt \
#     -c logs/new_exp_sg_acc_blank_conformer_gst_E12/grad_100.pt \
#     -o logs/new_exp_sg_acc_blank_conformer_gst_E12/gen_grad_100_male/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E12/gen_grad_100_male/raw 
# output_path=gen_grad_100_E12_male/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# E14 base
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl_E12.py \
#     -f resources/filelists/synthesis_zh_acc.txt \
#     -c logs/new_exp_sg_acc_blank_conformer_gst_E14/grad_253.pt \
#     -o logs/new_exp_sg_acc_blank_conformer_gst_E14/gen_grad_253_male/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E14/gen_grad_253_male/raw 
# output_path=gen_grad_253_E14_male/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# E13
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl_E12.py \
#     -f resources/filelists/synthesis_zh_acc.txt \
#     -c logs/new_exp_sg_acc_blank_conformer_gst_E13/grad_251.pt \
#     -o logs/new_exp_sg_acc_blank_conformer_gst_E13/gen_grad_251_male/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E13/gen_grad_251_male/raw 
# output_path=gen_grad_251_E13_male/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# E15
# python dump_feats_to_GPU4_zh_acc_blank_conformer_gstloss_cln_grl_E12.py \
#     -f resources/filelists/synthesis_zh_acc.txt \
#     -c logs/new_exp_sg_acc_blank_conformer_gst_E15/grad_500.pt \
#     -o logs/new_exp_sg_acc_blank_conformer_gst_E15/gen_grad_500_male/raw

# input_path=new_exp_sg_acc_blank_conformer_gst_E15/gen_grad_500_male/raw 
# output_path=gen_grad_500_E15_male/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r


# input_path=new_exp_sg_acc_blank_conformer_gst_E5/gen_grad_407/raw 
# output_path=gen_grad_407_E6/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r

# input_path=new_exp_sg_acc_blank_conformer_gst_E5/gen_grad_333/raw 
# output_path=gen_grad_333_E6/
# rsync --info=progress2 /home/xintong/Speech-Backbones/Grad-TTS/logs/$input_path xintong@smc-gpu4.d2.comp.nus.edu.sg:/home/xintong/ParallelWaveGAN/egs/csmsc/voc1/dump/magichub_sg_16k_gen/eval/$output_path -r



