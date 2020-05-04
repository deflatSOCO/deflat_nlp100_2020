import os
import sys
import re
import pandas as pd
import numpy as np
import gensim
from nltk import tokenize

from typing import List, Tuple


THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
w2v_model_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter7")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter8")


w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
    os.path.join(w2v_model_dir_path,'GoogleNews-vectors-negative300.bin.gz'),
    binary=True
)

def read_df(file_path: str) -> pd.DataFrame:
    return pd.read_csv(
        file_path,
        encoding="utf-8",
        sep="\t",
        header=None
    )

def preprocess(s: str) -> str:
    ret = s.lower()
    ret = re.sub(r"[^a-zA-Z\d']", " ", ret)
    return ret

def get_vec(s: str) -> np.array:
    global w2v_model
    wlist = tokenize.word_tokenize(s)
    vecs = [w2v_model[w] if w in w2v_model.vocab else np.zeros(shape=(w2v_model.vector_size,)) for w in wlist]
    ret = np.mean(np.array(vecs), axis=0)
    return ret

def get_X(data: pd.DataFrame) ->np.array:
    vecs = data[1].apply(preprocess).apply(get_vec)
    return np.array(vecs.tolist())

def get_y(data: pd.DataFrame) ->np.array:
    convert_table = {"b":0,"t":1,"e":2,"m":3}
    return data[4].replace(convert_table).values

def nlp_70():

    train_data = read_df(os.path.join(data_dir_path, "train.txt"))
    valid_data = read_df(os.path.join(data_dir_path, "valid.txt"))
    test_data = read_df(os.path.join(data_dir_path, "test.txt"))

    X_train = get_X(train_data)
    y_train = get_y(train_data)
    X_valid = get_X(valid_data)
    y_valid = get_y(valid_data)
    X_test = get_X(test_data)
    y_test = get_y(test_data)
    np.save(os.path.join(result_dir_path, "train_X.npy"), X_train)
    np.save(os.path.join(result_dir_path, "train_y.npy"), y_train)
    np.save(os.path.join(result_dir_path, "valid_X.npy"), X_valid)
    np.save(os.path.join(result_dir_path, "valid_y.npy"), y_valid)
    np.save(os.path.join(result_dir_path, "test_X.npy"), X_test)
    np.save(os.path.join(result_dir_path, "test_y.npy"), y_test)

if __name__ == "__main__":
    nlp_70()