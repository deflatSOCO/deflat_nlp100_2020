import os
import sys
import MeCab

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter4")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter4")

def prep():
    with open(os.path.join(data_dir_path,"neko.txt"), "r", encoding="utf-8") as f:
        data = f.read()
    m = MeCab.Tagger()
    ret = m.parse(data)
    with open(os.path.join(data_dir_path,"neko.txt.mecab"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ret)


if __name__ == "__main__":
    prep()