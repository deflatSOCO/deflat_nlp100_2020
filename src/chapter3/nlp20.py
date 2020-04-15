import os
import sys
import math
import re
import json
from collections import Counter

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter3")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter3")

def nlp_20():
    with open(os.path.join(data_dir_path,"jawiki-country.json"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    for l in data_line:
        js = json.loads(l)
        if js["title"] == "イギリス":
            with open(os.path.join(result_dir_path,"england.txt"), "w", encoding="utf-8", newline="\n") as f:
                f.write(js["text"])
            break
    
if __name__ == "__main__":
    nlp_20()