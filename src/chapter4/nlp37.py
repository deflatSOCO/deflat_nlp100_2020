import os
import sys
import re
import json
from collections import Counter

import matplotlib.pyplot as plt
import japanize_matplotlib

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter4")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter4")

def parse_mecab_result(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()
    ret = []
    for l in data:
        if l == "EOS\n": break
        surface, info = l.split("\t")
        info_split = info.split(",")
        ret.append(
            {
                "surface":surface,
                "base":info_split[6],
                "pos":info_split[0],
                "pos1":info_split[1]
            }
        )
    return ret
    

def nlp_37():
    result = parse_mecab_result(
        os.path.join(data_dir_path,"neko.txt.mecab")
    )
    gram_word = []
    for i in range(1,len(result)-1):
        if result[i]["surface"] == "猫":
            gram_word.append(result[i-1]["surface"])
            gram_word.append(result[i+1]["surface"])
    
    cnt = Counter(gram_word).most_common()
    top_words = [e[0] for e in cnt[:10]]
    top_count = [e[1] for e in cnt[:10]]

    plt.bar(top_words, top_count)
    plt.show()

if __name__ == "__main__":
    nlp_37()