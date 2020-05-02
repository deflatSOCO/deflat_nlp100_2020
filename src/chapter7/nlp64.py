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

def nlp_64():
    """
    どうしてもメモリ不足で動作しなかったため、Google Colab.上に環境を再現し実行した。
    """
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
        os.path.join(data_dir_path,'GoogleNews-vectors-negative300.bin.gz'),
        binary=True
    )
    with open(os.path.join(data_dir_path,"questions-words.txt"),encoding="utf-8") as f1:
        with open(os.path.join(result_dir_path,"result_64.txt"),"w",encoding="utf-8", newline="\n") as f2:
            line_lists = [l for l in f1.read().split("\n") if len(l)>0]
            for l in tqdm(line_lists,desc="proc"):
                if l[0]==":":
                    f2.write(l+"\n")
                else:
                    a,b,c,d = l.split()
                    e = w2v_model.most_similar(positive=[b, c], negative=[a], topn=1)[0][0]
                    f2.write("{} {}\n".format(l, e))
                    


if __name__ == "__main__":
    nlp_64()