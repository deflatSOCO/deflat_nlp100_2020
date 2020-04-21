import os
import sys
import re
import json


from common import *

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter5")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter5")


def nlp_42():
    chunk_lists = parse_cabocha_result(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )
    for chunks in chunk_lists:
        for chunk in chunks:
            if chunk.dst != -1:
                sent_f = chunk.morph_to_str(skip_fig=True)
                sent_t = chunks[chunk.dst].morph_to_str(skip_fig=True)
                print("{}\t{}".format(sent_f, sent_t))

if __name__ == "__main__":
    nlp_42()