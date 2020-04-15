
def create_ngram(s: str, n: int, gram_type: str) -> list:
    if gram_type == "word":
        lst = s.split()
    elif gram_type == "character":
        lst = s
    else:
        raise ValueError('gram_type must be either "word" or "character"')
    
    ret_lst = []
    for i in range(len(lst)-(n-1)):
        ret_lst.append(lst[i:i+n])
    return ret_lst


def nlp_05():
    s = "I am an NLPer"
    print("word_bigram:")
    print(create_ngram(s, 2, "word"))
    print("character_bigram:")
    print(create_ngram(s, 2, "character"))

if __name__ == "__main__":
    nlp_05()