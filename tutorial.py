from http.server import  HTTPServer,BaseHTTPRequestHandler
import  time
host = '192.168.1.15'
port = 9999
class Vision_object(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","twxt/html")
        self.end_headers()
        self.wfile.write(bytes(str([402, 504, 6082]), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes(f'\{"time":"{date}"\}', "utf-8"))


server = HTTPServer(('192.168.1.15', 8000), Vision_object)
print("Server now running ...")
server.serve_forever()
server.server_close()
print("Server stoped")