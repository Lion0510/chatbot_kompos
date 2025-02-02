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
        # Mengambil cuplikan teks yang lebih relevan dari hasil pencarian
        # Fokus pada jenis-jenis pupuk kompos yang disebutkan dalam cuplikan
        relevant_snippets = []

        for res in results["organic_results"][:3]:
            snippet = res.get("snippet", "")
            if "pupuk kompos" in snippet.lower():
                relevant_snippets.append(snippet)

        # Jika tidak ada cuplikan relevan, memberikan pesan alternatif
        if not relevant_snippets:
            return "Maaf, saya tidak dapat menemukan informasi yang relevan."

        # Merangkum hasil dan memastikan jawabannya lebih jelas dan terstruktur
        summary = "\n\n".join(relevant_snippets)
        return summary

    except KeyError:
        return "Maaf, saya tidak bisa mencari saat ini."

# Header aplikasi
st.title("Chatbot Pupuk Kompos Organik")

# Input pengguna
user_input = st.text_input("Tanyakan sesuatu tentang pupuk kompos:")

if user_input:
    st.write("🔄 Sedang memproses...")
    response = google_search(user_input)
    
    # Menampilkan jawaban dengan format yang lebih rapi
    st.markdown(f"**Jawaban:**\n\n{response}")
