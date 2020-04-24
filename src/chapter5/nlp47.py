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

    
def nlp_47():

    chunk_lists = parse_cabocha_result(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )

    with open(
        os.path.join(result_dir_path,"result_47.txt"),
        "w",
        newline="\n",
        encoding="utf-8"
    )as f:
        for chunks in chunk_lists:
            pp_list = defaultdict(list)
            verb_dict = OrderedDict()
            for i,chunk in enumerate(chunks):
                if chunk.contains_sahen_wo():
                    chunk_verb = chunks[chunk.dst]
                    if chunk_verb.contains_verb():
                        left = chunk.morph_to_str(skip_fig=True)
                        right = chunk_verb.get_leftmost_verb()
                        verb_dict[chunk.dst] = left + right
                elif chunk.contains_pp():
                    pp_list[chunk.dst].append([chunk.get_pp(), chunk.morph_to_str(skip_fig=True)])
            for k in verb_dict.keys():
                if pp_list[k]:
                    sorted_list = sorted(pp_list[k], key=lambda x: x[0])
                    pps = " ".join([x[0] for x in sorted_list])
                    strs = " ".join([x[1] for x in sorted_list])
                    f.write("{}\t{}\t{}\n".format(verb_dict[k], pps, strs))


if __name__ == "__main__":
    nlp_47()