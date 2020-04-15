import random

def typoglycemia(s: str):
    if len(s)<=4:
        return s
    else:
        substr = list(s[1:-1])
        random.shuffle(substr)
        return s[0]+"".join(substr)+s[-1]

def nlp_09():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    s_lst = s.split()
    converted_lst = [
        typoglycemia(e) for e in s_lst
    ]
    print(" ".join(converted_lst))

if __name__ == "__main__":
    nlp_09()