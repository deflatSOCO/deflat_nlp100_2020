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


def nlp_57():
    with open(os.path.join(result_dir_path, "trained_model.pkl"),"rb") as f:
        model = pickle.load(f)
    with open(os.path.join(result_dir_path, "feature_word.txt"), encoding="utf-8") as f:
        word_label = f.read().split("\n")
    category_label = ["Business","Science&Tech.","Entertainment","Health"]

    for i,c in enumerate(category_label):
        word_and_weight = pd.DataFrame({
            "word":word_label,
            "weight":list(model.coef_[i])
        }).sort_values(by="weight",ascending=False).reset_index(drop=True)

        print("--- {} ---".format(c))
        print("top_10:")
        print(word_and_weight.head(10))
        print("buttom_10:")
        print(word_and_weight.tail(10))


if __name__ == "__main__":
    nlp_57()