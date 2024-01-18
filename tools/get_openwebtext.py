import datasets
import os
import re

dataset = datasets.load_dataset('openwebtext', split='train', data_files='/home/oem/lifanwu/openwebtext')

os.makedirs("data/openwebtext", exist_ok=True)

num = 0
with open("data/openwebtext/data.txt", "w") as f:
    for data in dataset:
        f.write(re.sub(r"\n+", "<@x(x!>", data['text']) + "\n")
        num += 1

print("Number of lines:", num)