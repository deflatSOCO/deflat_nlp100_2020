import os
import sys
import math
import re
import json
from collections import Counter

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter3")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter3")

def nlp_23():
    with open(os.path.join(result_dir_path,"england.txt"), "r", encoding="utf-8") as f:
        data = f.read()
    categories = re.findall("([=]+)\s*(.+?)\s*([=]+)\n", data)
    for c in categories:
        print(c[1], len(c[0])-1)
    
if __name__ == "__main__":
    nlp_23()