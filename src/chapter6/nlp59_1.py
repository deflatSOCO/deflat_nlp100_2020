import os
import sys
import re
import pandas as pd
import numpy as np
import json
from typing import List, Tuple
import pickle
from collections import OrderedDict
import itertools

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn import preprocessing
import matplotlib.pyplot as plt

from feature_generator import *
from wordlist_generator import WordListGenerator

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")

def preproc_data(input_file:str):
    data = pd.read_csv(
        input_file,
        header=None,
        sep="\t"
    )
    data = data[[0,1,4]]
    wg = WordListGenerator(lemma=True, keep_pos=["N","V","A"] ,drop_stopword=True)
    ret = pd.DataFrame({
        "ID": data[0],
        "TITLE": wg.tokenize_series(data[1]),
        "CATEGORY": data[4]
    })
    return ret

def generate_np(df: pd.DataFrame, title_vec: FeatureGenerator) -> Tuple[np.array,List[str]]:
    arrays, words = title_vec.transform(df["TITLE"])
    return (arrays, words)

def generate_label(df: pd.DataFrame) ->np.array:
    convert_table = {"b":0,"t":1,"e":2,"m":3}
    return df["CATEGORY"].replace(convert_table).values

def generate_params(min_df:float, max_df:float) ->dict:
    train_data = preproc_data(
        os.path.join(data_dir_path, "train.txt")
    )
    test_data = preproc_data(
        os.path.join(data_dir_path, "test.txt")
    )
    title_vectorizer = TfIdf(min_df=min_df, max_df=max_df)
    title_vectorizer.fit(train_data["TITLE"])

    with open(os.path.join(result_dir_path,"vectorizer.pkl"),"wb") as f:
        pickle.dump(title_vectorizer, f)

    train_X, w = generate_np(train_data, title_vectorizer)
    test_X, w = generate_np(test_data, title_vectorizer)
    train_y = generate_label(train_data)
    test_y = generate_label(test_data)
    print(train_X.shape)
    ret={
        "train_X":train_X,
        "train_y":train_y,
        "test_X":test_X,
        "test_y":test_y,
        "word_list":w
    }
    return ret

def train_model(penalty: str, X:np.array, y:np.array, solver:str) -> LogisticRegression:
    model = LogisticRegression(max_iter=1000, penalty=penalty, solver=solver)
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

def nlp_59_part1():
    """
    Part1: パラメータ抽出段階におけるminh_dffおよびmax_dfの最適値探索
    """

    min_df_cand = [0.0001]
    max_df_cand = [0.001,0.01,0.02,0.05,0.1]

    for min_df, max_df in itertools.product(*[min_df_cand, max_df_cand]):
        print("min_df={}, max_df={}".format(min_df, max_df))
        params = generate_params(min_df, max_df)        
        model = train_model("l2", params["train_X"], params["train_y"], "lbfgs")
        accuracy = get_accuracy(model,params["test_X"], params["test_y"])
        print("accuracy={}".format(accuracy))

if __name__ == "__main__":
    nlp_59_part1()