import conexion

db = conexion.crud()


class carrito:
    def consultar_carrito(self):
        sql = "SELECT * FROM carrito"
        return db.consultar(sql)

    def administrar_carrito(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO carrito (Imagen, nombre, precio) VALUES (%s, %s, %s)"
                val = (contenido["Imagen"], contenido["nombre"], contenido["precio"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE alumnos SET codigo=%s, nombre=%s, telefono=%s WHERE idAlumno=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["idAlumno"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM alumnos WHERE idAlumno=%s"
                val = (contenido["idAlumno"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)