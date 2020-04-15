import os
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_12():
    with open(os.path.join(data_dir_path,"popular-names.txt"), "r", encoding="utf-8") as f:
        data_line = f.readlines()
    col1 = [e.split("\t")[0] for e in data_line]
    col2 = [e.split("\t")[1] for e in data_line]
    with open(os.path.join(result_dir_path,"col1.txt"), "w", encoding="utf-8",newline="\n") as f:
        f.write("\n".join(col1))
    with open(os.path.join(result_dir_path,"col2.txt"), "w", encoding="utf-8",newline="\n") as f:
        f.write("\n".join(col2))
    
if __name__ == "__main__":
    nlp_12()