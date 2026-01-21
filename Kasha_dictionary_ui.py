#translations = {
    "hello": {"English": "Hello", "Igbo": "Ndewo", "Yoruba": "Bawo", "Hausa": "Sannu", "Spanish": "Hola", "Italian": "Ciao"},
    "thank you": {"English": "Thank you", "Igbo": "Daalụ", "Yoruba": "E se", "Hausa": "Na gode", "Spanish": "Gracias", "Italian": "Grazie"},
    "yes": {"English": "Yes", "Igbo": "Ee", "Yoruba": "Beni", "Hausa": "Eh", "Spanish": "Sí", "Italian": "Sì"},
    "no": {"English": "No", "Igbo": "Mba", "Yoruba": "Rara", "Hausa": "A'a", "Spanish": "No", "Italian": "No"},
    "water": {"English": "Water", "Igbo": "Mmiri", "Yoruba": "Omi", "Hausa": "Ruwa", "Spanish": "Agua", "Italian": "Acqua"},
    "food": {"English": "Food", "Igbo": "Nri", "Yoruba": "Ounje", "Hausa": "Abinci", "Spanish": "Comida", "Italian": "Cibo"},
    "house": {"English": "House", "Igbo": "Ụlọ", "Yoruba": "Ile", "Hausa": "Gida", "Spanish": "Casa", "Italian": "Casa"},
    "school": {"English": "School", "Igbo": "Ụlọ akwụkwọ", "Yoruba": "Ile-iwe", "Hausa": "Makaranta", "Spanish": "Escuela", "Italian": "Scuola"},
    "friend": {"English": "Friend", "Igbo": "Enyi", "Yoruba": "Ore", "Hausa": "Aboki", "Spanish": "Amigo", "Italian": "Amico"},
    "mother": {"English": "Mother", "Igbo": "Nne", "Yoruba": "Iya", "Hausa": "Uwa", "Spanish": "Madre", "Italian": "Madre"},
    "father": {"English": "Father", "Igbo": "Nna", "Yoruba": "Baba", "Hausa": "Uba", "Spanish": "Padre", "Italian": "Padre"},
    "child": {"English": "Child", "Igbo": "Nwa", "Yoruba": "Omo", "Hausa": "Yaro", "Spanish": "Niño", "Italian": "Bambino"},
    "love": {"English": "Love", "Igbo": "Ịhụnanya", "Yoruba": "Ifẹ", "Hausa": "Soyayya", "Spanish": "Amor", "Italian": "Amore"},
    "money": {"English": "Money", "Igbo": "Ego", "Yoruba": "Owo", "Hausa": "Kudi", "Spanish": "Dinero", "Italian": "Denaro"},
    "work": {"English": "Work", "Igbo": "Ọrụ", "Yoruba": "Iṣẹ", "Hausa": "Aiki", "Spanish": "Trabajo", "Italian": "Lavoro"},
    "market": {"English": "Market", "Igbo": "Ahịa", "Yoruba": "Oja", "Hausa": "Kasuwa", "Spanish": "Mercado", "Italian": "Mercato"},
    "road": {"English": "Road", "Igbo": "Ụzọ", "Yoruba": "Ona", "Hausa": "Hanya", "Spanish": "Camino", "Italian": "Strada"},
    "day": {"English": "Day", "Igbo": "Ụbọchị", "Yoruba": "Ọjọ", "Hausa": "Rana", "Spanish": "Día", "Italian": "Giorno"},
    "night": {"English": "Night", "Igbo": "Abalị", "Yoruba": "Ale", "Hausa": "Dare", "Spanish": "Noche", "Italian": "Notte"},
    "god": {"English": "God", "Igbo": "Chukwu", "Yoruba": "Olorun", "Hausa": "Allah", "Spanish": "Dios", "Italian": "Dio"}
}

# Sidebar
st.sidebar.title("Translator Settings")
language = st.sidebar.selectbox("Select a language", ["English", "Igbo", "Yoruba", "Hausa", "Spanish", "Italian"])
st.sidebar.write("Available words:")
for word in translations.keys():
    st.sidebar.write(f"- {word}")

# Main area
st.title("Multi-language Translator")
search_word = st.text_input("Enter a word to translate:")

if search_word:
    search_word_lower = search_word.lower()
    if search_word_lower in translations:
        st.write(f"**{language} translation:** {translations[search_word_lower][language]}")
    else:
        st.write("Word not found in dictionary.")
