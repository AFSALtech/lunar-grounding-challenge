import http.server
import socketserver
import os

PORT = 20140
DIRECTORY = "/home/afsal/lunar-grounding-challenge/deliverables"

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    # Kill existing port if any
    os.system(f"fuser -k {PORT}/tcp >/dev/null 2>&1")
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print(f"Serving {DIRECTORY} with CORS on port {PORT}")
        httpd.serve_forever()
