# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Proyek ini mengangkat sebuah studi kasus mengenai sebuah institusi di bidang pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Intitut ini bernama Jaya jaya yang telah mencetak banyak lulusan dengan reputasi yang sangat baik. Walaupun berhasil mendapat reputasi yang baik, masih terdapat siswa yang tidak dapat menyelesaikan pendidikannya atau bisa dibilang *Dropout*.
Intitusi ini membutuhkan bantuan untuk mengidentifikasi apa penyebab mahasiswanya hingga harus *dropout*. Dengan ditemukannya penyebab masalah tersebut diharapkan dapat diambil keputusan yang cepat dan tepat untuk mengurangi jumlah mahasiswa yang *dropout*

### Permasalahan Bisnis

Institut Jaya Jaya mengalami masalahbesar karena jumlah mahasiswa yang tidak dapat menyelesaikan studinya lumayan tinggi. Kondisi ini dapat berdampak pada reputasi baik institusi ini.

### Cakupan Proyek

Berikut beberapa cakupan proyek ini:

1. Apa saja faktor yang mempengaruhi tingkat *dropout* pada institus jaya Jaya.

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
   `python <nama file>.py`

## Business Dashboard

![Dashboard - Bayun Kurniawan](https://github.com/user-attachments/assets/9c312d41-ffd0-43b7-b9bb-85a50da3e5a1)
Dashboard tersebut menampilkan beberapa fitur yang ada dalam data tersebut mulai dari jumlah keseluruhan mahasiswa, jumlah pemegang beasiswa, sampai asal mulai mahasiswa tersebut.

## Conclusion

Data pada proyek ini memiliki jumlah 4424 data tanpa ada data yang mmemiliki 'missing value".
Datanya berisi 37 fitur dengan rincian:
- 1 data dengan tipe data objek dengan fitur `Status`
- 36 data lainnya dengan tipe data numerik

Selanjutnya dibuat grafik untuk melihat jumlah mahasiswa berdasarkan `Status` nya, didapatkan data sebagai berikut:

| Status    | Jumlah | Persentase (%) |
|-----------|--------|----------------|
| Graduate  | 2209   | 49.93%         |
| Dropout   | 1421   | 32.12%         |
| Enrolled  | 794    | 17.95%         |
| **Total** | **4424** | **100.00%**  |

Berdasakan data di atas dapat dilihat, jumlah mahasiswa yang berstatus *dropout* ada 32,12% dengan jumlah 1421 dari jumlah 4424 siswa. 
Selanjutnya dilakukkan uji korelasi antar fitur numerik dengan 'Status', didapatkan nilai korelasi sebagai berikut:

| No  | Fitur                                           | Korelasi    |
|-----|-------------------------------------------------|-------------|
| 1   | Curricular_units_2nd_sem_approved               | 0.624157    |
| 2   | Curricular_units_2nd_sem_grade                  | 0.566827    |
| 3   | Curricular_units_1st_sem_approved               | 0.529123    |
| 4   | Curricular_units_1st_sem_grade                  | 0.485207    |
| 5   | Tuition_fees_up_to_date                         | 0.409827    |
| 6   | Scholarship_holder                              | 0.297595    |
| 7   | Age_at_enrollment                               | -0.243438   |
| 8   | Debtor                                          | -0.240999   |
| 9   | Gender                                          | -0.229270   |
| 10  | Application_mode                                | -0.221747   |
| 11  | Curricular_units_2nd_sem_enrolled               | 0.175847    |
| 12  | Curricular_units_1st_sem_enrolled               | 0.155974    |
| 13  | Admission_grade                                 | 0.120889    |
| 14  | Displaced                                       | 0.113986    |
| 15  | Previous_qualification_grade                    | 0.103764    |
| 16  | Curricular_units_2nd_sem_without_evaluations    | -0.094028   |
| 17  | Curricular_units_2nd_sem_evaluations            | 0.092721    |
| 18  | Marital_status                                  | -0.089804   |
| 19  | Application_order                               | 0.089791    |
| 20  | Daytime_evening_attendance                      | 0.075107    |
| 21  | Curricular_units_1st_sem_without_evaluations    | -0.068702   |
| 22  | Previous_qualification                          | -0.056039   |
| 23  | Curricular_units_2nd_sem_credited               | 0.054004    |
| 24  | Curricular_units_1st_sem_credited               | 0.048150    |
| 25  | Curricular_units_1st_sem_evaluations            | 0.044362    |
| 26  | GDP                                             | 0.044135    |
| 27  | Mothers_qualification                           | -0.043178   |
| 28  | Course                                          | 0.034219    |
| 29  | Inflation_rate                                  | -0.026874   |
| 30  | Nacionality                                     | -0.014801   |
| 31  | Unemployment_rate                               | 0.008627    |
| 32  | Educational_special_needs                       | -0.007353   |
| 33  | Mothers_occupation                              | -0.005629   |
| 34  | International                                   | 0.003934    |
| 35  | Fathers_occupation                              | -0.001899   |
| 36  | Fathers_qualification                           | -0.001393   |



Dikarenakan nilai pada fitur `status_label` maka bisa disimpulkan nilai dengan korelasi positif cenderung berbanding lurus dengan status `Graduate` yang bernilai 2 dan korelasi negatif cenderung berbanding lurus dengan status `Dropout` yang bernilai 0.

Dari nilai korelasi tersebut ada 4 fitur yang paling berpengaruh terhadap status `Dropout` nya mahasiswa mulai dari `Application_mode`, `Gender`, `Debtor` dan juga `Age_at_Enrollment`. 4 fitur ini dapat dipertimbangkan untuk mencegah terjadinya *dropout* dikemudian hari.

Berikut tampilan streamlit sederhana untuk membantu identifikasi awal mahasiswa dari Institut Jaya jaya 
[streamlit](https://jaya-institut.streamlit.app/)
 
### Rekomendasi Action Items
Berdasarkan pada pengerjaan yang sudah dilakukan, rekomendasi action yang bisa dilakukan oleh Jaya Jaya institut adalah:
1. Membantu pinjaman kepada mahasiswa untuk biaya kuliah atau menambah kuota beasiswa untuk mahasiswa yang membutuhkan
2. Monitoring lebih awal terhadap mahasiswa terutama yang memiliki 4 kriteria di atas 
