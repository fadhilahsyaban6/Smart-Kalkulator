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
st.sidebar.title("⚛️ Smart Fisika V2.1")
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
    serta simulasi perhitungan menggunakan instrumen laboratorium riil seperti **Piknometer** dan **Jangka Sorong**.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📊 **Metrologi & Pikno**\nHitung kerapatan cairan murni atau padatan secara presisi lewat simulasi bobot piknometer.")
    with col2:
        st.success("💧 **Mikro & Fluida**\nKonversi otomatis satuan viskositas dari Poise ke cPoise dan analisis Hukum Stokes.")
    with col3:
        st.warning("📝 **Akurasi Data**\nHitung nilai galat mutlak/relatif untuk memvalidasi tingkat ketelitian hasil pengukuran Anda.")

# ==========================================
# MENU 2: CHEAT SHEET (DENGAN TAMBAHAN RANGKUMAN HUKUM)
# ==========================================
elif menu == "Catatan Rumus & Cheat Sheet":
    st.title("📚 Kumpulan Catatan Rumus & Cheat Sheet")
    
    tab1, tab2, tab3 = st.tabs(["📊 Tabel Satuan Eksperimen", "🌌 Konstanta Fisika Penting", "📜 Rangkuman Hukum Fisika"])
    
    with tab1:
        st.subheader("Satuan Konvensional vs Satuan Mikro Laboratorium")
        data_satuan = {
            "Besaran": ["Panjang (Gelombang/Partikel)", "Massa (Analitis)", "Volume (Mikro)", "Viskositas", "Kerapatan"],
            "Satuan Standar SI": ["Meter (m)", "Kilogram (kg)", "Meter Kubik (m³)", "Pascal sekon (Pa·s)", "kg/m³"],
            "Satuan Sering di Lab": ["Milimeter (mm) / Mikrometer (μm)", "Gram (g) / Miligram (mg)", "Mililiter (mL) / Mikroliter (μL)", "Poise (P) / Centipoise (cP)", "g/cm³ atau g/mL"]
        }
        st.table(pd.DataFrame(data_satuan))
        
    with tab2:
        st.subheader("Konstanta Fisika & Faktor Pengali")
        st.write("- **Percepatan Gravitasi (g):** $9.8\\text{ m/s}^2$ atau $980\\text{ cm/s}^2$")
        st.write("- **Kecepatan Cahaya (c):** $3 \\times 10^8\\text{ m/s}$")
        st.write("- **Kerapatan Air Murni ($4^\\circ\\text{C}$):** $1.000\\text{ g/cm}^3$ atau $1000\\text{ kg/m}^3$")

    with tab3:
        st.subheader("📜 Rangkuman Hukum Utama dalam Fisika Dasar")
        st.caption("Gunakan ekspander di bawah untuk mempelajari bunyi dan persamaan dasar dari hukum-hukum fisika.")
        
        with st.expander("1. Hukum Newton (Mekanika)"):
            st.markdown("""
            *   **Hukum I Newton (Inersia):** Jika gaya total yang bekerja pada benda sama dengan nol, benda diam akan tetap diam dan benda bergerak akan tetap bergerak dengan kecepatan konstan. 
                $$\Sigma F = 0$$
            *   **Hukum II Newton:** Percepatan sebuah benda berbanding lurus dengan gaya total yang bekerja padanya dan berbanding terbalik dengan massanya.
                $$F = m \cdot a$$
            *   **Hukum III Newton (Aksi-Reaksi):** Untuk setiap aksi, selalu ada reaksi yang sama besar namun berlawanan arah.
                $$F_{\\text{aksi}} = -F_{\\text{reaksi}}$$
            """)
            
        with st.expander("2. Hukum Fluida (Stokes & Archimedes)"):
            st.markdown("""
            *   **Hukum Stokes:** Mengukur gaya hambat (gaya gesek) yang dialami oleh benda berbentuk bola yang jatuh bebas di dalam fluida kental.
                $$F_s = 6 \pi \eta r v$$
            *   **Hukum Archimedes:** Benda yang dicelupkan sebagian atau seluruhnya ke dalam fluida akan mengalami gaya ke atas yang besarnya sama dengan berat fluida yang dipindahkan.
                $$F_a = \rho_f \cdot g \cdot V_{\\text{tercelup}}$$
            *   **Hukum Bernoulli:** Peningkatan kecepatan pada fluida akan terjadi bersamaan dengan penurunan tekanan atau penurunan energi potensial fluida tersebut.
                $$P + \\frac{1}{2}\rho v^2 + \rho gh = \\text{Konstan}$$
            """)
            
        with st.expander("3. Hukum Termodinamika & Pemuaian"):
            st.markdown("""
            *   **Hukum Pemuaian Panjang:** Pertambahan panjang benda padat berbanding lurus dengan panjang awal, koefisien muai panjang, dan perubahan suhu.
                $$\Delta L = L_0 \cdot \alpha \cdot \Delta T$$
            *   **Hukum I Termodinamika (Kekekalan Energi):** Perubahan energi dalam sistem sama dengan kalor yang ditambahkan ke sistem dikurangi usaha yang dilakukan oleh sistem.
                $$\Delta U = Q - W$$
            """)
            
        with st.expander("4. Hukum Kelistrikan (Coulomb & Ohm)"):
            st.markdown("""
            *   **Hukum Coulomb:** Gaya tarik-menarik atau tolak-menolak antara dua muatan listrik sebanding dengan perkalian kedua muatan dan berbanding terbalik dengan kuadrat jaraknya.
                $$F = k \cdot \\frac{q_1 \cdot q_2}{r^2}$$
            *   **Hukum Ohm:** Kuat arus yang mengalir pada suatu penghantar sebanding dengan beda potensial (tegangan) antara ujung-ujung penghantar tersebut.
                $$V = I \cdot R$$
            """)

