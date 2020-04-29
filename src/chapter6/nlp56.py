import os
import sys
import re
import pandas as pd
import numpy as np
import json
from typing import List, Tuple
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt


THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def calc_and_print_stat(y_corr: np.array, y_pred: np.array, label:List[str], average_type:str=None):
    precision = precision_score(y_corr, y_pred, average=average_type)
    recall = recall_score(y_corr, y_pred, average=average_type)
    f1 = f1_score(y_corr, y_pred, average=average_type)
    if average_type is None:
        for i,l in enumerate(label):
            print("Precision ({}):\t{}".format(l, precision[i]))
            print("Recall ({}):\t{}".format(l, recall[i]))
            print("F1-Score ({}):\t{}".format(l, f1[i]))
    else:
        print("Precision ({}):\t{}".format(average_type, precision))
        print("Recall ({}):\t{}".format(average_type, recall))
        print("F1-Score ({}):\t{}".format(average_type, f1))


def get_result_stat(model:LogisticRegression, X:np.array, y:np.array):
    y_pred = model.predict(X)
    calc_and_print_stat(y, y_pred, ["Business","Science&Tech.","Entertainment","Health"], None)
    print("\n")
    calc_and_print_stat(y, y_pred, ["micro"], "micro")
    print("\n")
    calc_and_print_stat(y, y_pred, ["macro"], "macro")
    print("\n")


def load_file(input_file: str, dtype:type=float) -> np.array:
    return np.loadtxt(input_file,dtype=dtype)

def nlp_56():
    with open(os.path.join(result_dir_path, "trained_model.pkl"),"rb") as f:
        model = pickle.load(f)
    train_X = load_file(
        os.path.join(result_dir_path,"train.feature.txt"), dtype=float
    )
    train_y = load_file(
        os.path.join(result_dir_path,"train.label.txt"), dtype=int
    )
    print("--- training_data ---\n")
    get_result_stat(model, train_X, train_y)
    print("---------------------")
    test_X = load_file(
        os.path.join(result_dir_path,"test.feature.txt"), dtype=float
    )
    test_y = load_file(
        os.path.join(result_dir_path,"test.label.txt"), dtype=int
    )
    print("--- test_data ---\n")
    get_result_stat(model, test_X, test_y)
    print("---------------------")

if __name__ == "__main__":
    nlp_56()