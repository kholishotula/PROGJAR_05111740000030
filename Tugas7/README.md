# Tugas 7 PROGJAR C Kholishotul Amaliah 05111740000030

## Judul tugas
Performance Test

## Deskripsi tugas
Performance test dilakukan untuk mengetahui seberapa kapasitas dari web server yang kita gunakan untuk melayani request dari client (browser, device dsb). Request dari client datang secara simultan (berbarengan) dan konkuren (datang berbarengan tidak pada saat yang bersamaan). Untuk meningkatkan layanan, kita tidak bisa memproses request satu demi satu , yang berarti satu selesai baru dilanjutkan ke yang lain. Hal ini selain menghambat layanan, juga membuat resource computing kita menjadi IDLE/ menganggur.<br>
Program yang saya gunakan untuk performance test berasal dari Tugas 6.

## Testing
* Menggunakan CLI, ketikkan<br>
```
ab -n <jumlahrequest> -c <concurency> http://127.0.0.1:10001/
```
* Parameter yang diujikan <br>
<table>
<thead>
<td>Nomor</td>
<td>Jumlah request</td>
<td>Konkurensi</td>
</thead>
<tbody>
<tr>
<td>1</td>
<td>10</td>
<td>1, 5, 10</td>
</tr>
<tr>
<td>2</td>
<td>50</td>
<td>1, 10, 30, 50</td>
</tr>
<tr>
<td>3</td>
<td>100</td>
<td>1, 10, 50, 100</td>
</tr>
</tbody>
</table>


## Hasil
Keluaran hasil performance test adalah sebagai berikut :<br>
<table>
<thead>
<td>No test</td>
<td>Concurrency level</td>
<td>Time taken for test</td>
<td>Complete request</td>
<td>Failed request</td>
<td>Total transferred</td>
<td>Request per second</td>
<td>Time per request</td>
<td>Transfer rate</td>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1</td>
<td>0.018 s</td>
<td>10</td>
<td>0</td>
<td>1160 bytes</td>
<td>542.42 [#/sec] (mean)</td>
<td>1.844 [ms] (mean)</td>
<td>61.45 [Kbytes/sec]</td>
</tr>
<tr>
<td>2</td>
<td>5</td>
<td>0.037 s</td>
<td>10</td>
<td>0</td>
<td>1160 bytes</td>
<td>268.52 [#/sec] (mean)</td>
<td></td>
<td>30.42 [Kbytes/sec]</td>
</tr>
<tr>
<td>3</td>
<td>10</td>
<td>0.025 s</td>
<td>10</td>
<td>0</td>
<td>1160 bytes</td>
<td>403.60 [#/sec] (mean)</td>
<td></td>
<td>45.72 [Kbytes/sec]</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>0.445 s</td>
<td>50</td>
<td>0</td>
<td>5800 bytes</td>
<td>112.43 [#/sec] (mean)</td>
<td>8.894 [ms] (mean)</td>
<td>12.74 [Kbytes/sec]</td>
</tr>
<tr>
<td>5</td>
<td>10</td>
<td>0.487 s</td>
<td>50</td>
<td>0</td>
<td>5800 bytes</td>
<td>102.65 [#/sec] (mean)</td>
<td></td>
<td>11.63 [Kbytes/sec]</td>
</tr>
<tr>
<td>6</td>
<td>30</td>
<td>0.668 s</td>
<td>50</td>
<td>0</td>
<td>5800 bytes</td>
<td>74.80 [#/sec] (mean)</td>
<td></td>
<td>8.47 [Kbytes/sec]</td>
</tr>
<tr>
<td>7</td>
<td>50</td>
<td>0.896 s</td>
<td>50</td>
<td>0</td>
<td>5800 bytes</td>
<td>55.81 [#/sec] (mean)</td>
<td></td>
<td>6.32 [Kbytes/sec]</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>0.871 s</td>
<td>100</td>
<td>0</td>
<td>11600 bytes</td>
<td>114.85 [#/sec] (mean)</td>
<td>8.707 [ms] (mean)</td>
<td>13.01 [Kbytes/sec]</td>
</tr>
<tr>
<td>9</td>
<td>10</td>
<td>1.342 s</td>
<td>100</td>
<td>0</td>
<td>11600 bytes</td>
<td>74.53 [#/sec] (mean)</td>
<td></td>
<td>8.44 [Kbytes/sec]</td>
</tr>
<tr>
<td>10</td>
<td>50</td>
<td>2.620 s</td>
<td>100</td>
<td>0</td>
<td>11600 bytes</td>
<td>38.16 [#/sec] (mean)</td>
<td></td>
<td>4.32 [Kbytes/sec]</td>
</tr>
<tr>
<td>11</td>
<td>100</td>
<td>3.529 s</td>
<td>100</td>
<td>0</td>
<td>11600 bytes</td>
<td>28.34 [#/sec] (mean)</td>
<td></td>
<td>3.21 [Kbytes/sec]</td>
</tr>
</tbody>
</table>
