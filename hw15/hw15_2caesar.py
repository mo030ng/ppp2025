def print_code(ch):
    print(f"{ch} -> {ord(ch)}")

def print_char(code):
    print(f"{code} -> {chr(code)}")

def caesar_encode_ch(ch, shift):
    return chr(ord(ch) + shift)

def caesar_encode(text: str, shift: int = 3) -> str:
    full_text = []
    for ch in text:
        encoded_ch = caesar_encode_ch(ch, shift)
        full_text.append(encoded_ch)
    return "".join(full_text)
    
def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)


def main():
    print_code("a")
    print_char(99)
    
    print(caesar_encode("LoVe"))
    print(caesar_decode("OrYh"))


if __name__ == '__main__':
    main()