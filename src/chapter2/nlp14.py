import os
import sys
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_14(N: int):
    with open(os.path.join(data_dir_path,"popular-names.txt"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    data_head = data_line[:N]
    print("".join(data_head))
    
if __name__ == "__main__":
    N = int(sys.argv[1])
    nlp_14(N)