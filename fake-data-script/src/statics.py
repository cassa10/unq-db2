
class Table:
    def __init__(self, name: str, columns: [str]):
        self.name = name
        self.columns = columns

prefix_table = "dbo"

biblioteca_table: Table = Table(f"{prefix_table}.biblioteca", ["nombre", "direccion"])
socio_table: Table = Table(f"{prefix_table}.socio",
                           ["dni", "email", "telefono", "nombre", "apellido", "fechaNacimiento"])
libro_table: Table = Table(f"{prefix_table}.libro", ["nombre", "autores", "valor", "categoria", "id_biblioteca"])

biblioteca_socio_table: Table = Table(f"{prefix_table}.biblioteca_socio", ["id_biblioteca", "id_socio"])
prestamo_table: Table = Table(f"{prefix_table}.prestamo",
                              ["id_libro", "id_socio", "prestadoDesde", "prestadoHasta", "devuelto"])

all_tables: [Table] = [
    biblioteca_table,
    socio_table,
    libro_table,
    biblioteca_socio_table,
    prestamo_table,
]
