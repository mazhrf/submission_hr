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

**Komponen Utama Dashboard:**

1.  **Metriks Awal:**
    * **879 Total Karyawan yang Masih Bekerja:** Jumlah karyawan yang aktif bekerja.
    * **179 Total Karyawan yang Keluar:** Jumlah karyawan yang telah meninggalkan perusahaan.
    * **856.496 Tarif Operasional Harian:** Jumlah pengeluaran harian perusahaan untuk Operasional.
    * **15.094.784 Tarif Operasional Bulanan:** Jumlah pengeluaran harian perusahaan untuk Operasional.

2.  **Faktor-Faktor Penyebab Karyawan Keluar:**
    * Menampilkan 10 fitur atau faktor teratas yang paling berpengaruh terhadap keputusan karyawan untuk keluar. Berdasarkan visualisasi ini, **MonthlyIncome** (Gaji Bulanan) menjadi faktor yang paling signifikan, diikuti oleh **Age** (Usia) dan **TotalWorkingYears** (Total Tahun Bekerja).

3.  **Penyajian Data Berbagai Faktor:**
    * **Distribusi Gender Karyawan:** Membandingkan jumlah karyawan berdasarkan jenis kelamin.
    * **Distribusi Departmnent Karyawan:** Membandingkan jumlah karyawan berdasarkan departemen.
    * **Distribusi Marital Karyawan:** Membandingkan jumlah karyawan berdasarkan status.
    * **Distribusi Education Karyawan:** Menunjukkan distribusi tingkat pendidikan terakhir yang ditempuh karyawan.
    * **Distribusi EducationField Karyawan:** Menunjukkan distribusi bidang pendidikan terakhir yang ditempuh karyawan.
    * **Distribusi YearsAtCompany Karyawan:** Menunjukkan distribusi lama bekerja karyawan. 
    * **Distribusi TotalWorkingYears Karyawan:** Menunjukkan distribusi pengabdian/tahun kerja karyawan. 
    * **Distribusi Age Karyawan:** Menunjukkan distribusi usia karyawan.
    * **Distribusi PerfomanceRating Karyawan:** Membandingkan jumlah karyawan berdasarkan performa.
    * **Distribusi JobLevel Karyawan:** Membandingkan jumlah karyawan berdasarkan tingkatan pekerjaan.
    * **Distribusi OverTime Karyawan:** Membandingkan jumlah karyawan berdasarkan jam lembur.
    * **Distribusi DistanceFromHome Karyawan:** Menunjukkan distribusi jarak antar rumah  dan tempat kerja tiap karyawan.
    * **Distribusi WorkLifeBalance Karyawan:** Membandingkan jumlah karyawan berdasarkan kualitas hidup.
    * **Distribusi JobInvolvement Karyawan:** Membandingkan jumlah karyawan berdasarkan kontribusi pada pekerjaan.
    * **Distribusi PercentSalaryHike Karyawan:** Menunjukkan distribusi jarak kemungkinan naik gaji karyawan.
    * **Distribusi RelationshipSatisfaction Karyawan:** Menunjukkan distribusi kepuasan terhadap hubungan antar karyawan.
    * **Distribusi EnvironmentSatisfaction Karyawan:** Menunjukkan distribusi kepuasan lingkungan kerja karyawan.

## Conclusion

Proyek ini difokuskan untuk mengenali penyebab utama tingginya angka attrition karyawan di Jaya Jaya Maju dan menyediakan dashboard interaktif sebagai alat bantu visualisasi serta prediksi karyawan yang berisiko keluar.

Dari hasil analisis data dan model Random Forest, ditemukan bahwa **Gaji Bulanan**, **Usia**, dan **Total Pengalaman Kerja** adalah faktor paling menentukan. Selain itu, **lembur dan lama bekerja di perusahaan** juga berkontribusi signifikan terhadap keputusan seorang karyawan untuk meninggalkan pekerjaannya.

Model prediksi menunjukkan kinerja yang sangat baik dengan akurasi 93,32% serta metrik evaluasi lainnya seperti precision, recall, dan f1-score yang tinggi, menandakan bahwa model mampu membedakan dengan akurat antara karyawan yang bertahan dan yang keluar.

*Dashboard* yang dikembangkan menampilkan data secara visual, memudahkan HR dalam melihat tren dan pola *attrition* berdasarkan berbagai aspek, serta mengidentifikasi karyawan dengan risiko tinggi secara real-time.

### Rekomendasi Action Items (Optional)

Berdasarkan hasil temuan, berikut beberapa langkah *strategis* yang disarankan untuk Jaya Jaya Maju:

* **Evaluasi Skema Gaji:** Karena kompensasi menjadi faktor utama attrition, penting untuk mengevaluasi ulang struktur gaji dan memastikan daya saing di pasar tenaga kerja, terutama untuk posisi yang rawan *turnover*.
* **Program Engagement Karyawan Berdasarkan Usia dan Masa Kerja:** Mengembangkan program engagement yang ditargetkan untuk kelompok usia dan masa kerja tertentu yang menunjukkan tingkat *attrition* lebih tinggi. Misalnya, program pengembangan karir untuk karyawan muda atau program apresiasi untuk karyawan dengan masa kerja lebih pendek.
* **Atur Kebijakan Lembur Secara Bijak:** Perusahaan perlu memastikan beban kerja tidak berlebihan. Jika lembur tidak bisa dihindari, sediakan kompensasi atau fleksibilitas kerja sebagai bentuk apresiasi.
* **Analisis Faktor Tambahan:** Faktor seperti **Job Involvement**, **Job Level**, dan **Business Travel** juga berpengaruh dan perlu dianalisis lebih lanjut untuk memahami konteks spesifik yang memicu *attrition*.
* **Lakukan Pendekatan pada Karyawan Berisiko Tinggi:** Gunakan hasil prediksi model untuk melakukan intervensi personal, seperti diskusi satu-satu atau penawaran insentif agar mereka merasa dihargai dan tetap bertahan.
