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
        # Fokus pada pembuatan pupuk kompos organik dengan metode Takakura
        for res in results["organic_results"][:3]:
            snippet = res.get("snippet", "")
            if "pupuk kompos organik" in snippet.lower() and "metode takakura" in snippet.lower():
                return snippet.split('.')[0] + '.'  # Ambil kalimat pertama yang relevan
        
        # Jika tidak ada hasil, beri penjelasan singkat tentang metode Takakura
        return ("Metode Takakura adalah teknik pembuatan pupuk kompos organik yang menggunakan bahan-bahan organik seperti sisa makanan, daun, dan kotoran hewan, "
                "dengan cara fermentasi dalam wadah tertutup untuk menghasilkan pupuk yang kaya mikroorganisme yang bermanfaat bagi tanah.")

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
