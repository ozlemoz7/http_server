from http.server import HTTPServer, BaseHTTPRequestHandler  , SimpleHTTPRequestHandler
import argparse

port = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(h('h1', 'Hello World!'))
        return

httpd = HTTPServer(('', port), MyHandler)
print('serving at port', port)
httpd.serve_forever()

# Path: python/http_server/http_server.py