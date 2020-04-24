import os.path
from glob import glob
from datetime import datetime


class HttpServer:
    def __init__(self):
        self.sessions = {}
        self.types = {}
        self.types['.pdf'] = 'application/pdf'
        self.types['.jpg'] = 'image/jpeg'
        self.types['.txt'] = 'text/plain'
        self.types['.html'] = 'text/html'

    def response(self, kode=404, message='Not Found', messagebody='', headers={}):
        tanggal = datetime.now().strftime('%c')
        resp = []
        resp.append("HTTP/1.0 {} {}\r\n".format(kode, message))
        resp.append("Date: {}\r\n".format(tanggal))
        resp.append("Connection: close\r\n")
        resp.append("Server: myserver/1.0\r\n")
        resp.append("Content-Length: {}\r\n".format(len(messagebody)))
        for kk in headers:
            resp.append("{}:{}\r\n".format(kk, headers[kk]))
        resp.append("\r\n")
        resp.append("{}".format(messagebody))
        response_str = ''
        for i in resp:
            response_str = "{}{}".format(response_str, i)
        return response_str

    def proses(self, data):

        requests = data.split("\r\n")

        baris = requests[0]

        all_headers = [n for n in requests[1:] if n != '']

        j = baris.split(" ")
        try:
            method = j[0].upper().strip()
            if (method == 'GET'):
                object_address = j[1].strip()
                return self.http_get(object_address, all_headers)
            if (method == 'POST'):
                object_address = j[1].strip()
                return self.http_post(object_address, all_headers)
            else:
                return self.response(400, 'Bad Request', '', {})
        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address, headers):
        files = glob('./*')
        thedir = '.\\'
        object_address = object_address.split("/")
        if thedir + object_address[1] not in files:
            return self.response(404, 'Not Found', '', {})
        fp = open(thedir + object_address[1], 'r')
        isi = fp.read()

        fext = os.path.splitext(thedir + object_address[1])[1]
        content_type = self.types[fext]

        headers = {}
        headers['Content-type'] = content_type

        return self.response(200, 'OK', isi, headers)

    def http_post(self, object_address, headers):
        data_sent = headers[-1].split("=")

        isi = "<h1>Header</h1>"

        for i in range(len(headers)):
            isi = isi + headers[i] + "<br>"
        isi = isi + "<br><h1>Data yang dikirim</h1>" + data_sent[1]

        headers = {}
        headers['Content-type'] = 'text/html'

        return self.response(200, 'OK', isi, headers)

if __name__ == "__main__":
    httpserver = HttpServer()
    d = httpserver.proses('GET /sending.html HTTP/1.0')
    print(d)
    '''
    d = httpserver.http_get('testing2.txt')
    print(d)
    d = httpserver.http_get('testing.txt')
    print(d)
    '''