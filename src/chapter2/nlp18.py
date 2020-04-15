import os
import sys
import math
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_18():
    with open(os.path.join(data_dir_path,"popular-names.txt"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    data_line.sort(key=lambda x: -int(x.split("\t")[2]))
    print("".join(data_line))
    
if __name__ == "__main__":
    nlp_18()