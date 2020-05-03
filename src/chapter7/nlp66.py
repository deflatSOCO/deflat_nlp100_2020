import os
import sys
import re

import pandas as pd
import numpy as np

import gensim
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt

from typing import List, Tuple

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter7")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter7")

def nlp_66():
    w2v_model = gensim.models.KeyedVectors.load_word2vec_format(
        os.path.join(data_dir_path,'GoogleNews-vectors-negative300.bin.gz'),
        binary=True
    )

    sim_data = pd.read_csv(
        os.path.join(data_dir_path,"combined.tab"),
        sep="\t",
        encoding="utf-8"
    )
    tqdm.pandas()
    sim_data["w2v"] = sim_data[["Word 1","Word 2"]].progress_apply(
        lambda x: w2v_model.similarity(x[0], x[1]),
        axis=1
    )

    sim_data["human_rank"] = sim_data["Human (mean)"].rank(method="min")
    sim_data["w2v_rank"] = sim_data["w2v"].rank(method="min")

    plt.clf()
    sns.scatterplot(data=sim_data, x="Human (mean)", y="w2v")
    plt.savefig(os.path.join(result_dir_path, "66_score_scatter.png"))

    plt.clf()
    sns.scatterplot(data=sim_data, x="human_rank", y="w2v_rank")
    plt.savefig(os.path.join(result_dir_path, "66_rank_scatter.png"))

    corr = sim_data[["human_rank","w2v_rank"]].corr(method="spearman")
    print(corr.iloc[0,1])

if __name__ == "__main__":
    nlp_66()