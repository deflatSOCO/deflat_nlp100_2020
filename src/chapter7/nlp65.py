import os
import sys
import re

import pandas as pd
import numpy as np

import gensim
from tqdm import tqdm

from typing import List, Tuple

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter7")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter7")

def nlp_65():
    semantic_total = 0
    semantic_correct = 0
    syntactic_total = 0
    syntactic_correct = 0
    pattern_flag = -1
    with open(os.path.join(result_dir_path,"result_64.txt"),encoding="utf-8") as f:
        for l in tqdm(f.read().split("\n"),desc="proc"):
            if len(l)==0: continue
            if l[0]==":":
                if re.match(r": gram\d", l) is not None:
                    pattern_flag = 1
                else:
                    pattern_flag = 0
            else:
                wlist = l.split()
                pred_word = wlist[-1]
                corr_word = wlist[-2]
                if pred_word == corr_word:
                    if pattern_flag == 0:
                        semantic_correct += 1
                    else:
                        syntactic_correct += 1
                if pattern_flag == 0:
                    semantic_total += 1
                else:
                    syntactic_total += 1
    print("Semantic analogy: {} / {} ({})".format(semantic_correct, semantic_total,semantic_correct/semantic_total))
    print("Semantic analogy: {} / {} ({})".format(syntactic_correct, syntactic_total,syntactic_correct/syntactic_total))


if __name__ == "__main__":
    nlp_65()