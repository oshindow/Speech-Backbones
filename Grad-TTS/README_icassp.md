1. python3.8+

conda install python=3.9
pip install tiktoken
pip install numpy==1.26.4
pip install tqdm
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1+cu117 -f https://download.pytorch.org/whl/torch_stable.html
pip install tensorboard
pip install six
pip install Cython
cd model/monotonic_align; mkdir -p model/monotonic_align; python setup.py build_ext --inplace; cd ../..
pip install einops
pip install numba
pip install librosa
pip install unidecode
matplotlib
h5py
flask
inflect
jieba
pyymal
ParallelWaveGAN (cd ParallelWaveGAN;pip install -e .)