import os
import sys
import math
import re
import json
import itertools
from collections import Counter
import requests

THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(THISFILEDIR, "..", "..", "data","chapter3")
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter3")

def nlp_29():
    with open(os.path.join(result_dir_path,"england.txt"), "r", encoding="utf-8") as f:
        data = f.read()
    info = re.search(r"\{\{基礎情報 国(\n.+?\n\})\}", data, re.DOTALL).groups()[0]
    info_lines = re.findall("(?=\n\|(.+?)\s*=\s*(.+?)\n[\|\}])", info, flags=re.DOTALL)
    info_dict = {}
    for k,v in info_lines:
        vv = re.sub(r"'{2,5}(.+?)'{2,5}", r"\1", v)
        vv = re.sub(r"<ref.+?</ref>","",vv, flags=re.DOTALL)
        vv = re.sub(r"<ref name.+?>","",vv)
        vv = re.sub(r"\[\[(?!ファイル:)([^\[\]]+\|)?(.+?)[\}]*?\]\]", r"\2",vv)
        vv = re.sub(r"\{\{(\d+)\}\}",r"\1", vv)
        vv = re.sub(r"\{\{(.+\|)?(.+?)\}\}", r"\2",vv)
        vv = vv.replace("<br />","\n")
        info_dict[k]=vv
    url = "https://www.mediawiki.org/w/api.php"
    file_url = info_dict["国旗画像"]
    params = {
        "action":"query",
        "prop":"imageinfo",
        "format":"json",
        "iiprop":"url",
        "titles":"File:"+file_url
    }
    res = requests.get(url, params=params)
    print(res.json()["query"]["pages"]["-1"]["imageinfo"][0]["url"])

if __name__ == "__main__":
    nlp_29()