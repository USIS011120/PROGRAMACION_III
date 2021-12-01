import conexion

db = conexion.crud()

class comentarios:
    def consultar_comentario(self):
        sql = "SELECT * FROM comentario"
        return db.consultar(sql)

    def administrar_comentario(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO comentario (texto, img) VALUES (%s, %s)"
                val = (contenido["texto"], contenido["img"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE alumnos SET codigo=%s, nombre=%s, telefono=%s WHERE idAlumno=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["idAlumno"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM alumnos WHERE idAlumno=%s"
                val = (contenido["idAlumno"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)