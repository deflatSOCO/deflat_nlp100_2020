import os
import sys
import re
import json

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
    

def nlp_32():
    result = parse_mecab_result(
        os.path.join(data_dir_path,"neko.txt.mecab")
    )
    ret = set()
    for e in result:
        if e["pos"] == "動詞":
            ret |= {e["base"]}
    print("\n".join(sorted(ret)))

if __name__ == "__main__":
    nlp_32()