# 15.1 Implementera "wordcount" som jag och Christoffer byggde

def wordcount(text):
    # 1. Dela texten i mellanrum (med split)
    # 2. Beräkna längden på resultatlistan
    # 3. Profit
    return len(text.split())


if __name__ == '__main__':
    text = input("Skriv in en text:")
    print(f"I den texten hittade jag {wordcount(text)} ord. Byeeee!")
