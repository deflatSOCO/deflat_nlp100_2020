import re
import json

def nlp_00():
    s = "stressed"
    print(s[::-1])

def nlp_01():
    s = "パタトクカシーー"
    print(s[::2])

def nlp_02():
    a = "パトカー"
    b = "タクシー"
    print("".join(c + d for c,d in zip(a,b)))

def nlp_03():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    ss = re.sub(r"[^a-zA-Z ]","",s)
    print([len(e) for e in ss.split()])

def nlp_04():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    s_lst = s.split()
    single_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    ret_dict={}
    for i in range(len(s_lst)):
        ret_dict[i+1] = s_lst[i][:1+(i+1 not in single_char)]
    print(json.dumps(ret_dict))
    

if __name__ == "__main__":
    nlp_00()
    nlp_01()
    nlp_02()
    nlp_03()
    nlp_04()