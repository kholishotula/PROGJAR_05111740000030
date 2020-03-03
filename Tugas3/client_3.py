import logging
import requests
import os
import threading


def download_gambar(url=None):
    if (url is None):
        return False

    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        # jika path.basename nya sudah mengandung ekstensi, maka tidak perlu menambahkan ekstensi lagi
        # ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}")
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    list_url = ['https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg',
                'https://asset.kompas.com/crops/bJGiSwEVMWMUiX2HRT99U6f7Wvc=/0x0:0x0/740x500/data/photo/2020/03/02/5e5cfb501f54a.jpg',
                'https://asset.kompas.com/crops/8q0sAyP-VaLrzoR7ZMZ7ZluoNiw=/168x0:1844x1117/740x500/data/photo/2020/03/02/5e5cd7a2ad3c6.jpg']
    threads = []
    for i in range(3):
        t = threading.Thread(target=download_gambar(list_url[i]), args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()
