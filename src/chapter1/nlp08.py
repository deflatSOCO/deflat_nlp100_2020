
def cipher(s: str)-> str:
    convert_list = [
        chr(219-ord(c)) if (ord('a')<=ord(c)<=ord('z')) else c
    for c in s]
    return "".join(convert_list)

def nlp_08():
    base_str = "cipher test_string. Can YOU hear me???"
    print(f"original: {base_str}")
    encrypted = cipher(base_str)
    print(f"encrypted: {encrypted}")
    decrypted = cipher(encrypted)
    print(f"decrypted: {decrypted}")

if __name__ == "__main__":
    nlp_08()