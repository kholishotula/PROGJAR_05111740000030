from Tugas4.drive import Drive
import json
import logging
import requests

'''
PROTOCOL FORMAT
string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...
FITUR
- upload : untuk mengupload file ke database server dan menambah list file
  request : upload
  parameter : nama spasi link
  response : berhasil -> "Upload Completed"
             gagal -> "ERROR"
- list : untuk melihat daftar file
  request: list
  parameter: tidak ada
  response: daftar record file yang ada
- download : untuk mencari file berdasar nama dan mengunduhnya ke lokal
  request: download 
  parameter: nama file yang dicari
  response: file ditemukan -> download -> "Download Completed"
            file tidak ditemukan -> "ERROR"
- exit : untuk keluar dari program
  request : exit
  parameter : tidak ada
  response : client memutuskan hubungan dengan server
- jika command tidak dikenali akan merespon dengan ERRCMD
'''
d = Drive()

class DriveMachine:
    def proses(self, string_to_process):
        global list
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command == 'upload'):
                nama = cstring[1].strip()
                link = cstring[2].strip()

                ff = requests.get(link)
                tipe = dict()
                tipe['image/png'] = 'png'
                tipe['image/jpg'] = 'jpg'
                tipe['image/jpeg'] = 'jpg'
                content_type = ff.headers['Content-Type']
                if (content_type in list(tipe.keys())):
                    ekstensi = tipe[content_type]
                    namafile = nama + "." + ekstensi
                    logging.warning(f"uploading {namafile} to server")
                    fp = open(f"database_server/{namafile}", "wb")
                    fp.write(ff.content)
                    fp.close()
                else:
                    return "Put an image link"

                d.upload_data(namafile, link)
                return "Upload Completed"
            elif (command == 'download'):
                nama = cstring[1].strip()
                hasil = d.download_data(nama)

                if(hasil):
                    fp = open("download/" + nama, "wb")
                    with open("database_server/" + nama, "rb") as ff:
                        buff = ff.read()
                        while buff:
                            fp.write(buff)
                            buff = ff.read()
                    fp.close()
                else:
                    return "Cannot find " + nama + " in database_server"

                logging.warning("downloading" + nama)
                return "Download Completed"
            elif (command == 'list'):
                hasil = d.list_data()
                logging.warning("listing")
                list = ""
                for i in hasil:
                    list = list + json.dumps(i, indent=2) + "\r\n"
                return list
            elif (command == 'exit'):
                return "EXIT"
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    dm = DriveMachine()
    '''
    hasil = dm.proses("list")
    print(hasil)
    hasil = dm.proses("download corona1")
    print(hasil)
    '''