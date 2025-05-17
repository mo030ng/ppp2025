def toggle_text(text: str) -> str:
    for ch in text: 
        if 'a' <= ch <= 'z':
            return chr(ord(ch)-32)
        elif 'A' <= ch <= 'Z':
            return chr(ord(ch)+32)
    return ch

def main():
    print(toggle_text("B"))

if __name__ == '__main__':
    main()