import os
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter2")

def nlp_13():
    with open(os.path.join(result_dir_path,"col1.txt"), "r", encoding="utf-8") as f:
        col1_line = f.readlines()
    with open(os.path.join(result_dir_path,"col2.txt"), "r", encoding="utf-8") as f:
        col2_line = f.readlines()
    joint_list = [a.rstrip("\n") + "\t" + b.rstrip("\n") + "\n" for a,b in zip(col1_line, col2_line)]
    with open(os.path.join(result_dir_path,"nlp13.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.writelines(joint_list)
    
if __name__ == "__main__":
    nlp_13()