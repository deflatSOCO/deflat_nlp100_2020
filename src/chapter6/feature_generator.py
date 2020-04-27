import os
import sys
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from typing import List, Tuple

class FeatureGenerator():

    def __init__(self):
        pass

    def fit(self, word_series: pd.Series):
        raise NotImplementedError

    def transform(self, word_series: pd.Series) -> Tuple[np.array, List[str]]:
        raise NotImplementedError
        

class WordCount(FeatureGenerator):
    
    def __init__(self):
        self.vectorizer = CountVectorizer(analyzer=lambda x:x)

    def fit(self, word_series: pd.Series):
        words = word_series.tolist()
        self.vectorizer.fit(words)

    def transform(self, word_series: pd.Series) -> Tuple[np.array, List[int]]:        
        words = word_series.tolist()
        vec = self.vectorizer.transform(words).toarray()
        fname = self.vectorizer.get_feature_names()
        return (vec, fname)

class TfIdf(FeatureGenerator):
    
    def __init__(self, min_df=0.0, max_df=1.0):
        self.vectorizer = TfidfVectorizer(
            analyzer=lambda x: x,
            min_df=min_df,
            max_df=max_df
        )

    def fit(self, word_series: pd.Series):
        words = word_series.tolist()
        self.vectorizer.fit(words)

    def transform(self, word_series: pd.Series) -> Tuple[np.array, List[int]]:        
        words = word_series.tolist()
        vec = self.vectorizer.transform(words).toarray()
        fname = self.vectorizer.get_feature_names()
        return (vec, fname)
