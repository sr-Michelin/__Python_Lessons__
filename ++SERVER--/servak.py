from http.server import HTTPServer, CGIHTTPRequestHandler
server_addres = ('',8000)
print('server "localhost:8000" is woking...')
httpd = HTTPServer(server_addres,CGIHTTPRequestHandler)
httpd.serve_forever()
