import shelve
import uuid
import requests


class Drive:
    def __init__(self):
        self.data = shelve.open('mydata.dat')

    def upload_data(self, nama=None, link=None):
        if (nama is None):
            return False
        id = str(uuid.uuid4())
        data = dict(id=id, nama=nama, link=link)
        self.data[id] = data
        return True

    def download_data (self, nama=None):
        for i in self.data.keys():
            try:
                if (self.data[i]['nama'].lower() == nama.lower()):
                    return self.data[i]
            except:
                return False

    def list_data(self):
        k = [self.data[i] for i in self.data.keys()]
        return k

if __name__=='__main__':
    d = Drive()
    '''
    d.upload_data("corona1", "https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg")
    d.upload_data("corona2", "https://asset.kompas.com/crops/bJGiSwEVMWMUiX2HRT99U6f7Wvc=/0x0:0x0/740x500/data/photo/2020/03/02/5e5cfb501f54a.jpg")
    print(d.list_data())
    '''
