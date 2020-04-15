import os
import re
import json

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter2","popular-names.txt")

def nlp_10():
    with open(data_path, "r", encoding="utf-8") as f:
        data = f.readlines()
    print(len(data))

if __name__ == "__main__":
    nlp_10()