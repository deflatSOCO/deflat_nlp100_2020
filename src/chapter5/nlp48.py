import os
import sys
import re
import json
from typing import List
import pydotplus
from collections import defaultdict, OrderedDict

from common import *

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter5")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter5")

def nlp_48():

    chunk_lists = parse_cabocha_result(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )

    with open(
        os.path.join(result_dir_path,"result_48.txt"),
        "w",
        newline="\n",
        encoding="utf-8"
    )as f:
        for chunks in chunk_lists:
            for i,chunk in enumerate(chunks):
                if chunk.contains_noun() and chunk.dst != -1:
                    sent_list = []
                    chunk_next = chunk
                    while True:
                        sent_list.append(chunk_next.morph_to_str(skip_fig=True))
                        if chunk_next.dst == -1: break
                        chunk_next = chunks[chunk_next.dst]
                    f.write(" -> ".join(sent_list)+"\n")


if __name__ == "__main__":
    nlp_48()