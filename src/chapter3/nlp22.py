import os
import sys
import math
import re
import json
import itertools
from collections import Counter

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter3")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter3")

def nlp_22():
    with open(os.path.join(result_dir_path,"england.txt"), "r", encoding="utf-8") as f:
        data = f.readlines()
    categories = [l for l in data if "Category:" in l]
    reg = re.compile(r"^\[\[Category:(.+?)[|\]]")
    category_names = [re.findall(reg,l) for l in categories]
    category_uniq = set(itertools.chain.from_iterable(category_names))
    print("\n".join(sorted(category_uniq)))
    
if __name__ == "__main__":
    nlp_22()