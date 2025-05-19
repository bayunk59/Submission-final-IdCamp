# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Proyek ini mengangkat sebuah studi kasus mengenai sebuah institusi di bidang pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Intitut ini bernama Jaya jaya yang telah mencetak banyak lulusan dengan reputasi yang sangat baik. Walaupun berhasil mendapat reputasi yang baik, masih terdapat siswa yang tidak dapat menyelesaikan pendidikannya atau bisa dibilang _Dropout_.
Intitusi ini membutuhkan bantuan untuk mengidentifikasi apa penyebab mahasiswanya hingga harus _dropout_. Dengan ditemukannya penyebab masalah tersebut diharapkan dapat diambil keputusan yang cepat dan tepat untuk mengurangi jumlah mahasiswa yang _dropout_

### Permasalahan Bisnis

Institut Jaya Jaya mengalami masalah besar karena jumlah mahasiswa yang tidak dapat menyelesaikan studinya lumayan tinggi. Kondisi ini dapat berdampak pada reputasi baik institusi ini.

### Cakupan Proyek

Berikut beberapa cakupan proyek ini:

1. Apa saja faktor yang mempengaruhi tingkat _dropout_ pada institus jaya Jaya.

### Persiapan

Sumber data: "[https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv]"

Setup environment:

1. Buat virtual environment
   `python -m venv env`

2. Aktifkan environment
   `env\Scripts\activate`

3. Install semua library dari file `requirement.txt`
   `pip install -r requirements.txt`

4. Jalankan skripnya
   `streamlit run app.py`

## Business Dashboard

![Dashboard - Bayun Kurniawan](https://github.com/user-attachments/assets/b8dc4dfb-698e-4218-9f1a-4a34d2aaecd2)
Dashboard tersebut menampilkan beberapa fitur yang ada dalam data tersebut mulai dari jumlah keseluruhan mahasiswa, jumlah pemegang beasiswa, dan lain sebagainya.

username metabase: user@gmail.com

password metabase: User12345

Selain dashboard, prediksi terkait kecenderungan status mahasiswa dapat juga dilakukan melalui aplikasi streamlit

[Prediksi](https://institut-jaya.streamlit.app/)

## Conclusion

1. Data pada proyek ini memiliki jumlah 4424 data tanpa ada data yang mmemiliki 'missing value".
2. Datanya berisi 37 fitur dengan rincian:

   - 1 data dengan tipe data objek dengan fitur `Status`
   - 36 data lainnya dengan tipe data numerik

3. Jumlah data di setiap Status

| Status    | Jumlah   | Persentase (%) |
| --------- | -------- | -------------- |
| Graduate  | 2209     | 49.93%         |
| Dropout   | 1421     | 32.12%         |
| Enrolled  | 794      | 17.95%         |
| **Total** | **4424** | **100.00%**    |

4. Fitur yang digunakan untuk modelling

| No  | Kolom                                | Tipe Data |
| --- | ------------------------------------ | --------- |
| 1   | Debtor                               | int64     |
| 2   | Tuition_fees_up_to_date              | int64     |
| 3   | Gender                               | int64     |
| 4   | Scholarship_holder                   | int64     |
| 5   | Age_at_enrollment                    | int64     |
| 6   | Curricular_units_1st_sem_enrolled    | int64     |
| 7   | Curricular_units_1st_sem_evaluations | int64     |
| 8   | Curricular_units_1st_sem_approved    | int64     |
| 9   | Curricular_units_1st_sem_grade       | float64   |
| 10  | Curricular_units_2nd_sem_enrolled    | int64     |
| 11  | Curricular_units_2nd_sem_evaluations | int64     |
| 12  | Curricular_units_2nd_sem_approved    | int64     |
| 13  | Curricular_units_2nd_sem_grade       | float64   |
| 14  | Status                               | object    |

5.  Hasil Modellling

    a. Decision Tree = Akurasi 60%

    b. Random Forest = Akurasi 66%

    c. Gradient Boosting = Akurasi 72%

### Rekomendasi Action Items

Berdasarkan pada pengerjaan yang sudah dilakukan, rekomendasi action yang bisa dilakukan oleh Jaya Jaya institut adalah:

1. Membantu pinjaman kepada mahasiswa untuk biaya kuliah atau menambah kuota beasiswa untuk mahasiswa yang membutuhkan.
2. Memberikan mentoring dan bimbingan lebih awal kepada mahasiswa.
3. Monitoring lebih awal terhadap mahasiswa terutama pada 14 fitur yang digunakan pada modelling di atas.
