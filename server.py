from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

import carrito
import comentario

carrito = carrito.carrito()
comentario = comentario.comentarios()

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

        elif self.path == '/consultar-carrito':
            resp = carrito.consultar_carrito()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        elif self.path == '/consultar-comentarios':
            resp = comentario.consultar_comentario()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
            
        
        else:
            return SimpleHTTPRequestHandler.do_GET(self)
           
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        data = parse.unquote(data)
        data = json.loads(data)
        if self.path == '/carrito':
            resp = carrito.administrar_carrito(data)
        elif self.path == '/comentarios':
            resp = comentario.administrar_comentario(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

print('Servidor iniciado en el puerto 3006')
servidor = HTTPServer(('localhost', 3006), servidorBasico)
servidor.serve_forever()