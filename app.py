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
st.sidebar.title("⚛️ Smart Fisika V2.7")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Beranda", "Catatan Rumus & Cheat Sheet", "Kalkulator Fisika", "Auto Unit Converter", "Kuis Fisika Dasar"]
)

# ==========================================
# MENU 1: BERANDA
# ==========================================
if menu == "Beranda":
    st.title("🚀 Smart Physics Calculator - Laboratorium Ed.")
    st.subheader("Asisten Digital Praktikum Fisika & Analisis Data Laboratorium")
    
    st.markdown("""
    Aplikasi ini dirancang untuk mendukung konversi satuan tingkat lanjut (ekstrim makro hingga mikro/nano) 
    serta simulasi perhitungan menggunakan instrumen laboratorium riil seperti **Piknometer** dan **Viskosimeter Ostwald**.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 **Metrologi & Pikno**\nHitung kerapatan cairan murni atau padatan secara presisi lewat simulasi bobot piknometer.")
    with col2:
        st.success("💧 **Viskositas Relatif**\nHitung viskositas sampel cairan dibanding air suling berdasarkan metode waktu alir pipa kapiler.")
    with col3:
        st.warning("📝 **Akurasi Data**\nHitung nilai galat mutlak/relatif untuk memvalidasi tingkat ketelitian hasil pengukuran Anda.")

# ==========================================
# MENU 2: CHEAT SHEET
# ==========================================
elif menu == "Catatan Rumus & Cheat Sheet":
    st.title("📚 Kumpulan Catatan Rumus & Cheat Sheet")
    
    sub_menu = st.selectbox(
        "Pilih Kategori Informasi:",
        ["📊 Tabel Satuan Eksperimen", "🌌 Konstanta Fisika Penting", "📜 Rangkuman Hukum Fisika", "🧮 Kumpulan Rumus Praktis"]
    )
    
    st.markdown("---")
    
    if sub_menu == "📊 Tabel Satuan Eksperimen":
        st.subheader("Satuan Konvensional vs Satuan Mikro Laboratorium")
        st.markdown("""
        *   **Panjang (Gelombang/Partikel):** Satuan SI: *Meter (m)* | Satuan Lab: *Milimeter (mm) / Mikrometer ($\mu m$)*
        *   **Massa (Analitis):** Satuan SI: *Kilogram (kg)* | Satuan Lab: *Gram (g) / Miligram (mg)*
        *   **Volume (Mikro):** Satuan SI: *Meter Kubik ($m^3$)* | Satuan Lab: *Mililiter (mL) / Mikroliter ($\mu L$)*
        *   **Viskositas:** Satuan SI: *Pascal sekon (Pa·s)* | Satuan Lab: *Poise (P) / Centipoise (cP)*
        *   **Kerapatan:** Satuan SI: *kg/$m^3$* | Satuan Lab: *g/$cm^3$ atau g/mL*
        """)
        
    elif sub_menu == "🌌 Konstanta Fisika Penting":
        st.subheader("Konstanta Fisika & Faktor Pengali")
        st.write("- **Percepatan Gravitasi (g):** $9.8\\text{ m/s}^2$ atau $980\\text{ cm/s}^2$")
        st.write("- **Kecepatan Cahaya (c):** $3 \\times 10^8\\text{ m/s}$")
        st.write("- **Kerapatan Air Murni ($4^\\circ\\text{C}$):** $1.000\\text{ g/cm}^3$ atau $1000\\text{ kg/m}^3$")

    elif sub_menu == "📜 Rangkuman Hukum Fisika":
        st.subheader("📜 Bunyi & Penjelasan Hukum Fisika Dasar")
        
        with st.expander("1. Hukum Newton (Mekanika)"):
            st.markdown("""
            *   **Hukum I Newton (Inersia):** 
                $$\Sigma F = 0$$
                *Penjelasan:* Jika gaya total yang bekerja pada benda sama dengan nol, benda yang diam akan tetap diam, dan benda yang bergerak akan tetap bergerak dengan kecepatan konstan. Benda cenderung mempertahankan posisinya.
            *   **Hukum II Newton (Gerak):** 
                $$F = m \cdot a$$
                *Penjelasan:* Percepatan sebuah benda berbanding lurus dengan total gaya yang mengenainya, namun berbanding terbalik dengan massa benda tersebut. Semakin berat benda, butuh gaya lebih besar untuk menggerakkannya.
            *   **Hukum III Newton (Aksi-Reaksi):** 
                $$F_{\\text{aksi}} = -F_{\\text{reaksi}}$$
                *Penjelasan:* Ketika Anda memberikan gaya pada suatu benda (aksi), benda tersebut akan membalas dengan gaya yang sama besar namun arahnya berlawanan (reaksi).
            """)
            
        with st.expander("2. Hukum Fluida (Ostwald, Archimedes & Bernoulli)"):
            st.markdown("""
            *   **Viskositas Relatif (Ostwald):** 
                $$\\eta_1 = \\frac{t_1 \\cdot \\rho_1}{t_2 \\cdot \\rho_2} \\cdot \\eta_2$$
                *Penjelasan:* Menentukan kekentalan (viskositas) suatu cairan sampel dengan membandingkan waktu alir ($t$) dan densitas ($\rho$) sampel tersebut terhadap cairan referensi yang sudah diketahui nilai viskositasnya (biasanya air suling).
            *   **Hukum Archimedes:** 
                $$F_a = \rho_f \cdot g \cdot V_{\\text{tercelup}}$$
                *Penjelasan:* Setiap benda yang dicelupkan ke dalam fluida akan menerima gaya angkat ke atas ($F_a$) yang besarnya persis sama dengan berat fluida yang ditumpahkan atau dipindahkan oleh benda tersebut.
            *   **Hukum Bernoulli:** 
                $$P + \\frac{1}{2}\rho v^2 + \rho gh = \\text{Konstan}$$
                *Penjelasan:* Pada fluida yang mengalir, jika kecepatannya meningkat, maka tekanan fluida tersebut justru akan menurun. Hukum ini menjadi dasar mekanika sayap pesawat dan alat semprot laboratorium.
            """)
            
        with st.expander("3. Hukum Termodinamika & Pemuaian"):
            st.markdown("""
            *   **Hukum Pemuaian Panjang:** 
                $$\Delta L = L_0 \cdot \alpha \cdot \Delta T$$
                *Penjelasan:* Mengindikasikan seberapa besar pertambahan panjang ($\Delta L$) suatu zat padat ketika dipanaskan. Nilainya sangat bergantung pada panjang awal ($L_0$), jenis bahan ($\alpha$), dan perubahan suhu ($\Delta T$).
            *   **Hukum I Termodinamika:** 
                $$\Delta U = Q - W$$
                *Penjelasan:* Bentuk hukum kekekalan energi pada sistem termal. Perubahan energi dalam ($\Delta U$) adalah total kalor ($Q$) yang masuk dikurangi usaha ($W$) yang dikeluarkan sistem ke lingkungan.
            """)
            
        with st.expander("4. Hukum Kelistrikan (Coulomb & Ohm)"):
            st.markdown("""
            *   **Hukum Coulomb:** 
                $$F = k \cdot \\frac{q_1 \cdot q_2}{r^2}$$
                *Penjelasan:* Menjelaskan gaya tarik atau gaya tolak antara dua muatan listrik. Gaya ini makin kuat jika muatannya besar, tetapi berbanding terbalik dengan kuadrat jarak ($r^2$) antar-muatan tersebut.
            *   **Hukum Ohm:** 
                $$V = I \cdot R$$
                *Penjelasan:* Arus listrik ($I$) yang mengalir melewati konduktor akan berbanding lurus dengan tegangan ($V$) yang diberikan, dan berbanding terbalik dengan hambatan ($R$) kawat tersebut.
            """)

    elif sub_menu == "🧮 Kumpulan Rumus Praktis":
        st.subheader("🧮 Cheat Sheet Kumpulan Rumus Fisika")
        
        with st.expander("🌡️ 1. Konversi Suhu & Kalor"):
            st.markdown("""
            *   **Konversi Celcius ke Fahrenheit:** $$T_F = \\left(\\frac{9}{5} \times T_C\\right) + 32$$
            *   **Konversi Celcius ke Kelvin:** $$T_K = T_C + 273.15$$
            *   **Kalor Sensibel (Perubahan Suhu):** $$Q = m \cdot c \cdot \Delta T$$
            *   **Kalor Laten (Perubahan Wujud):** $$Q = m \cdot L$$
            """)
            
        with st.expander("🏃 2. Kinematika Gerak (GLB & GLBB)"):
            st.markdown("""
            *   **Gerak Lurus Beraturan (GLB):** $$s = v \cdot t$$
            *   **Kecepatan Akhir (GLBB):** $$v_t = v_0 + a \cdot t$$
            *   **Jarak Tempuh (GLBB):** $$s = v_0 \cdot t + \\frac{1}{2} a \cdot t^2$$
            *   **Rumus Kuadrat Kecepatan (GLBB):** $$v_t^2 = v_0^2 + 2a \cdot s$$
            """)
            
        with st.expander("🔋 3. Usaha, Energi, & Daya"):
            st.markdown("""
            *   **Usaha (W):** $$W = F \cdot s \cdot \cos(\\theta)$$
            *   **Energi Kinetik ($E_k$):** $$E_k = \\frac{1}{2} m \cdot v^2$$
            *   **Energi Potensial ($E_p$):** $$E_p = m \cdot g \cdot h$$
            *   **Daya Mekanik (P):** $$P = \\frac{W}{t} = F \cdot v$$
            """)
            
        with st.expander("⚡ 4. Rangkaian Listrik Searah (DC)"):
            st.markdown("""
            *   **Hambatan Seri ($R_s$):** $$R_s = R_1 + R_2 + R_3 + \dots$$
            *   **Hambatan Paralel ($R_p$):** $$\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3} + \dots$$
            *   **Daya Listrik (P):** $$P = V \cdot I = I^2 \cdot R = \\frac{V^2}{R}$$
            """)

# ==========================================
# MENU 3: KALKULATOR FISIKA
# ==========================================
elif menu == "Kalkulator Fisika":
    st.title("🧮 Kalkulator Fisika Pintar & Instrumen Lab")
    
    topik = st.selectbox(
        "Pilih Topik Kalkulator:",
        ["Kerapatan & Metode Piknometer", "Mencari Nilai Galat", "Viskositas Relatif (Ostwald Method)", 
         "Cara Baca Jangka Sorong", "Sudut Reposisi", "Koefisien Muai Panjang"]
    )
    
    st.markdown("---")
    
    if topik == "Kerapatan & Metode Piknometer":
        st.subheader("⚙️ Kalkulator Kerapatan (Metode Piknometer & Umum)")
        metode = st.radio("Pilih Metode Input:", ["Input Manual Langsung (m & V)", "Metode Piknometer Eksperimen"])
        
        if metode == "Input Manual Langsung (m & V)":
            sat_massa = st.selectbox("Satuan Massa:", ["Kilogram (kg)", "Gram (g)", "Miligram (mg)"])
            m = st.number_input("Masukkan Massa:", value=1.0, min_value=0.0)
            sat_vol = st.selectbox("Satuan Volume:", ["Meter Kubik (m³)", "Sentimeter Kubik (cm³)", "Mililiter (mL)", "Mikroliter (μL)"])
            v = st.number_input("Masukkan Volume:", value=1.0, min_value=0.000001, format="%.6f")
            
            if st.button("Hitung Kerapatan"):
                m_si = m if sat_massa == "Kilogram (kg)" else (m * 1e-3 if sat_massa == "Gram (g)" else m * 1e-6)
                if sat_vol == "Meter Kubik (m³)": v_si = v
                elif sat_vol == "Sentimeter Kubik (cm³)" or sat_vol == "Mililiter (mL)": v_si = v * 1e-6
                else: v_si = v * 1e-12
                
                rho = m_si / v_si
                rho_g_cm3 = rho / 1000
                st.success(f"**Hasil Akhir:** 𝜌 = {rho:.4f} kg/m³ atau {rho_g_cm3:.4f} g/cm³ (g/mL)")

        elif metode == "Metode Piknometer Eksperimen":
            v_pikno = st.number_input("Volume nominal Piknometer (mL):", value=25.0)
            w0 = st.number_input("Massa Piknometer Kosong + Tutup (gram):", value=20.1500, format="%.4f")
            w1 = st.number_input("Massa Piknometer + Sampel Cairan (gram):", value=42.3400, format="%.4f")
            
            if st.button("Hitung Kerapatan Cairan"):
                m_sampel = w1 - w0
                rho_cairan = m_sampel / v_pikno
                rho_si = rho_cairan * 1000
                st.success(f"**Massa Cairan:** {m_sampel:.4f} gram")
                st.success(f"**Kerapatan Cairan:** {rho_cairan:.4f} g/mL  atau  {rho_si:.2f} kg/m³")

    elif topik == "Mencari Nilai Galat":
        st.subheader("⚙️ Kalkulator Analisis Galat (Error)")
        x_obs = st.number_input("Nilai Observasi:", value=9.82)
        x_ref = st.number_input("Nilai Referensi:", value=10.00)
        if st.button("Hitung Galat"):
            err_abs = abs(x_obs - x_ref)
            err_rel = (err_abs / x_ref) * 100 if x_ref != 0 else 0
            st.info(f"**Galat Mutlak:** {err_abs:.4f}")
            st.success(f"**Galat Relatif:** {err_rel:.2f}%")

    elif topik == "Viskositas Relatif (Ostwald Method)":
        st.subheader("⚙️ Kalkulator Viskositas Metode Perbandingan Ostwald")
        st.markdown("*(Sesuai rumus perbandingan waktu alir & densitas cairan)*")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### **Data Sampel (Misal: Air Sabun)**")
            t_sampel = st.number_input("Waktu Alir Sampel (detik):", value=15.5, format="%.2f")
            rho_sampel = st.number_input("Densitas Sampel (g/mL atau g/cm³):", value=1.0500, format="%.4f")
            
        with col2:
            st.markdown("##### **Data Cairan Referensi (Misal: Air Suling)**")
            t_ref = st.number_input("Waktu Alir Air Suling (detik):", value=10.2, format="%.2f")
            rho_ref = st.number_input("Densitas Air Suling (g/mL atau g/cm³):", value=1.0000, format="%.4f")
            eta_ref = st.number_input("Viskositas Air Suling (cP atau Poise):", value=0.8900, format="%.4f")
            
        if st.button("Hitung Viskositas Sampel"):
            if t_ref > 0 and rho_ref > 0:
                eta_sampel = ((t_sampel * rho_sampel) / (t_ref * rho_ref)) * eta_ref
                st.success(f"**Hasil Viskositas Cairan Sampel:** {eta_sampel:.4f}")
            else:
                st.error("Waktu alir dan densitas referensi harus lebih besar dari 0!")

    elif topik == "Cara Baca Jangka Sorong":
        st.subheader("⚙️ Kalkulator Pembacaan Jangka Sorong")
        su = st.number_input("Skala Utama (cm):", value=2.4, step=0.1)
        sn = st.number_input("Garis Nonius yang sejajar:", value=7, min_value=0)
        ketelitian = st.selectbox("Ketelitian Alat (mm):", [0.1, 0.05, 0.02])
        if st.button("Hitung"):
            nonius_cm = (sn * ketelitian) / 10
            hasil_cm = su + nonius_cm
            st.success(f"**Hasil:** {hasil_cm:.3f} cm  |  {hasil_cm*10:.2f} mm")

    elif topik == "Sudut Reposisi":
        st.subheader("⚙️ Sudut Reposisi Bahan")
        h = st.number_input("Tinggi Kerucut (meter):", value=0.3)
        r = st.number_input("Jari-jari Alas (meter):", value=0.5)
        if st.button("Hitung Sudut"):
            st.success(f"Sudut Reposisi: {math.degrees(math.atan(h/r)):.2f}°")

    elif topik == "Koefisien Muai Panjang":
        st.subheader("⚙️ Pemuaian Termal Panjang")
        l0 = st.number_input("Panjang Mula-mula (m):", value=1.0)
        alpha = st.number_input("Koefisien Muai (α):", value=0.000012, format="%.6f")
        dt = st.number_input("Perubahan Suhu (ΔT dalam °C):", value=50.0)
        if st.button("Hitung Muai"):
            st.success(f"Pertambahan Panjang (ΔL): {l0 * alpha * dt:.6f} m")

# ==========================================
# MENU 4: AUTO UNIT CONVERTER
# ==========================================
elif menu == "Auto Unit Converter":
    st.title("🔄 Auto Unit Converter")
    kategori = st.selectbox("Pilih Kategori Besaran:", ["Panjang (Jarak)", "Massa (Bobot)", "Volume (Ruang)", "Viskositas"])
    nilai = st.number_input("Masukkan Nilai Angka:", value=1.0, format="%.6f")
    
    if kategori == "Panjang (Jarak)":
        dari = st.selectbox("Dari Satuan:", ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Milimeter (mm)", "Mikrometer (μm)", "Nanometer (nm)"])
        ke = st.selectbox("Ke Satuan:", ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Milimeter (mm)", "Mikrometer (μm)", "Nanometer (nm)"])
        faktor = {"Kilometer (km)": 1000.0, "Meter (m)": 1.0, "Centimeter (cm)": 0.01, "Milimeter (mm)": 0.001, "Mikrometer (μm)": 1e-6, "Nanometer (nm)": 1e-9}
        st.success(f"**Hasil:** {nilai * (faktor[dari] / faktor[ke]):.6f} {ke}")
        
    elif kategori == "Massa (Bobot)":
        dari = st.selectbox("Dari Satuan:", ["Ton", "Kilogram (kg)", "Gram (g)", "Miligram (mg)", "Mikrogram (μg)"])
        ke = st.selectbox("Ke Satuan:", ["Ton", "Kilogram (kg)", "Gram (g)", "Miligram (mg)", "Mikrogram (μg)"])
        faktor = {"Ton": 1e6, "Kilogram (kg)": 1000.0, "Gram (g)": 1.0, "Miligram (mg)": 0.001, "Mikrogram (μg)": 1e-6}
        st.success(f"**Hasil:** {nilai * (faktor[dari] / faktor[ke]):.6f} {ke}")

    elif kategori == "Volume (Ruang)":
        dari = st.selectbox("Dari Satuan:", ["Meter Kubik (m³)", "Liter (L)", "Mililiter / cc (mL)", "Mikroliter (μL)"])
        ke = st.selectbox("Ke Satuan:", ["Meter Kubik (m³)", "Liter (L)", "Mililiter / cc (mL)", "Mikroliter (μL)"])
        faktor = {"Meter Kubik (m³)": 1000.0, "Liter (L)": 1.0, "Mililiter / cc (mL)": 0.001, "Mikroliter (μL)": 1e-6}
        st.success(f"**Hasil:** {nilai * (faktor[dari] / faktor[ke]):.6f} {ke}")

    elif kategori == "Viskositas":
        dari = st.selectbox("Dari Satuan:", ["Pascal sekon (Pa·s)", "Poise (P)", "Centipoise (cP)"])
        ke = st.selectbox("Ke Satuan:", ["Pascal sekon (Pa·s)", "Poise (P)", "Centipoise (cP)"])
        faktor = {"Pascal sekon (Pa·s)": 1.0, "Poise (P)": 0.1, "Centipoise (cP)": 0.001}
        st.success(f"**Hasil:** {nilai * (faktor[dari] / faktor[ke]):.6f} {ke}")

# ==========================================
# MENU 5: KUIS FISIKA DASAR (7 SOAL - SAFE STRING)
# ==========================================
elif menu == "Kuis Fisika Dasar":
    st.title("✍️ Kuis Mandiri Fisika (7 Soal)")
    st.markdown("Jawablah seluruh pertanyaan di bawah ini, kemudian klik tombol **Kirim Semua Jawaban** di bagian paling bawah.")
    
    soal_list = 
        {
            "id": 1,
            "pertanyaan": "1. Jika Anda menimbang piknometer seberat 25 gram dalam keadaan kosong, lalu menjadi 50 gram saat diisi penuh cairan bervolume 25 mL, berapakah kerapatan cairan tersebut?",
            "opsi": ["A. 0.5 g/mL", "B. 1.0 g/mL", "C. 2.0 g/mL", "D. 1.5 g/mL"],
            "jawaban": "B. 1.0 g/mL"
        },
        {
            "id": 2,
            "pertanyaan": "2. Berdasarkan metode Ostwald, jika waktu alir sampel dua kali lebih lama dari air suling sedangkan densitas keduanya dianggap sama, maka viskositas sampel adalah...",
            "opsi": ["A. Setengah dari viskositas air suling", "B. Sama dengan viskositas air suling", "C. Dua kali viskositas air suling", "D. Empat kali viskositas air suling"],
            "jawaban": "C. Dua kali viskositas air suling"
        },
        {
            "id": 3,
            "pertanyaan": "3. Sebuah benda mula-mula diam, kemudian diberi gaya total sebesar 20 N. Jika massa benda tersebut adalah 4 kg, berapakah percepatan yang dialami benda?",
            "opsi": ["A. 2 m/s²", "B. 4 m/s²", "C. 5 m/s²", "D. 80 m/s²"],
            "jawaban": "C. 5 m/s²"
        },
        {
            "id": 4,
            "pertanyaan": "4. Satuan viskositas laboratorium yang setara dengan 0.01 Poise (P) dinamakan...",
            "opsi": ["A. Centipoise (cP)", "B. Pascal Sekon (Pa·s)", "C. Milipoise (mP)", "D. KiloPoise (kP)"],
            "jawaban": "A. Centipoise (cP)"
        },
        {
            "id": 5,
            "pertanyaan": "5. Faktor utama yang memengaruhi besarnya pertambahan panjang (ΔL) suatu benda padat saat mengalami pemuaian termal adalah...",
            "opsi": ["A. Panjang awal, koefisien muai panjang, dan perubahan suhu", "B. Kecepatan pemanasan dan volume benda", "C. Tekanan udara sekitar dan bentuk penampang", "D. Kalor jenis dan massa total benda"],
            "jawaban": "A. Panjang awal, koefisien muai panjang, dan perubahan suhu"
        },
        {
            "id": 6,
            "pertanyaan": "6. Hukum Fisika yang menjelaskan bahwa gaya angkat ke atas pada benda di dalam zat cair setara dengan berat zat cair yang dipindahkan adalah...",
            "opsi": ["A. Hukum Bernoulli", "B. Hukum Archimedes", "C. Hukum Stokes", "D. Hukum Pascal"],
            "jawaban": "B. Hukum Archimedes"
        },
        
            "id": 7,
            "pertanyaan": "7. Jika hasil pembacaan Skala Utama jangka sorong adalah 3.1 cm "
                          "dan Garis Nonius yang sejajar berada di angka 4 "
        
