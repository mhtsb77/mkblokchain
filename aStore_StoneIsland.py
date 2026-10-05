import streamlit as st
from coree import Blockchain  # Import the Blockchain class from coree.py

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Stone Island Store",
    page_icon="🧥",
    layout="wide"
)


# =========================================================
# JUDUL
# =========================================================

st.title("🧥 Stone Island Store")
st.subheader("Sistem Penjualan Produk Berbasis Blockchain")
st.caption(
    "Pencatatan produk dan transaksi menggunakan teknologi Blockchain"
)


# =========================================================
# SESSION STATE
# =========================================================

if "my_blockchain" not in st.session_state:
    st.session_state.my_blockchain = Blockchain()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🧥 Stone Island")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Dashboard",
        "Tambah Produk",
        "Transaksi",
        "Blockchain",
        "Validasi Blockchain"
    ]
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "Dashboard":

    st.header("📊 Dashboard Stone Island")

    blockchain = st.session_state.my_blockchain

    jumlah_block = len(blockchain.chain)
    jumlah_transaksi = jumlah_block - 1

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Jumlah Block",
            jumlah_block
        )

    with col2:
        st.metric(
            "Jumlah Transaksi",
            jumlah_transaksi
        )

    with col3:
        status = blockchain.is_chain_valid()

        if status:
            st.metric(
                "Status Blockchain",
                "VALID"
            )
        else:
            st.metric(
                "Status Blockchain",
                "TIDAK VALID"
            )

    st.divider()

    st.info(
        "Selamat datang di Stone Island Store. "
        "Gunakan menu di sebelah kiri untuk mengelola produk "
        "dan transaksi."
    )


# =========================================================
# TAMBAH PRODUK
# =========================================================

elif menu == "Tambah Produk":

    st.header("➕ Tambah Produk Stone Island")

    with st.form("form_tambah_produk"):

        nama_produk = st.text_input(
            "Nama Produk",
            placeholder="Contoh: Stone Island Hoodie"
        )

        kategori = st.selectbox(
            "Kategori",
            [
                "Hoodie",
                "Jacket",
                "T-Shirt",
                "Sweater",
                "Pants",
                "Accessories"
            ]
        )

        ukuran = st.selectbox(
            "Ukuran",
            [
                "S",
                "M",
                "L",
                "XL",
                "XXL"
            ]
        )

        harga = st.number_input(
            "Harga Produk",
            min_value=0,
            value=1000000,
            step=50000,
            key="harga_produk"
        )

        stok = st.number_input(
            "Stok",
            min_value=0,
            value=1,
            step=1,
            key="stok_produk"
        )

        status = st.selectbox(
            "Status Produk",
            [
                "Tersedia",
                "Habis"
            ]
        )

        submit = st.form_submit_button(
            "💾 Simpan Produk"
        )

    if submit:

        if nama_produk.strip() == "":
            st.error("Nama produk harus diisi!")

        elif harga <= 0:
            st.error("Harga harus lebih dari 0!")

        elif stok < 0:
            st.error("Stok tidak boleh negatif!")

        else:

            data_produk = {
                "jenis_data": "Produk",
                "nama_produk": nama_produk,
                "kategori": kategori,
                "ukuran": ukuran,
                "harga": harga,
                "stok": stok,
                "status": status
            }

            st.session_state.my_blockchain.add_block(
                data_produk
            )

            st.success(
                "✅ Produk berhasil ditambahkan ke blockchain!"
            )

            st.write("Data Produk:")

            st.json(data_produk)


# =========================================================
# TRANSAKSI
# =========================================================

elif menu == "Transaksi":

    st.header("🛒 Transaksi Penjualan")

    with st.form("form_transaksi"):

        nama_pembeli = st.text_input(
            "Nama Pembeli",
            placeholder="Masukkan nama pembeli"
        )

        nama_produk = st.text_input(
            "Nama Produk",
            placeholder="Contoh: Stone Island Jacket"
        )

        jumlah = st.number_input(
            "Jumlah Barang",
            min_value=1,
            value=1,
            step=1,
            key="jumlah_transaksi"
        )

        harga_satuan = st.number_input(
            "Harga Satuan",
            min_value=0,
            value=1000000,
            step=50000,
            key="harga_transaksi"
        )

        metode_pembayaran = st.selectbox(
            "Metode Pembayaran",
            [
                "Cash",
                "Transfer Bank",
                "E-Wallet"
            ]
        )

        submit_transaksi = st.form_submit_button(
            "💳 Simpan Transaksi"
        )

    if submit_transaksi:

        if nama_pembeli.strip() == "":
            st.error("Nama pembeli harus diisi!")

        elif nama_produk.strip() == "":
            st.error("Nama produk harus diisi!")

        elif harga_satuan <= 0:
            st.error("Harga satuan harus lebih dari 0!")

        else:

            total_harga = jumlah * harga_satuan

            data_transaksi = {
                "jenis_data": "Transaksi",
                "nama_pembeli": nama_pembeli,
                "nama_produk": nama_produk,
                "jumlah": jumlah,
                "harga_satuan": harga_satuan,
                "total_harga": total_harga,
                "metode_pembayaran": metode_pembayaran,
                "status": "Berhasil"
            }

            st.session_state.my_blockchain.add_block(
                data_transaksi
            )

            st.success(
                "✅ Transaksi berhasil dicatat ke blockchain!"
            )

            st.divider()

            st.subheader("🧾 Detail Transaksi")

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"**Pembeli:** {nama_pembeli}"
                )

                st.write(
                    f"**Produk:** {nama_produk}"
                )

                st.write(
                    f"**Jumlah:** {jumlah}"
                )

            with col2:
                st.write(
                    f"**Harga Satuan:** Rp{harga_satuan:,.0f}"
                )

                st.write(
                    f"**Total:** Rp{total_harga:,.0f}"
                )

                st.write(
                    f"**Pembayaran:** {metode_pembayaran}"
                )


# =========================================================
# BLOCKCHAIN
# =========================================================

elif menu == "Blockchain":

    st.header("🔗 Data Blockchain")

    blockchain = st.session_state.my_blockchain

    st.write(
        f"Jumlah Block: **{len(blockchain.chain)}**"
    )

    st.divider()

    for block in blockchain.chain:

        st.subheader(
            f"Block #{block.index}"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Timestamp:** {block.timestamp}"
            )

            st.write(
                f"**Previous Hash:** `{block.previous_hash}`"
            )

        with col2:

            st.write(
                f"**Hash:** `{block.hash}`"
            )

        st.write("**Data:**")

        st.json(block.data)

        st.divider()


# =========================================================
# VALIDASI BLOCKCHAIN
# =========================================================

elif menu == "Validasi Blockchain":

    st.header("🔐 Validasi Blockchain")

    blockchain = st.session_state.my_blockchain

    valid = blockchain.is_chain_valid()

    if valid:

        st.success(
            "✅ Blockchain VALID"
        )

        st.write(
            "Semua block memiliki hash yang sesuai "
            "dan hubungan antar-block masih valid."
        )

    else:

        st.error(
            "❌ Blockchain TIDAK VALID"
        )

        st.write(
            "Terdapat perubahan atau kerusakan pada "
            "data blockchain."
        )

    st.divider()

    st.subheader("Informasi Blockchain")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Block",
            len(blockchain.chain)
        )

    with col2:

        st.metric(
            "Status",
            "VALID" if valid else "TIDAK VALID"
        )