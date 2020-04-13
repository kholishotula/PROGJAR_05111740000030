from datetime import datetime


class HttpServer:

    def response(self, kode=404, message='Not Found', messagebody=''):
        tanggal = datetime.now().strftime('%c')
        resp = []
        resp.append("HTTP/1.0 {} {}\r\n".format(kode, message))
        resp.append("Date: {}\r\n".format(tanggal))
        resp.append("Connection: close\r\n")
        resp.append("Server: myserver/1.0\r\n")
        resp.append("\r\n")
        resp.append("{}".format(messagebody))
        response_str = ''
        for i in resp:
            response_str = "{}{}".format(response_str, i)
        return response_str

    def proses(self, data):

        requests = data.split("\r\n\r\n")
        baris = requests[0]

        print(baris)
        j = baris.split(" ")
        try:
            method = j[0].upper().strip()
            if (method == 'GET'):
                msg = j[1].strip()
                return self.http_get(msg)
            else:
                return self.response(400, 'Bad Request', '', {})
        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, msg):
        if(msg == '/'):
            isi = '<h1>SERVER HTTP</h1>'
            return self.response(200, 'OK', isi)


if __name__ == "__main__":
    httpserver = HttpServer()
    d = httpserver.proses('GET / HTTP/1.0')
    print(d)
