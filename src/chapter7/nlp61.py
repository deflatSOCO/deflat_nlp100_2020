import os
import sys
import re
import gensim
from typing import List, Tuple


THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter7")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter7")

def nlp_61():
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
        os.path.join(data_dir_path,'GoogleNews-vectors-negative300.bin'),
        binary=True
    )
    print(w2v_model.similarity("United_States", "U.S."))


if __name__ == "__main__":
    nlp_61()