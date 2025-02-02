import streamlit as st
from serpapi import GoogleSearch
import random

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
        # Fokus pada pembuatan pupuk kompos organik dengan metode Takakura
        for res in results["organic_results"][:3]:
            snippet = res.get("snippet", "")
            if "pupuk kompos organik" in snippet.lower() and "metode takakura" in snippet.lower():
                return snippet.split('.')[0] + '.'  # Ambil kalimat pertama yang relevan
        
        # Jika tidak ada hasil, beri penjelasan singkat yang beragam
        responses = [
            "Metode Takakura adalah teknik pembuatan pupuk kompos organik yang melibatkan fermentasi bahan-bahan organik seperti sisa makanan dan daun dalam wadah tertutup.",
            "Pada metode Takakura, proses fermentasi dilakukan dalam wadah tertutup untuk mengubah bahan-bahan organik seperti daun dan kotoran hewan menjadi pupuk yang kaya mikroorganisme.",
            "Pembuatan pupuk kompos dengan metode Takakura menggunakan bahan organik seperti sisa makanan, kotoran hewan, dan daun, yang difermentasi dalam wadah tertutup untuk menghasilkan pupuk berkualitas.",
            "Metode Takakura mengandalkan fermentasi bahan organik seperti sisa sayuran dan limbah rumah tangga dalam wadah tertutup untuk menciptakan pupuk kompos yang bermanfaat untuk pertanian."
        ]
        
        # Pilih jawaban secara acak agar lebih bervariasi
        return random.choice(responses)

    except KeyError:
        return "Maaf, saya tidak bisa mencari saat ini."

# Header aplikasi
st.title("Chatbot Pembuatan Pupuk Kompos Organik dengan Metode Takakura")

# Input pengguna
user_input = st.text_input("Tanyakan sesuatu tentang pembuatan pupuk kompos organik dengan metode Takakura:")

if user_input:
    st.write("🔄 Sedang memproses...")
    response = google_search(user_input)
    
    # Menampilkan jawaban dalam satu kalimat atau penjelasan singkat
    st.markdown(f"**Jawaban:** {response}")
