import streamlit as st

st.set_page_config(page_title="CV App", page_icon="🎓", layout="wide")

# pembuatan sidebar
st.sidebar.title("⚙️pengaturan profile")
st.sidebar.write("masukan data diri anda di bawah ini:")

# komponen imputan
nama = st.sidebar.text_input("Nama:", "Nama Lengkap")
nim = st.sidebar.text_input("NIM:", "NIM Anda")
jurusan = st.sidebar.selectbox("Jurusan:", ["Teknik Informartika", "Sistem Informasi", "Teknik Eloktro", "Teknik Mesin"])

deskripsi = st.sidebar.text_area("Deskripsi Diri:", "Tuliskan deskripsi singkat tentang diri anda di sini.")

#Area Utama
st.title("curiculum vitae")
st.markdown("----------")

kolom_kiri, kolom_kanan = st.columns([2,1])
with kolom_kiri:
    st.header(nama)
    st.image("foto.jpeg", width=150)
    st.subheader(f"{jurusan}-(NIM: {nim})")

    with kolom_kanan:
        st.write(f"tentang saya: {deskripsi}")