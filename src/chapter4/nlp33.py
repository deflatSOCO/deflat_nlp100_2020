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
    

def nlp_33():
    result = parse_mecab_result(
        os.path.join(data_dir_path,"neko.txt.mecab")
    )
    ret = set()
    for i in range(len(result)-2):
        if result[i]["pos"] == "名詞" and result[i+2]["pos"] == "名詞" and result[i+1]["surface"] == "の":
            ret_str = result[i]["surface"] + result[i+1]["surface"] + result[i+2]["surface"]
            ret |= {ret_str}
    print("\n".join(sorted(ret)))

if __name__ == "__main__":
    nlp_33()