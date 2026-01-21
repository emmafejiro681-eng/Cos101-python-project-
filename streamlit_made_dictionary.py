import streamlit as st

# 20-word translation dictionary
dictionary = {
    "hello": {
        "English": "Hello",
        "Igbo": "Ndewo",
        "Hausa": "Sannu",
        "Yoruba": "Pẹlẹ",
        "Spanish": "Hola"
    },
    "thank you": {
        "English": "Thank you",
        "Igbo": "Daalụ",
        "Hausa": "Na gode",
        "Yoruba": "E se",
        "Spanish": "Gracias"
    },
    "yes": {
        "English": "Yes",
        "Igbo": "Ee",
        "Hausa": "Eh",
        "Yoruba": "Bẹẹni",
        "Spanish": "Sí"
    },
    "no": {
        "English": "No",
        "Igbo": "Mba",
        "Hausa": "A'a",
        "Yoruba": "Rara",
        "Spanish": "No"
    },
    "water": {
        "English": "Water",
        "Igbo": "Mmiri",
        "Hausa": "Ruwa",
        "Yoruba": "Omi",
        "Spanish": "Agua"
    },
    "food": {
        "English": "Food",
        "Igbo": "Nri",
        "Hausa": "Abinci",
        "Yoruba": "Ounje",
        "Spanish": "Comida"
    },
    "house": {
        "English": "House",
        "Igbo": "Ụlọ",
        "Hausa": "Gida",
        "Yoruba": "Ile",
        "Spanish": "Casa"
    },
    "friend": {
        "English": "Friend",
        "Igbo": "Enyi",
        "Hausa": "Aboki",
        "Yoruba": "Ore",
        "Spanish": "Amigo"
    },
    "family": {
        "English": "Family",
        "Igbo": "Ezinụlọ",
        "Hausa": "Iyali",
        "Yoruba": "Idile",
        "Spanish": "Familia"
    },
    "love": {
        "English": "Love",
        "Igbo": "Ihunanya",
        "Hausa": "Soyayya",
        "Yoruba": "Ifẹ",
        "Spanish": "Amor"
    },
    "money": {
        "English": "Money",
        "Igbo": "Ego",
        "Hausa": "Kudi",
        "Yoruba": "Owo",
        "Spanish": "Dinero"
    },
    "work": {
        "English": "Work",
        "Igbo": "Ọrụ",
        "Hausa": "Aiki",
        "Yoruba": "Iṣẹ",
        "Spanish": "Trabajo"
    },
    "school": {
        "English": "School",
        "Igbo": "Ụlọ akwụkwọ",
        "Hausa": "Makaranta",
        "Yoruba": "Ile-iwe",
        "Spanish": "Escuela"
    },
    "book": {
        "English": "Book",
        "Igbo": "Akwụkwọ",
        "Hausa": "Littafi",
        "Yoruba": "Iwe",
        "Spanish": "Libro"
    },
    "sun": {
        "English": "Sun",
        "Igbo": "Anyānwụ",
        "Hausa": "Rana",
        "Yoruba": "Oorun",
        "Spanish": "Sol"
    },
    "moon": {
        "English": "Moon",
        "Igbo": "Ọnwa",
        "Hausa": "Wata",
        "Yoruba": "Osupa",
        "Spanish": "Luna"
    },
    "road": {
        "English": "Road",
        "Igbo": "Ụzọ",
        "Hausa": "Hanya",
        "Yoruba": "Ona",
        "Spanish": "Camino"
    },
    "market": {
        "English": "Market",
        "Igbo": "Ahịa",
        "Hausa": "Kasuwa",
        "Yoruba": "Oja",
        "Spanish": "Mercado"
    },
    "child": {
        "English": "Child",
        "Igbo": "Nwa",
        "Hausa": "Yaro",
        "Yoruba": "Ọmọ",
        "Spanish": "Niño"
    },
    "health": {
        "English": "Health",
        "Igbo": "Ahụike",
        "Hausa": "Lafiya",
        "Yoruba": "Ilera",
        "Spanish": "Salud"
    }
}

st.title("🌍 Simple Language Dictionary")

# Layout: left content, right controls
left, right = st.columns([3, 1])

with right:
    language = st.selectbox(
        "Select Language",
        ["English", "Igbo", "Hausa", "Yoruba", "Spanish"]
    )

with left:
    st.subheader(f"Translations in {language}")

    for word, translations in dictionary.items():
        st.write(f"**{word.capitalize()}** → {translations[language]}")
