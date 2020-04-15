import os
import sys
import math
import re
import json
import itertools
from collections import Counter

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter3")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter3")

def nlp_24():
    with open(os.path.join(result_dir_path,"england.txt"), "r", encoding="utf-8") as f:
        data = f.readlines()
    files = [l for l in data if "ファイル:" in l]
    reg = re.compile(r"ファイル:(.+?)[|\]]")
    file_names = [re.findall(reg, l) for l in files]
    file_list = list(itertools.chain.from_iterable(file_names))
    print("\n".join(file_list))    
if __name__ == "__main__":
    nlp_24()