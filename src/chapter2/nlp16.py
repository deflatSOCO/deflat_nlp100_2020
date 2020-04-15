import os
import sys
import math
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_16(N: int):
    with open(os.path.join(data_dir_path,"popular-names.txt"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    l = len(data_line)
    for i in range(N):
        part = data_line[math.ceil(l/N *i):math.ceil(l/N*(i+1))]
        with open(os.path.join(result_dir_path, "split_{}.txt".format(i)), "w", encoding="utf-8", newline="\n") as f:
            f.writelines(part)
    
if __name__ == "__main__":
    N = int(sys.argv[1])
    nlp_16(N)