import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ========================== #
# 🔹 Konfigurasi Dashboard 🔹 #
# ========================== #
st.set_page_config(
    page_title="Bike Sharing & Customer Segmentation Dashboard",
    page_icon="🚲",
    layout="wide"
)

# ========================== #
# 🔹 Membaca Dataset 🔹 #
# ========================== #
# Menggunakan path relatif berdasarkan lokasi script
# Dapatkan path absolut ke direktori yang berisi script ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definisikan path ke file data relatif terhadap script
data_file = os.path.join(current_dir, "data.csv")
rfm_file = os.path.join(current_dir, "customer_segmentation.csv")

# Menampilkan lokasi file untuk membantu debugging
st.sidebar.caption(f"Lokasi file data: {data_file}")
st.sidebar.caption(f"Lokasi file RFM: {rfm_file}")

try:
    df = pd.read_csv(data_file)
    st.success("✅ Dataset berhasil dimuat!")
except FileNotFoundError:
    st.error(f"❌ File '{data_file}' tidak ditemukan. Pastikan file berada di folder yang sama dengan script!")
    # Alternatif jika file tetap tidak ditemukan
    alternative_data_path = os.path.join(os.getcwd(), "data.csv")
    st.info(f"Mencoba alternatif path: {alternative_data_path}")
    try:
        df = pd.read_csv(alternative_data_path)
        st.success("✅ Dataset berhasil dimuat menggunakan path alternatif!")
    except FileNotFoundError:
        st.error("❌ File data tidak dapat ditemukan. Upload file atau periksa nama file!")
        st.stop()
except Exception as e:
    st.error(f"❌ Terjadi kesalahan saat membaca file: {e}")
    st.stop()

try:
    df_rfm = pd.read_csv(rfm_file)
    st.success("✅ Dataset RFM berhasil dimuat!")
except FileNotFoundError:
    st.error(f"❌ File '{rfm_file}' tidak ditemukan. Pastikan file berada di folder yang sama dengan script!")
    # Alternatif jika file tetap tidak ditemukan
    alternative_rfm_path = os.path.join(os.getcwd(), "customer_segmentation.csv")
    st.info(f"Mencoba alternatif path: {alternative_rfm_path}")
    try:
        df_rfm = pd.read_csv(alternative_rfm_path)
        st.success("✅ Dataset RFM berhasil dimuat menggunakan path alternatif!")
    except FileNotFoundError:
        st.error("❌ File RFM tidak dapat ditemukan. Upload file atau periksa nama file!")
        st.stop()
except Exception as e:
    st.error(f"❌ Terjadi kesalahan saat membaca file: {e}")
    st.stop()

# ========================== #
# 🔹 Header Dashboard 🔹 #
# ========================== #
st.markdown("<h1 style='text-align: center;'>🚲 Bike Sharing & Customer Segmentation 📊</h1>", unsafe_allow_html=True)

# ========================== #
# 🔹 Filter Data 🔹 #
# ========================== #
st.sidebar.header("🔎 Filter Data")
segment_options = df_rfm['Customer_Segment'].unique().tolist()
selected_segment = st.sidebar.multiselect("Pilih Segmentasi Customer", segment_options, default=segment_options)

# ========================== #
# 🔹 Tabel Segmentasi Customer 🔹 #
# ========================== #
st.subheader("📋 Tabel Segmentasi Customer")

# Filter berdasarkan pilihan pengguna
filtered_df = df_rfm[df_rfm['Customer_Segment'].isin(selected_segment)]
st.dataframe(filtered_df.head(10))  # Menampilkan 10 data pertama

# ========================== #
# 🔹 Visualisasi Distribusi Customer 🔹 #
# ========================== #
st.subheader("👥 Distribusi Customer Berdasarkan Segmentasi RFM")

# Mengecek apakah kolom 'Customer_Segment' tersedia
df_rfm['Customer_Segment'] = df_rfm['Customer_Segment'].astype(str)  # Pastikan format teks
customer_count = df_rfm['Customer_Segment'].value_counts().reset_index()
customer_count.Columns = ["Segment", "Jumlah Customer"]

# Membuat visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=customer_count, x="Segment", y="Jumlah Customer", palette="Pastel", ax=ax)
ax.set_xlabel("Kategori Customer")
ax.set_ylabel("Jumlah Customer")
ax.set_title("Distribusi Customer Berdasarkan Segmentasi RFM")
plt.xticks(Rotation=30)

# Menampilkan plot di Streamlit
st.pyplot(fig)

# ========================== #
# 🔹 Statistik Ringkasan 🔹 #
# ========================== #
st.sidebar.subheader("📊 Statistik Ringkasan")

# Menampilkan jumlah total customer per segment jika kolom "Customer_ID" ada
If "customer_id" in df_rfm.Columns:
    total_customer = df_rfm.groupby("Customer_Segment")["customer_id"].count().reset_index()
    total_customer.Columns = ["Segment", "Total Customer"]
    st.sidebar.write("Total Customer per Segmentasi:")
    st.sidebar.DataFrame(total_customer)

# ========================== #
# 🔹 Footer Dashboard 🔹 #
# ========================== #
st.Markdown("---")
st.Markdown("<p style='text-align: center;'&gt; Sandy Tirta Yudha | © 2025>", unsafe_allow_html=true)
