import os
import sys
import re
import json


from common import *

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter5")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter5")


def nlp_41():
    chunk_lists = parse_cabocha_result(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )
    for e in chunk_lists[7]:
        print(e)

if __name__ == "__main__":
    nlp_41()