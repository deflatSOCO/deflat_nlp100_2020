from nlp05 import create_ngram

def nlp_06():
    str1 = "paraparaparadise"
    str2 = "paragraph"
    X = set(create_ngram(str1, 2, "character"))
    Y = set(create_ngram(str2, 2, "character"))
    print("X&Y:")
    print(X&Y)
    print("X+Y:")
    print(X|Y)
    print("X-Y:")
    print(X-Y)
    print("Y-X:")
    print(Y-X)
    print("'se' in X:")
    print("se" in X)
    print("'se' in Y:")
    print("se" in Y)

if __name__ == "__main__":
    nlp_06()