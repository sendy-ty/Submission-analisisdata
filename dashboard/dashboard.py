Import Streamlit as st
Import Pandas as pd
Import matplotlib.pyplot as plt
Import seaborn as sns

# ========================== #
# 🔹 Konfigurasi Dashboard 🔹 #
# ========================== #
st.set_page_config(
    page_title="Bike Sharing &amp; Customer Segmentation Dashboard",
    page_icon="🚲",
    Layout="Wide"
)

# ========================== #
# 🔹 Membaca Dataset 🔹 #
# ========================== #
file_path = "data.csv"  # Sesuaikan dengan path yang diunggah

try:
    df = pd.read_csv(file_path)
    st.success("✅ Dataset berhasil dimuat!")
except FileNotFoundError:
    st.error(f"❌ File '{file_path}' tidak ditemukan. Periksa kembali lokasi file!")
    st.stop()
except Exception as e:
    st.error(f"❌ Terjadi kesalahan saat membaca file: {e}")
    st.stop()

# ========================== #
# 🔹 Header Dashboard 🔹 #
# ========================== #
st.Markdown("<h1 style='text-align: center;'&gt;🚲 Bike Sharing Dashboard 📊1>", unsafe_allow_html=true)

# ========================== #
# 🔹 Statistik Ringkasan 🔹 #
# ========================== #
st.sidebar.subheader("📊 Statistik Ringkasan")

If "count" in df.Columns:
    total_count = df["count"].sum()
    st.sidebar.metric("Total Pengguna Sepeda", total_count)

# ========================== #
# 🔹 Visualisasi data 🔹 #
# ========================== #
st.subheader("📊 Tren Penggunaan Sepeda")

If "datetime" in df.Columns and "count" in df.Columns:
    df["datetime"] = pd.to_datetime(df["datetime"])
    df.set_index("datetime", inplace=True)
    df_resampled = df.resample("D").sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(Data=df_resampled, x=df_resampled.index, y="count", ax=ax)
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Pengguna")
    ax.set_title("Tren Harian Penggunaan Sepeda")
    plt.xticks(Rotation=30)

    st.pyplot(fig)
else:
    st.error("Kolom 'datetime' atau 'count' tidak ditemukan dalam dataset!")

# ========================== #
# 🔹 Footer Dashboard 🔹 #
# ========================== #
st.Markdown("---")
st.Markdown("  Sandy Tirta Yudha | © 2025 ", unsafe_allow_html=true)
