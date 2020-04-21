import os
import sys
import re
import json


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __str__(self):
        return "Surface: {}, Base: {}, Pos: {}, Pos1: {}".format(
            self.surface, self.base, self.pos, self.pos1
        )

def get_word_morph(word_line: str):
    surface, info = word_line.split("\t")
    info_split = info.split(",")
    return Morph(
        surface=surface,
        base=info_split[6],
        pos=info_split[0],
        pos1=info_split[1]
    )

def parse_sentence_result(data_lines: str):
    ret = []
    for l in data_lines:
        if l == "EOS\n": break
        ret.append(get_word_morph(l))
    return ret

