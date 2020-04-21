import os
import sys
import re
import json
from tqdm import tqdm

from common import *

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter5")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter5")


def parse_cabocha_result_for_nlp40(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
    header_pat = re.compile(r"^\* \d+ .+?D \d+/\d+ .+\n")
    ret = []
    cache = []
    for l in tqdm(data):
        if l == "EOS\n":
            if cache:
                ret.append(parse_sentence_result(cache))
            cache = []
        elif re.search(header_pat, l)is None:
            cache.append(l)
    return ret

def nlp_40():
    morph_lists = parse_cabocha_result_for_nlp40(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )
    for e in morph_lists[2]:
        print(e)

if __name__ == "__main__":
    nlp_40()