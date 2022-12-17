import subprocess
import os

# Creating folders
paths = ['input',
         'output']

for i in range(len(paths)):
    if not os.path.exists(paths[i]):
        os.makedirs(paths[i])

cmd1 = 'pip install flask flask_cors'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'pip install -qq -U diffusers==0.8.0 transformers ftfy'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'pip install git+https://github.com/huggingface/diffusers.git'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'pip install accelerate'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'curl -O https://pagekite.net/pk/pagekite.py'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'git config --global user.email "vatsal2473@gmail.com"'
p1 = subprocess.call(cmd1, shell=True)

cmd1 = 'git config --global user.name "vatsal2473"'
p1 = subprocess.call(cmd1, shell=True)

print("\nhuggingface-cli login\n")

