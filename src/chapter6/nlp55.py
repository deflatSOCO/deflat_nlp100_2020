import os
import sys
import re
import pandas as pd
import numpy as np
import json
from typing import List, Tuple
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt


THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def get_cm(model:LogisticRegression, X:np.array, y:np.array, fig_path:str):
    y_pred = model.predict(X)
    cm = confusion_matrix(y, y_pred)
    sns.heatmap(cm, annot=True, cmap="Blues")
    plt.savefig(fig_path)
    plt.clf()

def load_file(input_file: str, dtype:type=float) -> np.array:
    return np.loadtxt(input_file,dtype=dtype)

def nlp_55():
    with open(os.path.join(result_dir_path, "trained_model.pkl"),"rb") as f:
        model = pickle.load(f)
    train_X = load_file(
        os.path.join(result_dir_path,"train.feature.txt"), dtype=float
    )
    train_y = load_file(
        os.path.join(result_dir_path,"train.label.txt"), dtype=int
    )
    get_cm(model, train_X, train_y, os.path.join(result_dir_path, "55_train.png"))
    test_X = load_file(
        os.path.join(result_dir_path,"test.feature.txt"), dtype=float
    )
    test_y = load_file(
        os.path.join(result_dir_path,"test.label.txt"), dtype=int
    )
    get_cm(model, test_X, test_y, os.path.join(result_dir_path, "55_test.png"))

if __name__ == "__main__":
    nlp_55()