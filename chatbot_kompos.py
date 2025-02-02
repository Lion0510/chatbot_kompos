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
        
        # Jika tidak ada hasil, beri penjelasan lengkap tentang cara pembuatan pupuk kompos menggunakan metode Takakura
        responses = [
            "Pembuatan pupuk kompos organik menggunakan metode Takakura dimulai dengan pengumpulan bahan organik seperti daun, sampah rumah tangga, dan kotoran hewan. Bahan tersebut kemudian dimasukkan ke dalam wadah tertutup dan dibiarkan untuk difermentasi selama beberapa minggu. Proses fermentasi ini akan menghasilkan pupuk yang kaya mikroorganisme yang bermanfaat untuk tanah.",
            "Untuk membuat pupuk kompos organik dengan metode Takakura, pertama-tama kumpulkan bahan-bahan organik seperti daun kering, sisa makanan, dan kotoran hewan. Bahan-bahan ini dicampur dalam wadah tertutup yang memungkinkan fermentasi berlangsung dengan baik. Setelah beberapa minggu, bahan tersebut akan terurai menjadi pupuk yang kaya akan mikroorganisme, siap digunakan untuk meningkatkan kesuburan tanah.",
            "Metode Takakura dalam pembuatan pupuk kompos organik dimulai dengan pengumpulan bahan organik seperti sampah rumah tangga, daun kering, dan sisa sayuran. Bahan-bahan ini kemudian disusun dalam lapisan-lapisan di dalam wadah tertutup yang menjaga kelembaban dan suhu yang stabil. Setelah beberapa minggu, bahan-bahan tersebut akan terurai dan berubah menjadi kompos yang berguna.",
            "Proses pembuatan pupuk kompos organik dengan metode Takakura melibatkan fermentasi bahan-bahan organik seperti daun, sampah dapur, dan kotoran hewan dalam wadah tertutup. Bahan-bahan tersebut dicampur secara merata dan dibiarkan selama beberapa minggu untuk mengalami proses penguraian alami. Pupuk yang dihasilkan sangat bermanfaat untuk kesuburan tanah dan meningkatkan kesehatan tanaman."
        ]
        
        # Pilih jawaban secara acak agar lebih bervariasi
        return random.choice(responses)

    except KeyError:
        return "Maaf, saya tidak bisa mencari saat ini."

# Styling header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Chatbot Pembuatan Pupuk Kompos Organik</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #2c3e50;'>Dengan Metode Takakura</h3>", unsafe_allow_html=True)

# Menambahkan gambar terkait dengan pupuk kompos organik
st.image("https://www.example.com/images/compost.jpg", caption="Pembuatan Pupuk Kompos Organik", use_column_width=True)

# Input pengguna
st.markdown("<h4 style='color: #34495e;'>Tanyakan sesuatu tentang pembuatan pupuk kompos organik dengan metode Takakura:</h4>", unsafe_allow_html=True)
user_input = st.text_input("")

# Memproses input pengguna
if user_input:
    st.write("🔄 Sedang memproses...")
    response = google_search(user_input)
    
    # Menampilkan jawaban
    st.markdown(f"<div style='background-color: #f0f0f0; padding: 15px; border-radius: 10px; font-size: 16px; color: #2c3e50;'><b>Jawaban:</b> {response}</div>", unsafe_allow_html=True)
