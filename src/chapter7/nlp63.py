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

def cosine_sim(v1:np.array, v2:np.array) ->float:
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def nlp_63():
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
        os.path.join(data_dir_path,'GoogleNews-vectors-negative300.bin'),
        binary=True
    )

# 本来は以下で十分だが、メモリが足りず動作しなかった。
#   w2v_model.most_similar(positive=["Spain", "Athens"], negative=["Madrid"], topn=10)

# 以下、メモリ不足対応のための代替手段
    target_vec = w2v_model["Spain"] - w2v_model["Madrid"] + w2v_model["Athens"]
    vocab = list(w2v_model.vocab.keys())
    similarity = {}
    for w in tqdm(vocab):
        similarity[w] = cosine_sim(target_vec, w2v_model[w])
    sim_ser = pd.Series(similarity).sort_values(ascending=False)
    print(sim_ser.head(10))


if __name__ == "__main__":
    nlp_63()