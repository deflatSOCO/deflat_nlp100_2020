import os
import sys
import re
import pandas as pd
import numpy as np
from typing import List, Tuple
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import pickle

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def save_file(array: np.array, output_file: str):
    np.savetxt(output_file, array)

def load_file(input_file: str, dtype:type=float) -> np.array:
    return np.loadtxt(input_file,dtype=dtype)

def nlp_52():
    train_X = load_file(
        os.path.join(result_dir_path,"train.feature.txt"), dtype=float
    )
    train_Y = load_file(
        os.path.join(result_dir_path,"train.label.txt"), dtype=int
    )
    model = LogisticRegression(max_iter=1000,verbose=1)
    model.fit(train_X, train_Y)
    
    with open(os.path.join(result_dir_path, "trained_model.pkl"),"wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    nlp_52()