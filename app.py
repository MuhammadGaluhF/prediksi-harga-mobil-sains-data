import streamlit as st
import pandas as pd
import joblib

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Prediksi Harga Mobil",
    page_icon="🚗",
    layout="wide"
)

# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    return joblib.load("car_price_model.pkl")

model = load_model()

feature_columns = [
    "Engine_size",
    "Horsepower",
    "Wheelbase",
    "Width",
    "Length",
    "Curb_weight",
    "Fuel_capacity",
    "Fuel_efficiency"
]

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>
    .main {
        background-color: #f6f8fb;
    }

    .hero {
        padding: 32px;
        border-radius: 24px;
        background: linear-gradient(135deg, #102a43 0%, #243b53 45%, #0f766e 100%);
        color: white;
        margin-bottom: 28px;
        box-shadow: 0px 12px 28px rgba(15, 23, 42, 0.18);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
        font-weight: 800;
    }

    .hero p {
        font-size: 18px;
        color: #d9e2ec;
        margin-bottom: 0px;
    }

    .section-card {
        padding: 26px;
        border-radius: 22px;
        background-color: white;
        box-shadow: 0px 8px 22px rgba(15, 23, 42, 0.08);
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }

    .result-card {
        padding: 30px;
        border-radius: 24px;
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border: 1px solid #facc15;
        box-shadow: 0px 10px 24px rgba(202, 138, 4, 0.16);
        text-align: center;
        margin-bottom: 20px;
    }

    .result-title {
        font-size: 18px;
        font-weight: 700;
        color: #78350f;
        margin-bottom: 8px;
    }

    .result-price {
        font-size: 42px;
        font-weight: 900;
        color: #1f2937;
        margin-bottom: 6px;
    }

    .result-subtitle {
        font-size: 15px;
        color: #78350f;
    }

    .identity-card {
        padding: 24px;
        border-radius: 22px;
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border: 1px solid #93c5fd;
        text-align: center;
        color: #1e3a8a;
        font-weight: 600;
    }

    .small-note {
        font-size: 14px;
        color: #64748b;
    }

    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 14px 20px;
        font-size: 18px;
        font-weight: 700;
        box-shadow: 0px 8px 18px rgba(20, 184, 166, 0.28);
    }

    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #115e59 0%, #0d9488 100%);
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown("""
<div class="hero">
    <h1>🚗 Prediksi Harga Mobil</h1>
    <p>Aplikasi data science untuk memperkirakan harga mobil berdasarkan spesifikasi kendaraan menggunakan model Linear Regression.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.title("📌 Informasi Project")
    st.write("**Mata Kuliah:** Sains Data")
    st.write("**Metode:** CRISP-DM")
    st.write("**Model:** Linear Regression")
    st.write("**Target:** Price in thousands")
    st.divider()
    st.write("Aplikasi ini menerima input spesifikasi mobil, lalu menghasilkan estimasi harga mobil dalam ribuan dollar.")

# =========================
# Main Layout
# =========================
left_col, right_col = st.columns([1.05, 0.95], gap="large")

with left_col:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📝 Input Spesifikasi Mobil")
    st.write("Masukkan spesifikasi kendaraan yang ingin diprediksi harganya.")

    engine_size = st.number_input(
        "Engine Size",
        min_value=0.5,
        max_value=10.0,
        value=2.45,
        step=0.1,
        help="Ukuran mesin kendaraan."
    )

    horsepower = st.number_input(
        "Horsepower",
        min_value=50.0,
        max_value=600.0,
        value=142.5,
        step=5.0,
        help="Tenaga mesin kendaraan."
    )

    wheelbase = st.number_input(
        "Wheelbase",
        min_value=80.0,
        max_value=160.0,
        value=110.05,
        step=0.5,
        help="Jarak sumbu roda kendaraan."
    )

    width = st.number_input(
        "Width",
        min_value=50.0,
        max_value=100.0,
        value=70.25,
        step=0.5,
        help="Lebar kendaraan."
    )

    length = st.number_input(
        "Length",
        min_value=120.0,
        max_value=260.0,
        value=189.75,
        step=0.5,
        help="Panjang kendaraan."
    )

    curb_weight = st.number_input(
        "Curb Weight",
        min_value=1.0,
        max_value=7.0,
        value=3.227,
        step=0.1,
        help="Berat kendaraan."
    )

    fuel_capacity = st.number_input(
        "Fuel Capacity",
        min_value=5.0,
        max_value=40.0,
        value=19.25,
        step=0.5,
        help="Kapasitas bahan bakar."
    )

    fuel_efficiency = st.number_input(
        "Fuel Efficiency",
        min_value=5.0,
        max_value=60.0,
        value=24.0,
        step=1.0,
        help="Efisiensi bahan bakar."
    )

    predict_button = st.button("Hitung Harga Mobil")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📊 Hasil Prediksi")

    input_data = pd.DataFrame([{
        "Engine_size": engine_size,
        "Horsepower": horsepower,
        "Wheelbase": wheelbase,
        "Width": width,
        "Length": length,
        "Curb_weight": curb_weight,
        "Fuel_capacity": fuel_capacity,
        "Fuel_efficiency": fuel_efficiency
    }])

    if predict_button:
        predicted_price = model.predict(input_data)[0]
        predicted_price_dollar = predicted_price * 1000

        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">Perkiraan Harga Mobil</div>
            <div class="result-price">${predicted_price_dollar:,.2f}</div>
            <div class="result-subtitle">{predicted_price:.2f} ribu dollar</div>
        </div>
        """, unsafe_allow_html=True)

        if predicted_price < 20:
            category = "Harga Ekonomis / Menengah"
        elif predicted_price < 40:
            category = "Harga Menengah ke Atas"
        else:
            category = "Harga Premium"

        st.success(f"Kategori estimasi: {category}")

        st.write("**Ringkasan spesifikasi yang dimasukkan:**")
        st.dataframe(input_data, use_container_width=True)

    else:
        st.info("Silakan isi spesifikasi mobil, lalu klik tombol **Hitung Harga Mobil** untuk melihat hasil prediksi.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="identity-card">
        Sistem ini dibuat oleh:<br>
        Muhammad Galuh Ferirakhyan<br>
        NPM: 237006128
    </div>
    """, unsafe_allow_html=True)

# =========================
# Explanation Section
# =========================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("ℹ️ Tentang Aplikasi")
st.write("""
Aplikasi ini dibuat sebagai bagian dari final project mata kuliah Sains Data. 
Model yang digunakan adalah Linear Regression dengan input berupa spesifikasi kendaraan, 
yaitu Engine Size, Horsepower, Wheelbase, Width, Length, Curb Weight, Fuel Capacity, dan Fuel Efficiency.
""")
st.write("""
Hasil prediksi yang ditampilkan merupakan estimasi harga mobil berdasarkan pola data pada dataset Car_sales. 
Nilai harga ditampilkan dalam satuan dollar dan ribuan dollar.
""")
st.markdown('</div>', unsafe_allow_html=True)
