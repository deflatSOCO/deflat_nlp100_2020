import os
import sys
import re
import json
from typing import List
from itertools import combinations

from common import *

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter5")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter5")

def get_dst(ind:int, chunks:List[Chunk]) -> List[int]:
    ret_list = []
    while True:
        ret_list.append(ind)
        if chunks[ind].dst == -1: break
        ind = chunks[ind].dst
    return ret_list

def get_path_str(ind_A: int, ind_B: int, chunks:List[Chunk]) -> str:
    listA = get_dst(ind_A, chunks)
    listB = get_dst(ind_B, chunks)
    if ind_B in listA:
        sent_list = []
        for ind in listA:
            if ind == ind_A:
                sent_list.append(
                    chunks[ind].morph_to_masked_str("X", skip_fig=True)
                )
            elif ind == ind_B:
                sent_list.append(
                    "Y"
                )
                break
            else:
                sent_list.append(
                    chunks[ind].morph_to_str(skip_fig=True)
                )
        return " -> ".join(sent_list)
    else:
        common_dst = min(set(listA)&set(listB))
        sent_listA=[]
        sent_listB=[]
        for ind in listA:
            if ind == ind_A:
                sent_listA.append(
                    chunks[ind].morph_to_masked_str("X", skip_fig=True)
                )
            elif ind == common_dst:
                break
            else:
                sent_listA.append(
                    chunks[ind].morph_to_str(skip_fig=True)
                )
        for ind in listB:
            if ind == ind_B:
                sent_listB.append(
                    chunks[ind].morph_to_masked_str("Y", skip_fig=True)
                )
            elif ind == common_dst:
                break
            else:
                sent_listB.append(
                    chunks[ind].morph_to_str(skip_fig=True)
                )
        sent_strA = " -> ".join(sent_listA)
        sent_strB = " -> ".join(sent_listB)
        return "{} | {} | {}".format(
            sent_strA,
            sent_strB,
            chunks[common_dst].morph_to_str(skip_fig=True)
        )
def nlp_49():

    chunk_lists = parse_cabocha_result(
        os.path.join(data_dir_path,"neko.txt.cabocha")
    )

    with open(
        os.path.join(result_dir_path,"result_49.txt"),
        "w",
        newline="\n",
        encoding="utf-8"
    )as f:
        for chunks in chunk_lists:
            noun_part_list = []
            for i,chunk in enumerate(chunks):
                if chunk.contains_noun() and chunk.dst != -1:
                    noun_part_list.append(i)
            noun_part_list.sort()
            for a,b in list(combinations(noun_part_list,2)):
                f.write(get_path_str(a, b, chunks) + "\n")


if __name__ == "__main__":
    nlp_49()