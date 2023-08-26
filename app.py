import streamlit as st

# Judul halaman
st.title("Website Sederhana dengan Streamlit")

# Teks
st.write("Ini adalah contoh teks pada halaman web.")

# Gambar
st.image("https://www.example.com/gambar.jpg", caption="Contoh Gambar", use_column_width=True)

# Input teks
input_text = st.text_input("Masukkan teks di sini", "Tulis sesuatu...")
st.write("Anda menulis:", input_text)

# Pilihan
option = st.selectbox("Pilih opsi:", ("Pilihan 1", "Pilihan 2", "Pilihan 3"))
st.write("Anda memilih:", option)

# Tombol
if st.button("Klik di sini"):
    st.write("Tombol telah diklik!")

# Slider
slider_value = st.slider("Pilih nilai slider:", 0, 100, 50)
st.write("Nilai slider:", slider_value)
