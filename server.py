from typing import ContextManager
from urllib import parse

from http.server import HTTPServer, SimpleHTTPRequestHandler
import mysql.connector 
import json
class crud:
    def __init__(self):
        self.conexion= mysql.connector.connect(user='root', password='admin',
                                           host='localhost' ,database='db_mrHamburger')
        if self.conexion.is_connected():
            print("Conexion exitosa a la base de datos")
        else:
            print("Conexion fallida")
crud=crud()

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
            
        elif self.path == '/menu.html':
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/comentarios.html':
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/carrito.html':
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/registrar.html':
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/index.html':
            return SimpleHTTPRequestHandler.do_GET(self)
           
           
           

    
def do_POST(self):
        if self.path == '':
           Content_Length = int(self.headers['Content-Length'])
           data = self.rfile.read(Content_Length)
           data = data.decode('utf-8')
           data = parse.unquote(data)
           print(data)

print('Servidor iniciado en el puerto 3006')
servidor = HTTPServer(('localhost', 3006), servidorBasico)
servidor.serve_forever()