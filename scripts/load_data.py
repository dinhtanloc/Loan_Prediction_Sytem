import os
import shutil

import kagglehub

from path_configs import *

# Download latest version
path = kagglehub.dataset_download("taweilo/loan-approval-classification-data")

print("Path to dataset files:", path)


os.makedirs(data_dir, exist_ok=True)

for filename in os.listdir(path):
    src = os.path.join(path, filename)
    dst = os.path.join(data_dir, filename)

    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)

print("➡️ Dataset copied to:", data_dir)