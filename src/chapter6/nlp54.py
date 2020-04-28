import os
import sys
import re
import pandas as pd
import numpy as np
import json
from typing import List, Tuple
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import pickle

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def get_accuracy(model:LogisticRegression, X:np.array, y:np.array) -> float:
    y_pred = model.predict(X)
    return sum(y==y_pred) / y.shape[0]

def load_file(input_file: str, dtype:type=float) -> np.array:
    return np.loadtxt(input_file,dtype=dtype)

def nlp_54():
    with open(os.path.join(result_dir_path, "trained_model.pkl"),"rb") as f:
        model = pickle.load(f)
    train_X = load_file(
        os.path.join(result_dir_path,"train.feature.txt"), dtype=float
    )
    train_y = load_file(
        os.path.join(result_dir_path,"train.label.txt"), dtype=int
    )
    print("Train accucacy: {}".format(
        get_accuracy(model, train_X, train_y)
    ))
    test_X = load_file(
        os.path.join(result_dir_path,"test.feature.txt"), dtype=float
    )
    test_y = load_file(
        os.path.join(result_dir_path,"test.label.txt"), dtype=int
    )
    print("Test accucacy: {}".format(
        get_accuracy(model, test_X, test_y)
    ))


if __name__ == "__main__":
    nlp_54()