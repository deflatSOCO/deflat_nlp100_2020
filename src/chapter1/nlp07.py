
def str_template(x:int, y:str,z:float):
    return f"{x}時の{y}は{z}"

def nlp_07():
    print(str_template(12, "気温", 22.4))

if __name__ == "__main__":
    nlp_07()