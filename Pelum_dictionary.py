dictionary = {
    "hello": {
        "english": "hello",
        "yoruba": "bawo",
        "igbo": "ndewo",
        "hausa": "sannu",
        "spanish": "hola",
        "italian": "ciao"
    },
    "goodbye": {
        "english": "goodbye",
        "yoruba": "odabo",
        "igbo": "ka omesia",
        "hausa": "sai anjima",
        "spanish": "adios",
        "italian": "arrivederci"
    },
    "thank you": {
        "english": "thank you",
        "yoruba": "e se",
        "igbo": "daalu",
        "hausa": "na gode",
        "spanish": "gracias",
        "italian": "grazie"
    },
    "water": {
        "english": "water",
        "yoruba": "omi",
        "igbo": "mmiri",
        "hausa": "ruwa",
        "spanish": "agua",
        "italian": "acqua"
    },
    "food": {
        "english": "food",
        "yoruba": "ounje",
        "igbo": "nri",
        "hausa": "abinci",
        "spanish": "comida",
        "italian": "cibo"
    },
    "house": {
        "english": "house",
        "yoruba": "ile",
        "igbo": "ulo",
        "hausa": "gida",
        "spanish": "casa",
        "italian": "casa"
    },
    "friend": {
        "english": "friend",
        "yoruba": "ore",
        "igbo": "enyi",
        "hausa": "aboki",
        "spanish": "amigo",
        "italian": "amico"
    },
    "family": {
        "english": "family",
        "yoruba": "ebi",
        "igbo": "ezinulo",
        "hausa": "iyali",
        "spanish": "familia",
        "italian": "famiglia"
    },
    "love": {
        "english": "love",
        "yoruba": "ife",
        "igbo": "ihunanya",
        "hausa": "so",
        "spanish": "amor",
        "italian": "amore"
    },
    "school": {
        "english": "school",
        "yoruba": "ile-iwe",
        "igbo": "ulo akwukwo",
        "hausa": "makaranta",
        "spanish": "escuela",
        "italian": "scuola"
    },
    "book": {
        "english": "book",
        "yoruba": "iwe",
        "igbo": "akwukwo",
        "hausa": "littafi",
        "spanish": "libro",
        "italian": "libro"
    },
    "day": {
        "english": "day",
        "yoruba": "ojo",
        "igbo": "ubochi",
        "hausa": "rana",
        "spanish": "dia",
        "italian": "giorno"
    },
    "night": {
        "english": "night",
        "yoruba": "oru",
        "igbo": "abali",
        "hausa": "dare",
        "spanish": "noche",
        "italian": "notte"
    },
    "happy": {
        "english": "happy",
        "yoruba": "inu-dun",
        "igbo": "obi uto",
        "hausa": "murna",
        "spanish": "feliz",
        "italian": "felice"
    },
    "sad": {
        "english": "sad",
        "yoruba": "ibanuje",
        "igbo": "mwute",
        "hausa": "bakin ciki",
        "spanish": "triste",
        "italian": "triste"
    },
    "man": {
        "english": "man",
        "yoruba": "okunrin",
        "igbo": "nwoke",
        "hausa": "namiji",
        "spanish": "hombre",
        "italian": "uomo"
    },
    "woman": {
        "english": "woman",
        "yoruba": "obinrin",
        "igbo": "nwanyi",
        "hausa": "mace",
        "spanish": "mujer",
        "italian": "donna"
    },
    "child": {
        "english": "child",
        "yoruba": "omo",
        "igbo": "nwa",
        "hausa": "yaro",
        "spanish": "niño",
        "italian": "bambino"
    },
    "money": {
        "english": "money",
        "yoruba": "owo",
        "igbo": "ego",
        "hausa": "kudi",
        "spanish": "dinero",
        "italian": "denaro"
    },
    "work": {
        "english": "work",
        "yoruba": "ise",
        "igbo": "oru",
        "hausa": "aiki",
        "spanish": "trabajo",
        "italian": "lavoro"
    }
}

print("Multilingual Dictionary")
print("Languages: English, Yoruba, Igbo, Hausa, Spanish, Italian")
print("Type 'exit' to quit\n")

while True:
    word = input("Enter an English word: ").lower()

    if word == "exit":
        print("Goodbye!")
        break

    if word in dictionary:
        for lang, translation in dictionary[word].items():
            print(f"{lang.capitalize()}: {translation}")
        print()
    else:
        print("Word not found.\n")
