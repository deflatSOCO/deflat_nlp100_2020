import os
import sys
import re

import pandas as pd
import numpy as np

import gensim
from scipy.cluster.hierarchy import dendrogram, linkage
from tqdm import tqdm

import matplotlib.pyplot as plt

from typing import List, Tuple

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter7")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter7")

def pickup_country_name() -> List[str]:
    ret = []
    flag=False
    with open(os.path.join(data_dir_path,"questions-words.txt"),encoding="utf-8") as f:
        for l in tqdm(f.read().split("\n"),desc="proc"):
            if len(l)==0: continue
            elif l[0]==":":
                flag = re.match(r": capital", l) is not None
            elif flag:
                wlist = l.split()
                ret += [wlist[1],wlist[3]]
    return sorted(set(ret))

def nlp_68():
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
        os.path.join(data_dir_path,'GoogleNews-vectors-negative300.bin.gz'),
        binary=True
    )

    country_name = pickup_country_name()
    X = np.array([w2v_model[w] for w in country_name])

    model = linkage(X, method="ward")
    plt.clf()
    dendrogram(model, labels=country_name)
    plt.savefig(os.path.join(result_dir_path,"result_68.png"))

if __name__ == "__main__":
    nlp_68()