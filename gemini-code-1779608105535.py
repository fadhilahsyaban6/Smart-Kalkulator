import streamlit as st
import numpy as np
import pandas as pd
import math

# ==========================================
# KONFIGURASI HALAMAN & STYLE
# ==========================================
st.set_page_config(page_title="Smart Physics Calculator", page_icon="⚛️", layout="wide")

st.markdown("""
    <style>
    .stButton>button { width: 100%; background-color: #007bff; color: white; border-radius: 8px; }
    .stButton>button:hover { background-color: #0056b3; color: white; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("⚛️ Smart Fisika")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Beranda", "Catatan Rumus & Cheat Sheet", "Kalkulator Fisika", "Auto Unit Converter", "Kuis Fisika Dasar"]
)

# ==========================================
# MENU 1: BERANDA
# ==========================================
if menu == "Beranda":
    st.title("🚀 Selamat Datang di Smart Physics Calculator")
    st.subheader("Asisten Digital Belajar dan Menyelesaikan Masalah Fisika")
    
    st.markdown("""
    Aplikasi ini dirancang khusus untuk membantu mahasiswa dalam memahami konsep fisika dasar secara lebih intuitif. 
    Kelebihan kalkulator ini adalah menyediakan **langkah pengerjaan lengkap** secara transparan agar Anda memahami proses di balik angka yang muncul.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 **Mekanika & Pengukuran**\nPelajari ketelitian jangka sorong, kalkulasi galat praktikum, hingga sudut reposisi material.")
    with col2:
        st.success("💧 **Fluida & Termal**\nHitung koefisien viskositas fluida (Hukum Stokes) dan efek pemuaian panjang pada benda.")
    with col3:
        st.warning("📝 **Evaluasi Mandiri**\nUji pemahaman teoritis dan hitungan Anda melalui menu Kuis Interaktif tingkat kuliah dasar.")

    st.markdown("---")
    st.subheader("💡 Tips Singkat Praktikum Fisika")
    st.write("1. **Cek Satuan:** Selalu ubah besaran ke Satuan Internasional (SI) sebelum memasukkan angka ke rumus.")
    st.write("2. **Perhatikan Galat:** Nilai galat yang kecil menunjukkan tingkat presisi yang tinggi pada percobaan Anda.")

# ==========================================
# MENU 2: CHEAT SHEET
# ==========================================
elif menu == "Catatan Rumus & Cheat Sheet":
    st.title("📚 Kumpulan Catatan Rumus & Cheat Sheet")
    
    tab1, tab2 = st.tabs(["📊 Tabel Satuan Internasional (SI)", "🌌 Konstanta Fisika Penting"])
    
    with tab1:
        st.subheader("Satuan Dasar & Turunan")
        data_satuan = {
            "Besaran": ["Panjang", "Massa", "Waktu", "Gaya", "Tekanan", "Energi/Usaha", "Kerapatan (Massa Jenis)"],
            "Satuan SI": ["Meter (m)", "Kilogram (kg)", "Sekon (s)", "Newton (N)", "Pascal (Pa)", "Joule (J)", "kg/m³"],
            "Dimensi": ["[L]", "[M]", "[T]", "[M][L][T]⁻²", "[M][L]⁻¹[T]⁻²", "[M][L]²[T]⁻²", "[M][L]⁻³"]
        }
        st.table(pd.DataFrame(data_satuan))
        
    with tab2:
        st.subheader("Konstanta Fisika yang Sering Digunakan")
        data_konstanta = {
            "Simbol": ["g", "c", "G", "R", "e"],
            "Nama Konstanta": ["Percepatan Gravitasi Bumi", "Kecepatan Cahaya", "Konstanta Gravitasi Universal", "Konstanta Gas Ideal", "Muatan Elektron"],
            "Nilai Ketetapan": ["9.8 m/s²", "3 x 10⁸ m/s", "6.674 x 10⁻¹¹ N·m²/kg²", "8.314 J/(mol·K)", "1.602 x 10⁻¹⁹ C"]
        }
        st.table(pd.DataFrame(data_konstanta))

# ==========================================
# MENU 3: KALKULATOR FISIKA
# ==========================================
elif menu == "Kalkulator Fisika":
    st.title("🧮 Kalkulator Fisika Pintar")
    st.caption("Isi nilai yang diketahui untuk mendapatkan hasil dan langkah pengerjaannya.")
    
    topik = st.selectbox(
        "Pilih Topik Kalkulator:",
        ["Kerapatan (Massa Jenis)", "Mencari Nilai Galat", "Viskositas (Hukum Stokes)", 
         "Cara Baca Jangka Sorong", "Sudut Reposisi", "Koefisien Muai Panjang"]
    )
    
    st.markdown("---")
    
    if topik == "Kerapatan (Massa Jenis)":
        st.subheader("⚙️ Kalkulator Kerapatan (𝜌)")
        st.write("**Rumus:** $𝜌 = \\frac{m}{V}$")
        
        m = st.number_input("Masukkan Massa (m) dalam kg:", value=1.0, min_value=0.0)
        v = st.number_input("Masukkan Volume (V) dalam m³:", value=2.0, min_value=0.0001)
        
        if st.button("Hitung Kerapatan"):
            rho = m / v
            st.success(f"**Hasil Akhir:** 𝜌 = {rho:.4f} kg/m³")
            st.markdown("**Langkah Pengerjaan:**")
            st.code(f"1. Diketahui: m = {m} kg, V = {v} m³\n2. Gunakan rumus 𝜌 = m / V\n3. 𝜌 = {m} / {v}\n4. Hasil = {rho:.4f} kg/m³")

    elif topik == "Mencari Nilai Galat":
        st.subheader("⚙️ Kalkulator Analisis Galat (Error)")
        st.write("Mengukur tingkat kesalahan atau deviasi hasil praktikum dari nilai teoretis.")
        
        n_sebenarnya = st.number_input("Nilai Sebenarnya (Teoretis / Literatur):", value=10.0)
        n_percobaan = st.number_input("Nilai Hasil Percobaan (Observasi):", value=9.8)
        
        if st.button("Hitung Galat"):
            galat_mutlak = abs(n_sebenarnya - n_percobaan)
            galat_relatif = (galat_mutlak / n_sebenarnya) * 100 if n_sebenarnya != 0 else 0
            
            st.info(f"**Galat Mutlak:** {galat_mutlak:.4f}")
            st.success(f"**Galat Relatif:** {galat_relatif:.2f}%")
            
            st.markdown("**Langkah Pengerjaan:**")
            st.code(f"1. Galat Mutlak = |Nilai Sebenarnya - Nilai Percobaan|\n"
                    f"   Galat Mutlak = |{n_sebenarnya} - {n_percobaan}| = {galat_mutlak:.4f}\n"
                    f"2. Galat Relatif = (Galat Mutlak / Nilai Sebenarnya) * 100%\n"
                    f"   Galat Relatif = ({galat_mutlak:.4f} / {n_sebenarnya}) * 100% = {galat_relatif:.2f}%")

    elif topik == "Viskositas (Hukum Stokes)":
        st.subheader("⚙️ Kalkulator Viskositas Fluida (𝜂)")
        st.write("**Rumus:** $𝜂 = \\frac{2r^2g(𝜌_b - 𝜌_f)}{9v}$")
        
        r = st.number_input("Jari-jari bola (r) dalam meter:", value=0.005, format="%.5f")
        rho_b = st.number_input("Kerapatan Bola (𝜌b) dalam kg/m³:", value=7800.0)
        rho_f = st.number_input("Kerapatan Fluida (𝜌f) dalam kg/m³:", value=1260.0)
        v_terminal = st.number_input("Kecepatan Terminal bola (v) dalam m/s:", value=0.5)
        g = 9.8
        
        if st.button("Hitung Viskositas"):
            if v_terminal > 0:
                pembilang = 2 * (r**2) * g * (rho_b - rho_f)
                penyebut = 9 * v_terminal
                eta = pembilang / penyebut
                
                st.success(f"**Hasil Akhir:** Koefisien Viskositas (𝜂) = {eta:.4f} Pa·s")
                st.markdown("**Langkah Pengerjaan:**")
                st.code(f"1. Diketahui: r={r} m, 𝜌b={rho_b} kg/m³, 𝜌f={rho_f} kg/m³, v={v_terminal} m/s, g=9.8 m/s²\n"
                        f"2. Selisih Kerapatan (𝜌b - 𝜌f) = {rho_b} - {rho_f} = {rho_b - rho_f} kg/m³\n"
                        f"3. Masukkan ke rumus: 𝜂 = (2 * ({r}^2) * 9.8 * {rho_b - rho_f}) / (9 * {v_terminal})\n"
                        f"4. Hasil Akhir = {pembilang:.5f} / {penyebut:.5f} = {eta:.4f} Pa·s")
            else:
                st.error("Kecepatan terminal (v) harus lebih besar dari nol.")

    elif topik == "Cara Baca Jangka Sorong":
        st.subheader("⚙️ Kalkulator Pembacaan Jangka Sorong")
        
        skala_utama = st.number_input("Masukkan Nilai Skala Utama (cm) [Angka sebelum nol nonius]:", value=2.4, step=0.1)
        skala_nonius = st.number_input("Masukkan Garis Nonius yang berimpit tegak lurus (skala skala 0-10):", value=7, min_value=0, max_value=20)
        ketelitian = st.selectbox("Ketelitian Alat (mm):", [0.1, 0.05, 0.02])
        
        if st.button("Hitung Hasil Pengukuran"):
            nonius_cm = (skala_nonius * ketelitian) / 10
            hasil_ukur = skala_utama + nonius_cm
            
            st.success(f"**Hasil Pengukuran:** {hasil_ukur:.3f} cm")
            st.markdown("**Langkah Pembacaan:**")
            st.code(f"1. Skala Utama (SU) = {skala_utama} cm\n"
                    f"2. Skala Nonius (SN) = {skala_nonius} x {ketelitian} mm = {skala_nonius * ketelitian} mm = {nonius_cm} cm\n"
                    f"3. Hasil Pengukuran Total = SU + SN = {skala_utama} + {nonius_cm} = {hasil_ukur:.3f} cm")

    elif topik == "Sudut Reposisi":
        st.subheader("⚙️ Kalkulator Sudut Reposisi (𝜃)")
        st.write("Mengukur sudut longsor maksimum tumpukan material granular basah/kering. Rumus: $\\tan(𝜃) = \\frac{h}{r}$")
        
        h = st.number_input("Tinggi tumpukan kerucut material (h) dalam meter:", value=0.5)
        r_alas = st.number_input("Jari-jari lingkaran alas kerucut (r) dalam meter:", value=0.8)
        
        if st.button("Hitung Sudut Reposisi"):
            if r_alas > 0:
                tan_theta = h / r_alas
                theta_rad = math.atan(tan_theta)
                theta_deg = math.degrees(theta_rad)
                
                st.success(f"**Hasil Akhir:** Sudut Reposisi (𝜃) = {theta_deg:.2f}°")
                st.markdown("**Langkah Pengerjaan:**")
                st.code(f"1. tan(𝜃) = h / r = {h} / {r_alas} = {tan_theta:.4f}\n"
                        f"2. 𝜃 = arctan({tan_theta:.4f})\n"
                        f"3. Hasil dalam derajat = {theta_deg:.2f}°")
            else:
                st.error("Jari-jari alas harus lebih besar dari 0.")

    elif topik == "Koefisien Muai Panjang":
        st.subheader("⚙️ Kalkulator Pemuaian Panjang Benda Padat")
        st.write("**Rumus:** $𝛥L = L_0 \\cdot \\alpha \\cdot 𝛥T$")
        
        l0 = st.number_input("Panjang Awal Benda (L0) dalam meter:", value=10.0)
        alpha = st.number_input("Koefisien Muai Panjang (α) per °C [Contoh Besi = 0.000012]:", value=0.000012, format="%.6f")
        t_awal = st.number_input("Suhu Mula-mula T1 (°C):", value=25.0)
        t_akhir = st.number_input("Suhu Akhir T2 (°C):", value=100.0)
        
        if st.button("Hitung Pertambahan Panjang"):
            dt = t_akhir - t_awal
            dl = l0 * alpha * dt
            l_total = l0 + dl
            
            st.success(f"**Pertambahan Panjang (𝛥L):** {dl:.6f} meter")
            st.info(f"**Panjang Total Akhir (Lt):** {l_total:.6f} meter")
            st.markdown("**Langkah Pengerjaan:**")
            st.code(f"1. Cari Selisih Suhu (𝛥T) = T2 - T1 = {t_akhir} - {t_awal} = {dt} °C\n"
                    f"2. Hitung 𝛥L = L0 * α * 𝛥T\n"
                    f"   𝛥L = {l0} * {alpha:.6f} * {dt} = {dl:.6f} meter\n"
                    f"3. Panjang Total = L0 + 𝛥L = {l0} + {dl:.6f} = {l_total:.6f} meter")

# ==========================================
# MENU 4: AUTO UNIT CONVERTER
# ==========================================
elif menu == "Auto Unit Converter":
    st.title("🔄 Auto Unit Converter")
    st.write("Konversi otomatis besaran fisika tanpa perlu menghitung manual.")
    
    kategori = st.selectbox("Pilih Kategori Besaran:", ["Panjang", "Massa", "Suhu"])
    
    if kategori == "Panjang":
        nilai = st.number_input("Masukkan Angka:", value=1.0)
        dari = st.selectbox("Dari Satuan:", ["Meter (m)", "Centimeter (cm)", "Kilometer (km)"])
        ke = st.selectbox("Ke Satuan:", ["Meter (m)", "Centimeter (cm)", "Kilometer (km)"])
        
        faktor = {"Meter (m)": 1.0, "Centimeter (cm)": 0.01, "Kilometer (km)": 1000.0}
        hasil = nilai * (faktor[dari] / faktor[ke])
        st.success(f"**Hasil Konversi:** {nilai} {dari} = {hasil} {ke}")
        
    elif kategori == "Massa":
        nilai = st.number_input("Masukkan Angka:", value=1.0)
        dari = st.selectbox("Dari Satuan:", ["Kilogram (kg)", "Gram (g)"])
        ke = st.selectbox("Ke Satuan:", ["Kilogram (kg)", "Gram (g)"])
        
        faktor = {"Kilogram (kg)": 1.0, "Gram (g)": 0.001}
        hasil = nilai * (faktor[dari] / faktor[ke])
        st.success(f"**Hasil Konversi:** {nilai} {dari} = {hasil} {ke}")

    elif kategori == "Suhu":
        nilai = st.number_input("Masukkan Nilai awal (°Celsius):", value=0.0)
        st.write("**Hasil Konversi Langsung:**")
        st.info(f"🌡️ **Kelvin (K):** {nilai + 273.15} K")
        st.info(f"🌡️ **Fahrenheit (°F):** {(nilai * 9/5) + 32} °F")
        st.info(f"🌡️ **Reamur (°R):** {nilai * 4/5} °R")

# ==========================================
# MENU 5: KUIS FISIKA DASAR
# ==========================================
elif menu == "Kuis Fisika Dasar":
    st.title("✍️ Kuis Mandiri Fisika (Tingkat Kuliah Dasar)")
    st.write("Uji pemahaman Anda. Klik tombol di bawah untuk melihat skor dan pembahasan otomatis.")
    
    soal_list = [
        {
            "tipe": "PG",
            "pertanyaan": "Gaya hambat atau gesekan berbanding lurus dengan viskositas yang dialami oleh benda bulat di dalam fluida sebanding dengan Hukum...",
            "opsi": ["A. Archimedes", "B. Stokes", "C. Bernoulli", "D. Pascal"],
            "jawaban": "B. Stokes",
            "pembahasan": "Hukum Stokes menyatakan bahwa gaya hambat (Ff) pada bola yang bergerak di dalam fluida kental dipengaruhi oleh koefisien viskositas fluida."
        },
        {
            "tipe": "PG",
            "pertanyaan": "Manakah di bawah ini yang merupakan dimensi dari besaran Tekanan?",
            "opsi": ["A. [M][L]⁻¹[T]⁻²", "B. [M][L][T]⁻²", "C. [M][L]²[T]⁻²", "D. [M][L]⁻³"],
            "jawaban": "A. [M][L]⁻¹[T]⁻²",
            "pembahasan": "Tekanan = Gaya / Luas = (kg·m/s²) / m² = kg / (m·s²). Dimensinya adalah [M][L]⁻¹[T]⁻²."
        },
        {
            "tipe": "Isian",
            "pertanyaan": "Jika sebatang logam dipanaskan dan mengalami kenaikan suhu, sifat fisik panjangnya akan bertambah. Fenomena ini disebut apa? (Isi dengan 1 kata huruf kecil)",
            "jawaban": "pemuaian",
            "pembahasan": "Pemuaian adalah bertambahnya ukuran zat (panjang, luas, atau volume) akibat menerima energi panas (kalor)."
        }
    ]
    
    skor = 0
    with st.form("kuis_fisika"):
        user_ans = {}
        for i, q in enumerate(soal_list):
            st.markdown(f"**Soal {i+1}: {q['pertanyaan']}**")
            if q["tipe"] == "PG":
                user_ans[i] = st.radio(f"Pilih Jawaban Soal {i+1}:", q["opsi"], key=f"q_pg_{i}")
            else:
                user_ans[i] = st.text_input(f"Ketik Jawaban Soal {i+1}:", key=f"q_is_{i}").strip().lower()
            st.markdown("---")
            
        submit = st.form_submit_button("Kirim & Evaluasi Jawaban")
        
    if submit:
        st.subheader("📊 Pembahasan & Hasil Analisis Kuis")
        for i, q in enumerate(soal_list):
            if user_ans[i] == q["jawaban"]:
                st.success(f"✅ **Soal {i+1}: BENAR**")
                skor += 1
            else:
                st.error(f"❌ **Soal {i+1}: SALAH** (Jawaban Anda: {user_ans[i]} | Kunci: {q['jawaban']})")
            st.caption(f"💡 *Pembahasan:* {q['pembahasan']}")
            st.write(" ")
            
        st.balloons()
        st.metric(label="Total Nilai Benar Anda", value=f"{skor} / {len(soal_list)}")