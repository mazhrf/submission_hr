# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

PT Jaya Jaya Maju adalah perusahaan berskala internasional yang telah beroperasi lebih dari dua dekade (sejak tahun 2000) dengan tenaga kerja lebih dari 1.000 orang yang tersebar di berbagai lokasi. Meskipun perusahaan telah mencapai pertumbuhan yang menggembirakan dengan cakupan operasi yang luas, saat ini mereka menghadapi masalah serius dalam manajemen SDM, terutama terkait tingkat pengunduran diri karyawan (attrition rate) yang cukup tinggi, yaitu melebihi 10%.

Tingginya angka pengunduran diri ini menimbulkan beberapa konsekuensi negatif, antara lain gangguan pada operasional perusahaan, penurunan produktivitas, serta pembengkakan biaya untuk merekrut dan melatih karyawan pengganti. Untuk mengatasi masalah ini dan mendukung strategi retensi serta pertumbuhan berkelanjutan, PT Jaya Jaya Maju perlu melakukan analisis komprehensif untuk mengidentifikasi faktor-faktor utama yang menyebabkan karyawan memilih meninggalkan perusahaan.

### Permasalahan Bisnis

Divisi Sumber Daya Manusia PT Jaya Jaya Maju saat ini menghadapi beberapa kendala signifikan dalam mengelola tingkat pengunduran diri karyawan, meliputi:
- Kesulitan mengidentifikasi akar masalah pengunduran diri: Departemen HR belum memiliki pemahaman yang jelas mengenai faktor-faktor kunci yang mendorong karyawan memutuskan untuk meninggalkan perusahaan.
- Kurangnya wawasan tentang tren pengunduran diri: Belum tersedianya analisis data yang menunjukkan pola atau karakteristik umum dari karyawan yang cenderung mengundurkan diri.
- Sistem pemantauan yang belum efektif: Ketidakmampuan dalam melakukan pengawasan secara aktif dan tepat waktu terhadap indikator-indikator risiko pengunduran diri karyawan.
- Pengambilan keputusan yang belum berbasis data: Kebijakan dan strategi HR masih banyak yang belum didukung oleh analisis data yang mendalam dan menyeluruh.
- Ketiadaan mekanisme prediksi: Belum adanya model yang dapat memprediksi karyawan dengan risiko tinggi untuk mengundurkan diri, sehingga upaya pencegahan dini tidak dapat dilaksanakan dengan optimal.

### Tujuan Proyek

Untuk menjawab permasalahan bisnis tersebut, proyek ini bertujuan untuk:
- Menemukan faktor-faktor utama penyebab pengunduran diri: Melaksanakan analisis komprehensif terhadap informasi karyawan untuk mengungkap variabel-variabel yang memiliki korelasi kuat dengan tingkat pengunduran diri.
- Mengembangkan sistem prediksi berbasis machine learning: Merancang model klasifikasi dengan teknologi machine learning yang dapat mengestimasi probabilitas pengunduran diri setiap karyawan.
- Menciptakan dashboard pemantauan data : Menghadirkan visualisasi data yang informatif bagi departemen HR untuk memantau tren pengunduran diri secara langsung dengan pendekatan berbasis data.
- Menyediakan analisis mendalam dan saran praktis: Mempresentasikan temuan-temuan kunci dari hasil analisis dan prediksi untuk mendukung pengembangan strategi mempertahankan karyawan yang lebih efektif.

### Cakupan Proyek

### Cakupan Proyek

Proyek ini akan mencakup tahapan-tahapan berikut:

1. **Data Understanding**
   Mengumpulkan dan mempelajari data karyawan yang relevan untuk memahami struktur, sumber, dan potensi permasalahan kualitas data. Tahap ini bertujuan membangun pemahaman komprehensif mengenai konteks data yang akan dianalisis.

2. **Data Preparation**
   Membersihkan data dari nilai hilang (*missing values*), pencilan (*outliers*), dan inkonsistensi.

3. **Exploratory Data Analysis (EDA)**
   Menjalankan analisis statistik deskriptif dan membuat visualisasi untuk mengidentifikasi pola, kecenderungan, dan korelasi antar variabel. Fokus utama tahap ini adalah menemukan faktor-faktor yang berpotensi mempengaruhi *attrition*.

4. **Modelling**
   Memisahkan dataset menjadi data untuk pelatihan dan pengujian. Menyeleksi algoritma yang tepat, melatih model dengan data pelatihan, dan melakukan optimasi parameter bila diperlukan untuk meningkatkan kinerja model.

5. **Evaluasi**
   Menganalisis performa model menggunakan data pengujian dengan berbagai metrik evaluasi seperti akurasi, precision, recall, dan F1-score, untuk menentukan model terbaik dalam memprediksi risiko *attrition*.

6. **Pengembangan Dashboard**
   Merancang dan mengembangkan panel pemantauan interaktif yang memudahkan tim HR untuk mengawasi indikator penting terkait pengunduran diri, mengeksplorasi faktor risiko utama, dan melihat hasil prediksi model secara langsung.

7. **Dokumentasi Laporan dan Rekomendasi**
   Mendokumentasikan seluruh tahapan proyek, dari analisis hingga implementasi. Menyajikan temuan utama dan memberikan saran berbasis data yang dapat diterapkan oleh manajemen untuk mengurangi tingkat *attrition*.

### Persiapan

Sumber data: [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

**1. Run `notebook.ipynb`:**

  * **Instal Dependensi:** Pada terminal proyek, jalankan perintah berikut.
    ```
    pip install -r requirements.txt
    ```

  * **Jalankan Notebook:** Gunakan `jupyter notebook`, `jupyter lab` (lokal) atau unggah ke Google Colab dan jalankan semua sel.

**2. Run `prediction.py`:**

  * **Verifikasi dir. model:** Pastikan path model dan encoder di `prediction.py` sudah benar (Ubah jika perlu).
    ```
    model = joblib.load("model/model.pkl")
    encoder = joblib.load("model/scaler.pkl")
    ```
  
  * **Instal Dependensi (jika library belum terinstall):** 
    ```
    pip install pandas joblib scikit-learn
    ```
  
  * **Jalankan Skrip:** Pada terminal proyek, jalankan 
    ```
    python prediction.py
    ```
    Hasil prediksi akan tampil sebagai output.

**3. Jalankan Dashboard (Looker Studio):**

  * **Link:** Pada website, akses melalui 
    ```
    https://lookerstudio.google.com/reporting/f3232f7a-1bbf-4d98-9977-35c62a178960
    ```

## Business Dashboard

![Dashboard 1](<riri-db1.png>)
![Dashboard 2](<riri-db2.png>)
![Dashboard 3](<riri-db3.png>)
![Dashboard 4](<riri-db4.png>)

Dashboard ini dirancang untuk menampilkan visualisasi yang jelas dan informatif tentang berbagai aspek yang berkontribusi terhadap pengunduran diri karyawan di perusahaan Jaya Jaya Maju, sekaligus menyajikan prediksi mengenai karyawan yang berpotensi meninggalkan perusahaan.



## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
