import os
import sys
import re
import pandas as pd
import numpy as np
import json
from typing import List, Tuple
import pickle
from collections import OrderedDict

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn import preprocessing
import matplotlib.pyplot as plt



THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def train_model(penalty: str, X:np.array, y:np.array, solver:str) -> LogisticRegression:
    model = LogisticRegression(max_iter=1000,verbose=1, penalty=penalty, solver=solver, l1_ratio=0.7)
    model.fit(X, y)
    return model

def get_accuracy(model:LogisticRegression, X:np.array, y:np.array) -> float:
    y_pred = model.predict(X)
    return sum(y==y_pred) / y.shape[0]

def generate_fig(accuracy_dict: OrderedDict, output_file:str):
    label = list(accuracy_dict.keys())
    val = [accuracy_dict[k] for k in label]
    left = [i+1 for i in range(len(label))]
    plt.clf()
    plt.bar(left, val, tick_label=label, align='center')
    plt.savefig(output_file)


def load_file(input_file: str, dtype:type=float) -> np.array:
    return np.loadtxt(input_file,dtype=dtype)

def nlp_58():
    train_X = load_file(
        os.path.join(result_dir_path,"train.feature.txt"), dtype=float
    )
    train_Y = load_file(
        os.path.join(result_dir_path,"train.label.txt"), dtype=int
    )
    valid_X = load_file(
        os.path.join(result_dir_path,"valid.feature.txt"), dtype=float
    )
    valid_Y = load_file(
        os.path.join(result_dir_path,"valid.label.txt"), dtype=int
    )
    test_X = load_file(
        os.path.join(result_dir_path,"test.feature.txt"), dtype=float
    )
    test_Y = load_file(
        os.path.join(result_dir_path,"test.label.txt"), dtype=int
    )    

    solver_penalty={
        "lbfgs":["l2","none"],
        "saga":["l1","l2","elasticnet","none"]
    }
    for solver in solver_penalty.keys():
        acc = OrderedDict()
        acc["train"] = OrderedDict()
        acc["valid"] = OrderedDict()
        acc["test"] = OrderedDict()
        
        for penalty in solver_penalty[solver]:
            model = train_model(penalty, train_X, train_Y, solver)
            acc["train"][penalty] = get_accuracy(model,train_X,train_Y)
            acc["valid"][penalty] = get_accuracy(model,valid_X,valid_Y)
            acc["test"][penalty] = get_accuracy(model,test_X,test_Y)
        for k in acc.keys():
            generate_fig(
                acc[k],
                os.path.join(result_dir_path, "58_{}_{}.png".format(solver, k))
            )

if __name__ == "__main__":
    nlp_58()