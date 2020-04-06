# Tugas 5 PROGJAR C Kholishotul Amaliah 05111740000030

## Fitur-fitur program :
1. Log in User
2. Mengirim Pesan
3. Melihat Inbox
4. Melihat Daftar User yang Aktif
5. Keluar dari Program

### Log in User
Pre-conditions : (tidak ada)<br><br>
Sebelum melakukan percakapan, user diminta login sehingga server dapat mengautentikasi user. Mulanya pada database terdapat 3 user, yaitu izza, maya, dan nania.<br>
Untuk log in user, gunakan command <code>auth</code> dan masukkan username serta password user. Sebagai contoh adalah sebagai berikut :<br>
<code>auth {username} {password}</code><br>
Command tersebut kemudian dikirim ke server untuk diproses.<br>
Jika autentikasi berhasil, maka akan muncul pesan bahwa user sudah logged in dan token id-nya. Sebagai contoh adalah sebagai berikut :<br>
<code>username {username} logged in, token {tokenid}</code><br>
Jika autentikasi gagal, maka akan muncul pesan error dan alasan error-nya. Sebagai contoh adalah sebagai berikut :<br>
<code>Error, User tidak ditemukan</code><br>
<code>Error, Password salah</code><br>

### Mengirim Pesan
Pre-conditions :
-	Sudah log in
-	Mengetahui user lain yang aktif

Untuk mengirim pesan, gunakan command <code>send</code> dan masukkan username tujuan serta pesannya. Sebagai contoh adalah sebagai berikut :<br>
<code>send {username} {message}</code><br>
Command tersebut kemudian diproses dan dikirim ke server dengan parameter token ID, username pengirim, username tujuan, dan pesan.<br>
Jika pesan berhasil terkirim, maka akan muncul pesan bahwa pesan terkirim. Sebagai contoh adalah sebagai berikut :<br>
<code>message sent to {username}</code><br>
Jika pesan gagal terkirim, maka akan muncul pesan error dan alasan error-nya. Sebagai contoh adalah sebagai berikut :<br>
<code>Error, Session tidak ditemukan</code><br>
<code>Error, User tidak ditemukan</code>

### Melihat Inbox
Pre-conditions :
-	Sudah log in

Untuk melihat inbox, gunakan command <code>inbox</code>. Sebagai contoh adalah sebagai berikut :<br>
<code>inbox</code><br>
Command tersebut kemudian diproses dan dikirim ke server dengan parameter tokenID.<br>
Jika terdapat pesan yang diterima dari orang lain, maka akan muncul pesan-pesannya. Sebagai contoh adalah sebagai berikut :<br>
<code>{"{username_sender}": [{"msg_from": {name_sender}, "msg_to": {name_receiver}, "msg": {message}}]}</code>

### Melihat Daftar User yang Aktif
Pre-conditions :
-	Sudah log in

Untuk melihat daftar user yang aktif, gunakan command <code>list</code>. Sebagai contoh adalah sebagai berikut :<br>
<code>list</code><br>
Command tersebut kemudian dikirim ke server untuk diproses.<br>
Server kemudian membalas dengan daftar username yang sedang aktif. Sebagai contoh adalah sebagai berikut :<br>
<contoh>

### Log out User
Pre-conditions :
-	Sudah log in

Untuk keluar dari percakapan, gunakan command <code>logout</code>. Sebagai contoh adalah sebagai berikut :<br>
<code>logout</code><br>
Command tersebut kemudian diproses dan dikirim ke server dengan parameter session ID. Session ID tersebut kemudian dihapus dari server maupun client, sehingga user telah keluar dari percakapan.<br>
Server kemudian membalas dengan pesan bahwa user telah ter-log out. Sebagai contoh adalah sebagai berikut :<br>
<contoh>

### Keluar dari Program
Pre-conditions : (tidak ada)<br><br>
Untuk keluar dari program, gunakan command <code>exit</code>. Sebagai contoh adalah sebagai berikut :<br>
<code>exit</code><br>
Command tersebut menjalankan fungsi logout, kemudian memutuskan hubungan socket dengan server. Kemudian user telah keluar dari program.<br>
