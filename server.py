from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from model import *

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World! Here is a PUT response"
        self.wfile.write(bytes(message, "utf8"))

    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World! Here is a DELETE response"
        self.wfile.write(bytes(message, "utf8"))

json_string = json.dumps(MainModel.schema_json(indent=2))
with open('json_data.json', 'w') as outfile:
    json.dump(json_string, outfile)

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()
