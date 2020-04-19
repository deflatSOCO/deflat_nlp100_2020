import os
import sys
import re
import json
from collections import Counter

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
    

def nlp_35():
    result = parse_mecab_result(
        os.path.join(data_dir_path,"neko.txt.mecab")
    )
    result_s = [e["surface"] for e in result]
    cnt = Counter(result_s).most_common()
    cnt_words = [e[0] for e in cnt]
    print("\n".join(cnt_words))

if __name__ == "__main__":
    nlp_35()