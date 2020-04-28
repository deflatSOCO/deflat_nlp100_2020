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

from wordlist_generator import WordListGenerator
from feature_generator import TfIdf

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def predict_category(title: str) ->str:
    with open(os.path.join(result_dir_path, "trained_model.pkl"),"rb") as f:
        model = pickle.load(f)
    with open(os.path.join(result_dir_path,"vectorizer.pkl"),"rb") as f:
        vectorizer = pickle.load(f)
    tokenizer = WordListGenerator(lemma=True, keep_pos=["N","V","A"] ,drop_stopword=True)
    data = pd.Series([title])
    data_token = tokenizer.tokenize_series(data)
    data_vec, fname = vectorizer.transform(data_token)
    proba = model.predict_proba(data_vec)
    ret = {
        "Business":proba[0][0],
        "Science&Tech.":proba[0][1],
        "Entertainment":proba[0][2],
        "Health":proba[0][3]
    }
    return ret

def nlp_53():
    title="Omega's Cooperman says eBay should spin off portion of PayPal"
    ret = predict_category(title)
    print(json.dumps(ret, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    nlp_53()