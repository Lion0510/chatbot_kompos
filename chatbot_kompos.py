import streamlit as st
from serpapi import GoogleSearch

# Simpan API Key sebagai secret di Streamlit Cloud
SERPAPI_KEY = st.secrets["SERPAPI_KEY"]

# Fungsi pencarian Google menggunakan SerpAPI
def google_search(query):
    params = {
        "q": query,
        "hl": "id",  # Bahasa Indonesia
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    try:
        # Fokus pada pupuk kompos organik dan metode Takakura
        for res in results["organic_results"][:3]:
            snippet = res.get("snippet", "")
            if "pupuk kompos organik" in snippet.lower() and "takakura" in snippet.lower():
                return snippet.split('.')[0] + '.'  # Ambil kalimat pertama yang relevan
        
        return "Maaf, saya tidak dapat menemukan informasi yang relevan tentang pupuk kompos organik dan metode Takakura."

    except KeyError:
        return "Maaf, saya tidak bisa mencari saat ini."

# Header aplikasi
st.title("Chatbot Pupuk Kompos Organik dan Metode Takakura")

# Input pengguna
user_input = st.text_input("Tanyakan sesuatu tentang pupuk kompos organik atau metode Takakura:")

if user_input:
    st.write("🔄 Sedang memproses...")
    response = google_search(user_input)
    
    # Menampilkan jawaban dalam satu kalimat
    st.markdown(f"**Jawaban:** {response}")
