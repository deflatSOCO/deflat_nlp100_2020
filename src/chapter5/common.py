import os
import sys
import re
import json
from typing import List
from tqdm import tqdm

class Morph():
    def __init__(self, surface:str, base:str, pos:str, pos1:str):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __str__(self):
        return "Surface: {}, Base: {}, Pos: {}, Pos1: {}".format(
            self.surface, self.base, self.pos, self.pos1
        )

class Chunk():
    def __init__(self, word_lines: List[str], dst: int):
        self.morphs = parse_sentence_result(word_lines)
        self.dst = dst
        self.srcs = []
    
    def add_src(self, src: int):
        self.srcs.append(src)

    def morph_to_str(self, skip_fig: bool=False) -> str:
        if skip_fig:
            surface_list = [
                e.surface for e in self.morphs if e.pos != "記号"
            ]
        else:
            surface_list = [
                e.surface for e in self.morphs
            ]
        return "".join(surface_list)

    def _get_pos_list(self) -> List[str]:
        return [e.pos for e in self.morphs]

    def _contains_pos(self, pos:str) ->bool:
        return pos in self._get_pos_list()

    def contains_noun(self) -> bool:
        return self._contains_pos("名詞")

    def contains_verb(self) -> bool:
        return self._contains_pos("動詞")

    def contains_pp(self) -> bool:
        return self.get_pp() is not None

    def contains_sahen_wo(self) -> bool:
        flag = (len(self.morphs) == 2) and \
            self.morphs[0].pos == "名詞" and \
            self.morphs[0].pos1 == "サ変接続" and \
            self.morphs[1].pos == "助詞" and \
            self.morphs[1].surface == "を"
        return flag


    def get_leftmost_verb(self) -> str:
        for m in self.morphs:
            if m.pos == "動詞":
                return m.base
        return None
    
    def get_pp(self) -> str:
        ret = None
        for m in self.morphs[::-1]:
            if m.pos == "助詞":
                ret = m.surface
                break
            elif m.pos == "記号":
                continue
            else:
                break
        return ret      

    def __str__(self):
        return "Sentence: {}, dst: {}, srcs: {}".format(
            self.morph_to_str(), self.dst, self.srcs
        )    
    

def get_word_morph(word_line: str) -> Morph:
    surface, info = word_line.split("\t")
    info_split = info.split(",")
    return Morph(
        surface=surface,
        base=info_split[6],
        pos=info_split[0],
        pos1=info_split[1]
    )

def parse_sentence_result(data_lines: List[str]) ->List[Morph]:
    ret = []
    for l in data_lines:
        if l == "EOS\n": break
        ret.append(get_word_morph(l))
    return ret


def get_sentence_chunk(data_lines: List[str]) ->List[Chunk]:
    header_pat = re.compile(r"^\* \d+ (.+?)D \d+/\d+ .+\n")
    ret = []
    cache = []
    
    dst_no = None
    for l in data_lines:
        header_check = re.search(header_pat, l)
        if header_check is None:
            cache.append(l)
        else:
            if dst_no is not None:
                ret.append(Chunk(cache, dst_no))
            cache = []
            dst_no = int(header_check.groups()[0])
    if dst_no is not None:
        ret.append(Chunk(cache, dst_no))

    for i,chunk in enumerate(ret):
        target = chunk.dst
        if target != -1:
            ret[target].add_src(i)

    return ret


def parse_cabocha_result(file_name: str) -> List[List[Chunk]]:
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
    ret = []
    cache = []
    for l in tqdm(data):
        if l == "EOS\n":
            if cache:
                ret.append(get_sentence_chunk(cache))
            cache = []
        else:
            cache.append(l)
    return ret