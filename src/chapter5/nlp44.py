import os
import sys
import re
import json
from typing import List
import pydotplus

from common import *

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter5")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter5")

def chunks2dot(chunks: List[Chunk]) -> str:
    digraph_list = []
    for chunk in chunks:
        if chunk.dst != -1:
            sent_f = chunk.morph_to_str(skip_fig=True)
            sent_t = chunks[chunk.dst].morph_to_str(skip_fig=True)
            digraph_list.append("\t{} -> {};\n".format(sent_f, sent_t))
    ret_str = " digraph graphname {{ node[fontname=\"MS UI Gothic\"]; \n{}}}".format("".join(digraph_list))
    return ret_str

def dot2graph(dot_str: str, output_file: str):
    graph = pydotplus.graph_from_dot_data(dot_str)
    graph.write_png(output_file)
    
def nlp_44():

    chunk_lists = parse_cabocha_result(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )
    chunks = chunk_lists[3]
    dot_str = chunks2dot(chunks)
    dot2graph(
        dot_str,
        os.path.join(result_dir_path, "graph.png")
    )

if __name__ == "__main__":
    nlp_44()