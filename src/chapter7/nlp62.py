import os
import sys
import re

import pandas as pd
import gensim
from tqdm import tqdm

from typing import List, Tuple

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter7")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter7")

def nlp_62():
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
        os.path.join(data_dir_path,'GoogleNews-vectors-negative300.bin'),
        binary=True
    )
    vocab = list(w2v_model.vocab.keys())
    similarity = {}
    for w in tqdm(vocab):
        if w == "United_States": continue
        similarity[w] = w2v_model.similarity("United_States",w)
    sim_ser = pd.Series(similarity).sort_values(ascending=False)
    print(sim_ser.head(10))

# 本来は以下で十分だが、メモリが足りず動作しなかった。
#    print(w2v_model.similar_by_word("United_States", topn=10))


if __name__ == "__main__":
    nlp_62()