# 15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com)
# och skriv ut hur många vokaler som finns i strängen. Tips: "a" in "abcd" är True!

def count_vowels(txt):
    vowels = "aouåeiyäö"
    count = 0
    for letter in txt:
        if letter in vowels:
            count += 1
    return count


if __name__ == '__main__':
    txt = input("Jag kan räkna vokaler! Ge mig nått att äta: ")
    print(f"Antal vokaler: {count_vowels(txt)}")