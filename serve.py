#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler
import socketserver
import os

os.chdir("gh-pages")

PORT = 8000

Handler = SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()