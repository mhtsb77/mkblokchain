import streamlit as st
from core import Blockchain


# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Blockchain Supply Chain",
    page_icon="🔗",
    layout="wide"
)

st.title("📦 Blockchain Supply Chain")
st.caption(
    "Sistem pencatatan rantai pasok menggunakan teknologi Blockchain"
)


# ==========================================
# SESSION STATE
# ==========================================

if "my_blockchain" not in st.session_state:
    st.session_state.my_blockchain = Blockchain()


# ==========================================
# DATA STUDI KASUS
# ==========================================

studi_kasus = {
    "☕ Kopi Halal": {
        "produk": "Biji Kopi",
        "aktor": "Petani Kopi",
        "satuan": "Kg"
    },

    "🍚 Beras": {
        "produk": "Beras",
        "aktor": "Petani Padi",
        "satuan": "Kg"
    },

    "🐟 Ikan": {
        "produk": "Ikan Segar",
        "aktor": "Nelayan",
        "satuan": "Kg"
    },

    "🍫 Kakao": {
        "produk": "Biji Kakao",
        "aktor": "Petani Kakao",
        "satuan": "Kg"
    },

    "🥩 Daging Halal": {
        "produk": "Daging Sapi",
        "aktor": "Peternak",
        "satuan": "Kg"
    },

    "🥛 Susu": {
        "produk": "Susu Segar",
        "aktor": "Peternak Sapi",
        "satuan": "Liter"
    },

    "🌾 Gandum": {
        "produk": "Gandum",
        "aktor": "Petani Gandum",
        "satuan": "Kg"
    },

    "💊 Obat": {
        "produk": "Obat",
        "aktor": "Produsen Obat",
        "satuan": "Box"
    },

    "👕 Tekstil": {
        "produk": "Kain",
        "aktor": "Produsen Tekstil",
        "satuan": "Meter"
    },

    "📦 Distribusi Barang": {
        "produk": "Barang",
        "aktor": "Distributor",
        "satuan": "Unit"
    }
}


# ==========================================
# SIDEBAR - PILIH STUDI KASUS
# ==========================================

st.sidebar.header("📋 Studi Kasus")

pilihan_kasus = st.sidebar.selectbox(
    "Pilih Studi Kasus:",
    list(studi_kasus.keys()),
    key="pilihan_kasus"
)

data_kasus = studi_kasus[pilihan_kasus]


st.sidebar.info(
    f"""
**Studi Kasus:**
{pilihan_kasus}

**Produk:**
{data_kasus['produk']}

**Aktor Awal:**
{data_kasus['aktor']}
"""
)


# ==========================================
# SIDEBAR - INPUT DATA
# ==========================================

st.sidebar.header("✨ Tambah Data Baru")


aktor = st.sidebar.text_input(
    "Nama Petani/Aktor:",
    value=data_kasus["aktor"],
    key="aktor_input"
)


produk = st.sidebar.text_input(
    "Nama Produk:",
    value=data_kasus["produk"],
    key="produk_input"
)


jumlah = st.sidebar.number_input(
    f"Jumlah ({data_kasus['satuan']}):",
    min_value=1,
    value=1,
    step=1,
    key="jumlah_input"
)


lokasi = st.sidebar.text_input(
    "Lokasi:",
    key="lokasi_input"
)


status = st.sidebar.selectbox(
    "Status Produk:",
    [
        "Diproduksi",
        "Dipanen",
        "Diproses",
        "Diperiksa",
        "Disimpan",
        "Didistribusikan",
        "Diterima Konsumen"
    ],
    key="status_input"
)


sertifikasi = st.sidebar.selectbox(
    "Status Sertifikasi:",
    [
        "Belum Diverifikasi",
        "Terverifikasi",
        "Halal Certified",
        "Organik Certified"
    ],
    key="sertifikasi_input"
)


# ==========================================
# TAMBAHKAN DATA KE BLOCKCHAIN
# ==========================================

if st.sidebar.button(
    "⛓️ Tambahkan ke Blockchain",
    key="tambah_block_button"
):

    if aktor and produk and lokasi:

        data_transaksi = (
            f"Studi Kasus: {pilihan_kasus} | "
            f"Aktor: {aktor} | "
            f"Produk: {produk} | "
            f"Jumlah: {jumlah} {data_kasus['satuan']} | "
            f"Lokasi: {lokasi} | "
            f"Status: {status} | "
            f"Sertifikasi: {sertifikasi}"
        )

        # Pastikan method tersedia
        if hasattr(
            st.session_state.my_blockchain,
            "add_block"
        ):

            st.session_state.my_blockchain.add_block(
                data_transaksi
            )

            st.sidebar.success(
                "✅ Blok berhasil ditambahkan!"
            )

        else:

            st.sidebar.error(
                "❌ Method add_block() belum tersedia "
                "di class Blockchain pada core.py"
            )

    else:

        st.sidebar.error(
            "⚠️ Lengkapi semua data!"
        )


