# Tugas4 Progjar 05111740000030


### PROTOCOL FORMAT
string terbagi menjadi 2 bagian, dipisahkan oleh spasi<br>
COMMAND <spasi> PARAMETER <spasi> PARAMETER ...<br>
protokol ini sebatas file berjenis gambar saja<br>

### FITUR
- upload : untuk mengupload file ke database server dan menambah daftar file<br>
  request : upload<br>
  parameter : nama spasi link<br>
  response : berhasil -> "Upload Completed"<br>
             gagal -> "ERROR"<br>
  contoh : upload github http://github.com/fluidicon.png
  
- list : untuk melihat daftar file<br>
  request: list<br>
  parameter: tidak ada<br>
  response: daftar record file yang ada<br>
  contoh : list
  
- download : untuk mencari file berdasar nama dan mengunduhnya ke lokal<br>
  request: download<br>
  parameter: nama file yang dicari<br>
  response: file ditemukan -> download -> "Download Completed"<br>
            file tidak ditemukan -> "ERROR"<br>
  contoh : download github.png
  
- exit : untuk keluar dari program<br>
  request : exit<br>
  parameter : tidak ada<br>
  response : disconnect ke server<br>
  contoh : exit
  
- jika command tidak dikenali akan merespon dengan ERRCMD
