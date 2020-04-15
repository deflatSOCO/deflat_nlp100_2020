import os
import sys
import math
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_17():
    with open(os.path.join(data_dir_path,"popular-names.txt"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    names = [e.split("\t")[0] for e in data_line]
    names_uniq = sorted(set(names))
    print("\n".join(names_uniq))
    
if __name__ == "__main__":
    nlp_17()