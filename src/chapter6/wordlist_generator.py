import os
import sys
import re
import pandas as pd
import numpy as np
from tqdm import tqdm
import nltk
from nltk import tokenize, stem
from nltk.corpus import wordnet
from typing import List, Tuple

class WordListGenerator():

    def __init__(self, lemma: bool=False, keep_pos: List[str]=None, drop_stopword:bool=False):
        self.do_lemmatize = lemma
        self.keep_pos = keep_pos
        self.lemmatizer = stem.WordNetLemmatizer()
        self.drop_stopword = drop_stopword
        self._setup_nltk()

    def _setup_nltk(self):
        # tokenize
        try:
            a = tokenize.word_tokenize("tokenizer setup")
        except LookupError:
            nltk.download("punkt")
            a = tokenize.word_tokenize("tokenizer setup")
        # pos_tag
        try:
            b = nltk.pos_tag(a)
        except LookupError:
            nltk.download('averaged_perceptron_tagger')
            b = nltk.pos_tag(a)
        # lemmatizer
        try:
            a = self.lemmatizer.lemmatize("tokenizer")
        except LookupError:
            nltk.download("wordnet")
            a = self.lemmatizer.lemmatize("tokenizer")
        # stopword
        try:
            self.stopword = nltk.corpus.stopwords.words('english')
        except LookupError:
            nltk.download("stopword")
            self.stopword = nltk.corpus.stopwords.words('english')
            

    def _tokenize(self, word: str) -> List[str]:
        return tokenize.word_tokenize(word)

    def _get_wordnet_pos(self, pos_tag:str) -> str:
        tag = pos_tag[0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)

    def _pick_tag(self, pos_list: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        ret = []
        for p in pos_list:
            if p[1][0].upper() in self.keep_pos:
                ret.append(p)
        return ret

    def _get_pos(self, word_list: List[str]) -> List[Tuple[str, str]]:
        tags = nltk.pos_tag(word_list)
        if self.keep_pos is not None:
            tags = self._pick_tag(tags)
        return tags

    def _lemmatize(self, pos_list: List[Tuple[str, str]]) -> List[str]:
        ret = []
        for w in pos_list:
            ret.append(
                self.lemmatizer.lemmatize(w[0], self._get_wordnet_pos(w[1]))
            )
        return ret

    def _drop_stopword(self, word_list: List[str]) ->List[str]:
        return [w for w in word_list if w not in self.stopword]

    def _proc(self, sent:str) -> List[str]:
        sent = sent.lower()
        token = self._tokenize(sent)
        pos = self._get_pos(token)
        if self.do_lemmatize:
            ret = self._lemmatize(pos)
        else:
            ret = [e[0] for e in pos]

        if self.drop_stopword:
            ret = self._drop_stopword(ret)
        return ret

    def tokenize_series(self, word_series: pd.Series) -> pd.Series:
        ret = word_series.apply(self._proc)
        return ret
        

    def tokenize_df(self, word_df: pd.DataFrame) -> pd.DataFrame:
        ret = word_df.copy()
        for k in ret.keys():
            ret[k] = self.tokenize_series(word_df[k])
        return ret
