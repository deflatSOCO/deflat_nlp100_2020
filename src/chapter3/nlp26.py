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

def nlp_26():
    with open(os.path.join(result_dir_path,"england.txt"), "r", encoding="utf-8") as f:
        data = f.read()
    info = re.search(r"\{\{基礎情報 国(\n.+?\n\})\}", data, re.DOTALL).groups()[0]
    info_lines = re.findall("(?=\n\|(.+?)\s*=\s*(.+?)\n[\|\}])", info, flags=re.DOTALL)
    info_dict = {}
    for k,v in info_lines:
        vv = re.sub(r"'{2,5}(.+?)'{2,5}", r"\1", v)
        info_dict[k]=vv

    print(json.dumps(info_dict, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    nlp_26()