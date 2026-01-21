dictionary = {
    "hello": {
        "English": "hello",
        "Yoruba": "bawo",
        "Igbo": "ndewo",
        "Hausa": "sannu",
        "Spanish": "hola",
        "Italian": "ciao"
    },
    "goodbye": {
        "English": "goodbye",
        "Yoruba": "odabo",
        "Igbo": "ka omesia",
        "Hausa": "sai anjima",
        "Spanish": "adios",
        "Italian": "arrivederci"
    },
    "thank you": {
        "English": "thank you",
        "Yoruba": "e se",
        "Igbo": "daalu",
        "Hausa": "na gode",
        "Spanish": "gracias",
        "Italian": "grazie"
    },
    "water": {
        "English": "water",
        "Yoruba": "omi",
        "Igbo": "mmiri",
        "Hausa": "ruwa",
        "Spanish": "agua",
        "Italian": "acqua"
    },
    "food": {
        "English": "food",
        "Yoruba": "ounje",
        "Igbo": "nri",
        "Hausa": "abinci",
        "Spanish": "comida",
        "Italian": "cibo"
    },
    "house": {
        "English": "house",
        "Yoruba": "ile",
        "Igbo": "ulo",
        "Hausa": "gida",
        "Spanish": "casa",
        "Italian": "casa"
    },
    "friend": {
        "English": "friend",
        "Yoruba": "ore",
        "Igbo": "enyi",
        "Hausa": "aboki",
        "Spanish": "amigo",
        "Italian": "amico"
    },
    "family": {
        "English": "family",
        "Yoruba": "ebi",
        "Igbo": "ezinulo",
        "Hausa": "iyali",
        "Spanish": "familia",
        "Italian": "famiglia"
    },
    "love": {
        "English": "love",
        "Yoruba": "ife",
        "Igbo": "ihunanya",
        "Hausa": "so",
        "Spanish": "amor",
        "Italian": "amore"
    },
    "school": {
        "English": "school",
        "Yoruba": "ile-iwe",
        "Igbo": "ulo akwukwo",
        "Hausa": "makaranta",
        "Spanish": "escuela",
        "Italian": "scuola"
    },
    "book": {
        "English": "book",
        "Yoruba": "iwe",
        "Igbo": "akwukwo",
        "Hausa": "littafi",
        "Spanish": "libro",
        "Italian": "libro"
    },
    "day": {
        "English": "day",
        "Yoruba": "ojo",
        "Igbo": "ubochi",
        "Hausa": "rana",
        "Spanish": "dia",
        "Italian": "giorno"
    },
    "night": {
        "English": "night",
        "Yoruba": "oru",
        "Igbo": "abali",
        "Hausa": "dare",
        "Spanish": "noche",
        "Italian": "notte"
    },
    "happy": {
        "English": "happy",
        "Yoruba": "inu-dun",
        "Igbo": "obi uto",
        "Hausa": "murna",
        "Spanish": "feliz",
        "Italian": "felice"
    },
    "sad": {
        "English": "sad",
        "Yoruba": "ibanuje",
        "Igbo": "mwute",
        "Hausa": "bakin ciki",
        "Spanish": "triste",
        "Italian": "triste"
    },
    "man": {
        "English": "man",
        "Yoruba": "okunrin",
        "Igbo": "nwoke",
        "Hausa": "namiji",
        "Spanish": "hombre",
        "Italian": "uomo"
    },
    "woman": {
        "English": "woman",
        "Yoruba": "obinrin",
        "Igbo": "nwanyi",
        "Hausa": "mace",
        "Spanish": "mujer",
        "Italian": "donna"
    },
    "child": {
        "English": "child",
        "Yoruba": "omo",
        "Igbo": "nwa",
        "Hausa": "yaro",
        "Spanish": "niño",
        "Italian": "bambino"
    },
    "money": {
        "English": "money",
        "Yoruba": "owo",
        "Igbo": "ego",
        "Hausa": "kudi",
        "Spanish": "dinero",
        "Italian": "denaro"
    },
    "work": {
        "English": "work",
        "Yoruba": "ise",
        "Igbo": "oru",
        "Hausa": "aiki",
        "Spanish": "trabajo",
        "Italian": "lavoro"
    }
}

# ---------- STREAMLIT UI ----------

st.set_page_config(page_title="Multilingual Dictionary", layout="wide")

st.title("📘 Multilingual Dictionary")

# Sidebar
st.sidebar.header("Settings")

language = st.sidebar.selectbox(
    "Select Language",
    ["English", "Yoruba", "Igbo", "Hausa", "Spanish", "Italian"]
)

st.sidebar.subheader("Available Words")
st.sidebar.write(list(dictionary.keys()))

# Main search bar
search_word = st.text_input("🔍 Search for a word (English)")

if search_word:
    search_word = search_word.lower()

    if search_word in dictionary:
        st.success(f"Translation in {language}:")
        st.markdown(f"### **{dictionary[search_word][language]}**")
    else:
        st.error("Word not found. Please check the spelling.")
