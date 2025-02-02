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
        
        # Jika tidak ada hasil, beri penjelasan lengkap dan terstruktur
        responses = [
            "Pupuk kompos organik adalah pupuk yang terbuat dari bahan organik yang telah melalui proses dekomposisi alami. Contohnya adalah daun, sisa makanan, dan kotoran hewan. Metode Takakura adalah salah satu metode pembuatan pupuk kompos dengan cara fermentasi dalam wadah tertutup. Proses ini mempercepat penguraian bahan organik menjadi kompos yang kaya akan mikroorganisme yang bermanfaat.",
            "Pupuk kompos organik berasal dari bahan-bahan organik yang telah difermentasi menjadi pupuk yang berguna bagi tanah. Metode Takakura adalah cara pembuatan pupuk kompos dengan memanfaatkan bahan organik seperti sampah rumah tangga dan kotoran hewan yang difermentasi dalam wadah tertutup. Kelebihan metode ini adalah pengolahan sampah rumah tangga menjadi pupuk yang berguna, namun membutuhkan perhatian pada kelembaban dan aerasi.",
            "Pupuk kompos organik terdiri dari bahan-bahan alami yang telah terdekomposisi menjadi pupuk yang bermanfaat untuk kesuburan tanah, seperti sisa sayuran, daun, dan kotoran hewan. Metode Takakura adalah teknik fermentasi bahan organik dalam wadah tertutup yang memungkinkan penguraian lebih cepat. Keuntungan dari metode ini adalah mengurangi limbah dan meningkatkan kualitas tanah, tetapi kelemahannya adalah memerlukan pengelolaan yang hati-hati agar proses fermentasi berjalan optimal.",
            "Pupuk kompos organik adalah pupuk yang dihasilkan dari bahan organik seperti sampah rumah tangga yang difermentasi. Metode Takakura adalah teknik pembuatan pupuk kompos organik yang mengandalkan fermentasi dalam wadah tertutup dengan bahan organik seperti daun dan kotoran hewan. Kelebihan metode ini adalah efisiensi penggunaan limbah rumah tangga, namun kelemahannya adalah memerlukan waktu dan perhatian terhadap kondisi lingkungan dalam wadah fermentasi."
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

