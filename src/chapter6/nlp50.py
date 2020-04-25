import os
import sys
import re
import pandas as pd

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter6")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter6")


def save_file(df: pd.DataFrame, output_file: str):
    df.to_csv(
        output_file,
        encoding="utf-8",
        line_terminator="\n",
        sep="\t",
        header=False,
        index=False,
    )

def nlp_50():
    data = pd.read_csv(
        os.path.join(data_dir_path, "newsCorpora.csv"),
        sep="\t",
        header=None
    )
    data.columns = [
        "ID",
        "TITLE",
        "URL",
        "PUBLISHER",
        "CATEGORY",
        "STORY",
        "HOSTNAME",
        "TIMESTAMP"
    ]
    pickup_publisher = [
        "Reuters",
        "Huffington Post",
        "Businessweek", 
        "Contactmusic.com", 
        "Daily Mail"
    ]
    data_pick = data[data["PUBLISHER"].isin(pickup_publisher)]
    data_shuffle = data_pick.sample(frac=1, random_state=0).reset_index(drop=True)
    n = data_shuffle.shape[0]
    train_ind = int(n*0.8)
    valid_ind = int(n*0.9)
    data_train = data_shuffle.iloc[:train_ind,:]
    data_valid = data_shuffle.iloc[train_ind:valid_ind,:]
    data_test = data_shuffle.iloc[valid_ind:,:]
    save_file(
        data_train,
        os.path.join(data_dir_path, "train.txt")
    )
    save_file(
        data_valid,
        os.path.join(data_dir_path, "valid.txt")
    )
    save_file(
        data_test,
        os.path.join(data_dir_path, "test.txt")
    )
if __name__ == "__main__":
    nlp_50()