# ==========================================
# MENU 3: KALKULATOR FISIKA
# ==========================================
elif menu == "Kalkulator Fisika":
    st.title("🧮 Kalkulator Fisika Pintar & Instrumen Lab")
    
    topik = st.selectbox(
        "Pilih Topik Kalkulator:",
        ["Kerapatan & Metode Piknometer", "Mencari Nilai Galat", "Viskositas (Hukum Stokes)", 
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
                st.markdown("**Langkah Pengerjaan:**")
                st.code(f"1. Konversi data ke SI: m = {m_si} kg, V = {v_si} m³\n2. Gunakan rumus 𝜌 = m / V\n3. 𝜌 = {m_si} / {v_si}\n4. Hasil = {rho:.4f} kg/m³")

        elif metode == "Metode Piknometer Eksperimen":
            st.write("Menghitung kerapatan cairan menggunakan bobot piknometer kosong dan isi.")
            v_pikno = st.number_input("Volume nominal Piknometer (mL):", value=25.0)
            w0 = st.number_input("Massa Piknometer Kosong + Tutup (gram):", value=20.1500, format="%.4f")
            w1 = st.number_input("Massa Piknometer + Sampel Cairan (gram):", value=42.3400, format="%.4f")
            
            if st.button("Hitung Kerapatan Cairan"):
                m_sampel = w1 - w0
                rho_cairan = m_sampel / v_pikno
                rho_si = rho_cairan * 1000
                
                st.success(f"**Massa Cairan:** {m_sampel:.4f} gram")
                st.success(f"**Kerapatan Cairan:** {rho_cairan:.4f} g/mL  atau  {rho_si:.2f} kg/m³")
                st.markdown("**Langkah Pengerjaan Lab:**")
                st.code(f"1. Cari massa cairan (m) = W1 - W0 = {w1}g - {w0}g = {m_sampel:.4f} gram\n"
                        f"2. Hitung kerapatan (𝜌) = massa / Volume Pikno = {m_sampel:.4f} / {v_pikno} mL\n"
                        f"3. Hasil = {rho_cairan:.4f} g/mL")

    elif topik == "Mencari Nilai Galat":
        st.subheader("⚙️ Kalkulator Analisis Galat (Error)")
        x_obs = st.number_input("Nilai Observasi (Hasil Praktikum/Ukur):", value=9.82)
        x_ref = st.number_input("Nilai Referensi (Teoretis/Ketetapan):", value=10.00)
        
        if st.button("Hitung Galat"):
            err_abs = abs(x_obs - x_ref)
            err_rel = (err_abs / x_ref) * 100 if x_ref != 0 else 0
            
            st.info(f"**Galat Mutlak (Absolut):** {err_abs:.4f}")
            st.success(f"**Galat Relatif (Persen Kesalahan):** {err_rel:.2f}%")

    elif topik == "Viskositas (Hukum Stokes)":
        st.subheader("⚙️ Kalkulator Viskositas Fluida (𝜂)")
        st.write("Dilengkapi konversi otomatis satuan ketukan mikro/mili.")
        
        r_unit = st.selectbox("Satuan Jari-jari:", ["Meter (m)", "Sentimeter (cm)", "Milimeter (mm)"])
        r_val = st.number_input("Masukkan Nilai Jari-jari bola (r):", value=2.0, format="%.4f")
        
        rho_b = st.number_input("Kerapatan Bola (𝜌b) dalam kg/m³:", value=7800.0)
        rho_f = st.number_input("Kerapatan Fluida (𝜌f) dalam kg/m³:", value=1260.0)
        v_terminal = st.number_input("Kecepatan Terminal (v) dalam m/s:", value=0.5)
        
        if st.button("Hitung Viskositas"):
            r = r_val if r_unit == "Meter (m)" else (r_val * 0.01 if r_unit == "Sentimeter (cm)" else r_val * 0.001)
            g = 9.8
            
            eta = (2 * (r**2) * g * (rho_b - rho_f)) / (9 * v_terminal)
            eta_poise = eta * 10
            eta_cp = eta * 1000
            
            st.success(f"**Hasil Akhir (SI):** 𝜂 = {eta:.4f} Pa·s (atau N·s/m²)")
            st.info(f"**Satuan Alternatif Lab:** {eta_poise:.2f} Poise (P)  |  {eta_cp:.2f} Centipoise (cP)")

    elif topik == "Cara Baca Jangka Sorong":
        st.subheader("⚙️ Kalkulator Pembacaan Jangka Sorong")
        su = st.number_input("Skala Utama (cm):", value=2.4, step=0.1)
        sn = st.number_input("Garis Nonius yang sejajar:", value=7, min_value=0)
        ketelitian = st.selectbox("Ketelitian Alat (mm):", [0.1, 0.05, 0.02])
        
        if st.button("Hitung"):
            nonius_cm = (sn * ketelitian) / 10
            hasil_cm = su + nonius_cm
            hasil_mm = hasil_cm * 10
            hasil_um = hasil_mm * 1000
            
            st.success(f"**Hasil:** {hasil_cm:.3f} cm  |  {hasil_mm:.2f} mm  |  {hasil_um:.0f} μm (Mikrometer)")

    elif topik == "Sudut Reposisi":
        st.subheader("⚙️ Sudut Reposisi Bahan")
        h = st.number_input("Tinggi Kerucut (meter):", value=0.3)
        r = st.number_input("Jari-jari Alas (meter):", value=0.5)
        if st.button("Hitung Sudut"):
            tan_th = h / r
            th_deg = math.degrees(math.atan(tan_th))
            st.success(f"Sudut Reposisi: {th_deg:.2f}°")

    elif topik == "Koefisien Muai Panjang":
        st.subheader("⚙️ Pemuaian Termal Panjang")
        l0 = st.number_input("Panjang Mula-mula (m):", value=1.0)
        alpha = st.number_input("Koefisien Muai (α) [1/°C]:", value=0.000012, format="%.6f")
        dt = st.number_input("Perubahan Suhu (ΔT dalam °C):", value=50.0)
        
        if st.button("Hitung Muai"):
            dl = l0 * alpha * dt
            st.success(f"Pertambahan Panjang (ΔL): {dl:.6f} m  ({dl*1000:.4f} mm)")

# ==========================================
# MENU 4: AUTO UNIT CONVERTER
# ==========================================
elif menu == "Auto Unit Converter":
    st.title("🔄 Auto Unit Converter (Tingkat Mikro & Makro)")
    st.write("Sistem konversi mencakup jangkauan skala laboratorium dari Nano hingga Kilo.")
    
    kategori = st.selectbox("Pilih Kategori Besaran:", ["Panjang (Jarak)", "Massa (Bobot)", "Volume (Ruang)", "Viskositas"])
    nilai = st.number_input("Masukkan Nilai Angka:", value=1.0, format="%.6f")
    
    if kategori == "Panjang (Jarak)":
        dari = st.selectbox("Dari Satuan:", ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Milimeter (mm)", "Mikrometer (μm)", "Nanometer (nm)"])
        ke = st.selectbox("Ke Satuan:", ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Milimeter (mm)", "Mikrometer (μm)", "Nanometer (nm)"])
        
        faktor = {"Kilometer (km)": 1000.0, "Meter (m)": 1.0, "Centimeter (cm)": 0.01, "Milimeter (mm)": 0.001, "Mikrometer (μm)": 1e-6, "Nanometer (nm)": 1e-9}
        hasil = nilai * (faktor[dari] / faktor[ke])
        st.success(f"**Hasil Konversi Jarak:** {nilai} {dari} = {hasil:.6f} {ke}")
        
    elif kategori == "Massa (Bobot)":
        dari = st.selectbox("Dari Satuan:", ["Ton", "Kilogram (kg)", "Gram (g)", "Miligram (mg)", "Mikrogram (μg)"])
        ke = st.selectbox("Ke Satuan:", ["Ton", "Kilogram (kg)", "Gram (g)", "Miligram (mg)", "Mikrogram (μg)"])
        
        faktor = {"Ton": 1e6, "Kilogram (kg)": 1000.0, "Gram (g)": 1.0, "Miligram (mg)": 0.001, "Mikrogram (μg)": 1e-6}
        hasil = nilai * (faktor[dari] / faktor[ke])
        st.success(f"**Hasil Konversi Massa:** {nilai} {dari} = {hasil:.6f} {ke}")

    elif kategori == "Volume (Ruang)":
        dari = st.selectbox("Dari Satuan:", ["Meter Kubik (m³)", "Liter (L)", "Mililiter / cc (mL)", "Mikroliter (μL)"])
        ke = st.selectbox("Ke Satuan:", ["Meter Kubik (m³)", "Liter (L)", "Mililiter / cc (mL)", "Mikroliter (μL)"])
        
        faktor = {"Meter Kubik (m³)": 1000.0, "Liter (L)": 1.0, "Mililiter / cc (mL)": 0.001, "Mikroliter (μL)": 1e-6}
        hasil = nilai * (faktor[dari] / faktor[ke])
        st.success(f"**Hasil Konversi Volume:** {nilai} {dari} = {hasil:.6f} {ke}")

    elif kategori == "Viskositas":
        dari = st.selectbox("Dari Satuan:", ["Pascal sekon (Pa·s)", "Poise (P)", "Centipoise (cP)"])
        ke = st.selectbox("Ke Satuan:", ["Pascal sekon (Pa·s)", "Poise (P)", "Centipoise (cP)"])
        
        faktor = {"Pascal sekon (Pa·s)": 1.0, "Poise (P)": 0.1, "Centipoise (cP)": 0.001}
        hasil = nilai * (faktor[dari] / faktor[ke])
        st.success(f"**Hasil Konversi Viskositas:** {nilai} {dari} = {hasil:.6f} {ke}")

# ==========================================
# MENU 5: KUIS FISIKA DASAR
# ==========================================
elif menu == "Kuis Fisika Dasar":
    st.title("✍️ Kuis Mandiri Fisika (Tingkat Kuliah Dasar)")
    
    soal_list = [
        {
            "tipe": "PG",
            "pertanyaan": "Jika Anda menimbang piknometer seberat 25 gram dalam keadaan kosong, lalu menjadi 50 gram saat diisi penuh cairan bervolume 25 mL, berapakah kerapatan cairan tersebut?",
            "opsi": ["A. 0.5 g/mL", "B. 1.0 g/mL", "C. 2.0 g/mL", "D. 1.5 g/mL"],
            "jawaban": "B. 1.0 g/mL",
            "pembahasan": "Massa cairan = 50g - 25g = 25 gram. Kerapatan = massa / volume = 25g / 25mL = 1.0 g/mL (Kerapatan air)."
        },
        {
            "tipe": "PG",
            "pertanyaan": "Faktor pengali konversi satuan dari Centipoise (cP) menuju satuan dasar Pascal sekon (Pa·s) yang benar adalah...",
            "opsi": ["A. Dikali 1000", "B. Dikali 10", "C. Dibagi 1000", "D. Dibagi 10"],
            "jawaban": "C. Dibagi 1000",
            "pembahasan": "1 Pa·s sama dengan 10 Poise atau setara dengan 1000 Centipoise (cP). Sehingga dari cP ke Pa·s harus dibagi 1000."
        }
    ]
    
    skor = 0
    with st.form("kuis_v2"):
        user_ans = {}
        for i, q in enumerate(soal_list):
            st.markdown(f"**Soal {i+1}: {q['pertanyaan']}**")
            user_ans[i] = st.radio(f"Pilih Jawaban Soal {i+1}:", q["opsi"], key=f"q_{i}")
            st.markdown("---")
            
        submit = st.form_submit_button("Kirim & Evaluasi Jawaban")
        
    if submit:
        st.subheader("📊 Pembahasan Hasil")
        for i, q in enumerate(soal_list):
            if user_ans[i] == q["jawaban"]:
                st.success(f"✅ **Soal {i+1}: BENAR**")
                skor += 1
            else:
                st.error(f"❌ **Soal {i+1}: SALAH**")
            st.caption(f"💡 *Pembahasan:* {q['pembahasan']}")
            
        st.balloons()
        st.metric(label="Total Skor", value=f"{skor} / {len(soal_list)}")
