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
        # Ambil cuplikan pertama yang relevan dan pastikan jawabannya singkat
        for res in results["organic_results"][:3]:
            snippet = res.get("snippet", "")
            if "pupuk kompos" in snippet.lower():  # Memastikan relevansi
                return snippet.split('.')[0] + '.'  # Mengambil kalimat pertama
        
        return "Maaf, saya tidak dapat menemukan informasi yang relevan."

    except KeyError:
        return "Maaf, saya tidak bisa mencari saat ini."

# Header aplikasi
st.title("Chatbot Pupuk Kompos Organik")

# Input pengguna
user_input = st.text_input("Tanyakan sesuatu tentang pupuk kompos:")

if user_input:
    st.write("🔄 Sedang memproses...")
    response = google_search(user_input)
    
    # Menampilkan jawaban dalam satu kalimat
    st.markdown(f"**Jawaban:** {response}")
