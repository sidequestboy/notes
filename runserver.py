import SimpleHTTPServer, SocketServer
import os

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

os.chdir("_build/html")

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port {}".format(PORT))
httpd.serve_forever()
