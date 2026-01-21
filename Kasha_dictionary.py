translation = {
    "hello": {1: "Hello", 2: "Ndewo", 3: "Sannu", 4: "Bawo", 5: "Ojo"},
    "thank you": {1: "Thank you", 2: "Daalụ", 3: "Na gode", 4: "E se", 5: "Oche"},
    "yes": {1: "Yes", 2: "Ee", 3: "Eh", 4: "Beni", 5: "Ee"},
    "no": {1: "No", 2: "Mba", 3: "A'a", 4: "Rara", 5: "Mba"},
    "water": {1: "Water", 2: "Mmiri", 3: "Ruwa", 4: "Omi", 5: "Ami"},
    "food": {1: "Food", 2: "Nri", 3: "Abinci", 4: "Ounje", 5: "Unjẹ"},
    "house": {1: "House", 2: "Ụlọ", 3: "Gida", 4: "Ile", 5: "Ule"},
    "school": {1: "School", 2: "Ụlọ akwụkwọ", 3: "Makaranta", 4: "Ile-iwe", 5: "Ile-eko"},
    "friend": {1: "Friend", 2: "Enyi", 3: "Aboki", 4: "Ore", 5: "Onẹ"},
    "mother": {1: "Mother", 2: "Nne", 3: "Uwa", 4: "Iya", 5: "Iya"},
    "father": {1: "Father", 2: "Nna", 3: "Uba", 4: "Baba", 5: "Baba"},
    "child": {1: "Child", 2: "Nwa", 3: "Yaro", 4: "Omo", 5: "Omo"},
    "love": {1: "Love", 2: "Ịhụnanya", 3: "Soyayya", 4: "Ifẹ", 5: "Ifẹ"},
    "money": {1: "Money", 2: "Ego", 3: "Kudi", 4: "Owo", 5: "Owo"},
    "work": {1: "Work", 2: "Ọrụ", 3: "Aiki", 4: "Iṣẹ", 5: "Iṣẹ"},
    "market": {1: "Market", 2: "Ahịa", 3: "Kasuwa", 4: "Oja", 5: "Oja"},
    "road": {1: "Road", 2: "Ụzọ", 3: "Hanya", 4: "Ona", 5: "Ona"},
    "night": {1: "Night", 2: "Abalị", 3: "Dare", 4: "Ale", 5: "Ale"},
    "day": {1: "Day", 2: "Ụbọchị", 3: "Rana", 4: "Ọjọ", 5: "Ọjọ"},
    "God": {1: "God", 2: "Chukwu", 3: "Allah", 4: "Olorun", 5: "Ojochamachala"}
}

languages = {
    1: "English",
    2: "Igbo",
    3: "Hausa",
    4: "Yoruba",
    5: "Igala"
}

while True:
    print("\nLanguage Menu")
    print("1. English")
    print("2. Igbo")
    print("3. Hausa")
    print("4. Yoruba")
    print("5. Igala")
    print("6. Exit")

    choice = int(input("Select option (1-6): "))

    if choice == 6:
        print("Program exited successfully.")
        break

    if choice < 1 or choice > 5:
        print("Invalid choice. Try again.")
        continue

    word = input("Enter a word (e.g. hello, water, food): ").lower()

    if word in translations:
        print(f"{languages[choice]} translation: {translations[word][choice]}")
    else:
        print("Word not found in dictionary.")
