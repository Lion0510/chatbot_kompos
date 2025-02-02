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
        return "\n".join([res["link"] for res in results["organic_results"][:3]])
    except KeyError:
        return "Maaf, saya tidak bisa mencari saat ini."

# Header aplikasi
st.title("Chatbot Pupuk Kompos Organik")

# Input pengguna
user_input = st.text_input("Tanyakan sesuatu tentang pupuk kompos:")

if user_input:
    st.write("🔍 Mencari di Google...")
    response = google_search(user_input)
    st.write(response)
