# English-Hausa Translator - 20 Essential Words
# Group Assignment

hausa_dict = {
    "hello": "Sannu",
    "thank you": "Na gode",
    "please": "Don Allah",
    "yes": "Ee",
    "no": "A'a",
    "water": "Ruwa",
    "food": "Abinci",
    "house": "Gida",
    "money": "Kuɗi",
    "man": "Namiji",
    "woman": "Mace",
    "child": "Yaro",
    "mother": "Uwa",
    "father": "Uba",
    "friend": "Aboki",
    "school": "Makaranta",
    "work": "Aiki",
    "market": "Kasuwa",
    "good": "Da kyau",
    "bad": "Mugu"
}


def translate(word):
    word = word.lower().strip()
    return hausa_dict.get(word, "Word not found")


# Simple interface
print("ENGLISH-HAUSA TRANSLATOR (20 Words)")
print("=" * 35)

while True:
    print("\nEnter English word (or 'quit' to exit):")
    english_word = input("> ").strip()

    if english_word.lower() == 'quit':
        print("Barka da zuwa! (Goodbye!)")
        break

    hausa_word = translate(english_word)
    print(f"Hausa: {hausa_word}")
