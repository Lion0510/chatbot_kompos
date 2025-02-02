import streamlit as st

# Header aplikasi
st.title("Chatbot Pupuk Kompos Organik")

# Fungsi chatbot sederhana (berbasis rule-based)
def chatbot_response(user_input):
    responses = {
        "apa itu pupuk kompos?": "Pupuk kompos adalah pupuk organik yang dibuat dari bahan alami seperti daun kering, sisa makanan, dan kotoran hewan.",
        "bagaimana cara membuat pupuk kompos?": "1. Siapkan bahan organik\n2. Lapisi bahan dengan tanah\n3. Jaga kelembaban dan aerasi\n4. Tunggu 1-3 bulan hingga kompos matang.",
        "mengapa kompos saya berbau?": "Kompos yang berbau biasanya karena terlalu basah atau kurang aerasi. Tambahkan bahan kering seperti daun kering atau serbuk gergaji dan aduk secara rutin.",
    }
    return responses.get(user_input.lower(), "Maaf, saya tidak mengerti. Coba tanyakan pertanyaan lain.")

# Input pengguna
user_input = st.text_input("Tanyakan sesuatu tentang pupuk kompos:")

if user_input:
    response = chatbot_response(user_input)
    st.write("🤖 Chatbot:", response)
