import os
import sys
import re
import pandas as pd
import numpy as np
from typing import List, Tuple
import pickle

from feature_generator import *
from wordlist_generator import WordListGenerator

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def save_file(array: np.array, output_file: str):
    np.savetxt(output_file, array)
    

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


def nlp_51():
    train_data = preproc_data(
        os.path.join(data_dir_path, "train.txt")
    )
    valid_data = preproc_data(
        os.path.join(data_dir_path, "valid.txt")
    )
    test_data = preproc_data(
        os.path.join(data_dir_path, "test.txt")
    )
    title_vectorizer = TfIdf(min_df=0.001, max_df=0.9)
    title_vectorizer.fit(train_data["TITLE"])

    with open(os.path.join(result_dir_path,"vectorizer.pkl"),"wb") as f:
        pickle.dump(title_vectorizer, f)

    train_np, train_w = generate_np(train_data, title_vectorizer)
    valid_np, valid_w = generate_np(valid_data, title_vectorizer)
    test_np, test_w = generate_np(test_data, title_vectorizer)
    
    save_file(train_np, os.path.join(result_dir_path,"train.feature.txt"))
    save_file(valid_np, os.path.join(result_dir_path,"valid.feature.txt"))
    save_file(test_np, os.path.join(result_dir_path,"test.feature.txt"))
    with open(os.path.join(result_dir_path,"feature_word.txt"), "w", newline="\n",encoding="utf-8")as f:
        f.write("\n".join(train_w))

    train_label = generate_label(train_data)
    valid_label = generate_label(valid_data)
    test_label = generate_label(test_data)

    save_file(train_label, os.path.join(result_dir_path,"train.label.txt"))
    save_file(valid_label, os.path.join(result_dir_path,"valid.label.txt"))
    save_file(test_label, os.path.join(result_dir_path,"test.label.txt"))
    

if __name__ == "__main__":
    nlp_51()