# ==========================================
# MAIN AREA
# ==========================================

st.subheader(
    f"📜 Blockchain Ledger - {pilihan_kasus}"
)

st.write(
    f"""
Sistem ini mencatat perjalanan **{data_kasus['produk']}**
dari proses produksi hingga distribusi menggunakan teknologi Blockchain.
"""
)


# ==========================================
# STATUS BLOCKCHAIN
# ==========================================

if hasattr(
    st.session_state.my_blockchain,
    "is_chain_valid"
):

    is_valid = (
        st.session_state.my_blockchain.is_chain_valid()
    )

    if is_valid:

        st.success(
            "✔️ Status Jaringan: Rantai Valid (Aman)"
        )

    else:

        st.error(
            "❌ PERINGATAN: Integritas Rantai Rusak!"
        )

else:

    st.warning(
        "⚠️ Method is_chain_valid() belum tersedia di core.py"
    )


# ==========================================
# INFORMASI STUDI KASUS
# ==========================================

st.subheader("📊 Informasi Studi Kasus")

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Studi Kasus",
        pilihan_kasus
    )


with col2:

    st.metric(
        "Produk",
        data_kasus["produk"]
    )


with col3:

    st.metric(
        "Jumlah Block",
        len(st.session_state.my_blockchain.chain)
    )


# ==========================================
# ALUR SUPPLY CHAIN
# ==========================================

st.subheader("🔄 Alur Supply Chain")


if "Kopi" in pilihan_kasus:

    st.write(
        "🌱 Petani → 🏭 Pengolahan → 🔍 Quality Control → "
        "📦 Distributor → 🏪 Toko → 👤 Konsumen"
    )

elif "Beras" in pilihan_kasus:

    st.write(
        "🌾 Petani → 🏭 Penggilingan → 🔍 Quality Control → "
        "📦 Distributor → 🏪 Toko → 👤 Konsumen"
    )

elif "Ikan" in pilihan_kasus:

    st.write(
        "🎣 Nelayan → 🧊 Penyimpanan → 🔍 Quality Control → "
        "📦 Distributor → 🏪 Pasar → 👤 Konsumen"
    )

elif "Kakao" in pilihan_kasus:

    st.write(
        "🌱 Petani → 🏭 Pengolahan → 📦 Gudang → "
        "🚚 Distributor → 🏪 Toko → 👤 Konsumen"
    )

elif "Daging" in pilihan_kasus:

    st.write(
        "🐄 Peternak → 🥩 Rumah Potong → 🔍 Pemeriksaan Halal → "
        "📦 Pengemasan → 🚚 Distributor → 👤 Konsumen"
    )

elif "Susu" in pilihan_kasus:

    st.write(
        "🐄 Peternak → 🥛 Pengumpulan → 🏭 Pengolahan → "
        "🧊 Penyimpanan → 🚚 Distributor → 👤 Konsumen"
    )

elif "Gandum" in pilihan_kasus:

    st.write(
        "🌾 Petani → 🏭 Pengolahan → 📦 Gudang → "
        "🚚 Distributor → 🏪 Toko → 👤 Konsumen"
    )

elif "Obat" in pilihan_kasus:

    st.write(
        "🏭 Produsen → 🔬 Quality Control → 📦 Gudang → "
        "🚚 Distributor → 🏥 Apotek → 👤 Konsumen"
    )

elif "Tekstil" in pilihan_kasus:

    st.write(
        "🌱 Bahan Baku → 🏭 Produksi → 🔍 Quality Control → "
        "📦 Distributor → 🏪 Toko → 👤 Konsumen"
    )

else:

    st.write(
        "🏭 Produsen → 📦 Gudang → 🚚 Distributor → "
        "🏪 Toko → 👤 Konsumen"
    )


# ==========================================
# MENAMPILKAN BLOCKCHAIN
# ==========================================

st.subheader("🔗 Detail Blockchain")


if len(st.session_state.my_blockchain.chain) == 0:

    st.info(
        "📭 Belum ada block. Silakan tambahkan data melalui sidebar."
    )

else:

    for block in st.session_state.my_blockchain.chain:

        with st.expander(
            f"Blok #{block.index} | Hash: {block.hash[:15]}..."
        ):

            col1, col2 = st.columns(2)

            with col1:

                st.write("**📦 Data Payload:**")

                if block.index == 1:

                    st.info(block.data)

                else:

                    st.success(block.data)

                st.write(
                    f"**Timestamp:** {block.timestamp}"
                )

            with col2:

                st.write("**🔐 Kriptografi:**")

                st.write("**Hash Saat Ini:**")

                st.code(
                    block.hash,
                    language="text"
                )

                st.write(
                    "**Hash Sebelumnya (Pointer):**"
                )

                st.code(
                    block.previous_hash,
                    language="text"
                )