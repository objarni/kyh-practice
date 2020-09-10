# 15.1 Implementera "wordcount" som jag och Christoffer byggde

def wordcount(text):
    return len(text.split())


if __name__ == '__main__':
    text = input("Skriv in en text:")
    print(f"I den texten hittade jag {wordcount(text)} ord. Byeeee!")
