

def build_insert_query(table, columns, values):
    return f"INSERT INTO {table} {columns} VALUES {values};"

def build_multiple_insert_query(table, columns, list_values):
    return ''.join([build_insert_query(table, columns, values) for values in list_values])
