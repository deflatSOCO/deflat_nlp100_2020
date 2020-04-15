import os
import sys
import math
import re
import json
from collections import Counter

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_19():
    with open(os.path.join(data_dir_path,"popular-names.txt"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    names = [e.split("\t")[0] for e in data_line]
    names_count = Counter(names)
    names_uniq = list(set(names))
    names_uniq.sort(key=lambda x: -names_count[x])
    print("\n".join(names_uniq))
    
if __name__ == "__main__":
    nlp_19()