#Tugas 4 Progjar 05111740000030

PROTOCOL FORMAT
string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...
protokol ini sebatas file berjenis gambar saja

FITUR
- upload : untuk mengupload file ke database server dan menambah daftar file
  request : upload
  parameter : nama spasi link
  response : berhasil -> "Upload Completed"
             gagal -> "ERROR"           
  contoh : upload github http://github.com/fluidicon.png
  
- list : untuk melihat daftar file
  request: list
  parameter: tidak ada
  response: daftar record file yang ada
  contoh : list
  
- download : untuk mencari file berdasar nama dan mengunduhnya ke lokal
  request: download 
  parameter: nama file yang dicari
  response: file ditemukan -> download -> "Download Completed"
            file tidak ditemukan -> "ERROR"
  contoh : download github.png
  
- exit : untuk keluar dari program
  request : exit
  parameter : tidak ada
  response : disconnect ke server
  contoh : exit
  
- jika command tidak dikenali akan merespon dengan ERRCMD
