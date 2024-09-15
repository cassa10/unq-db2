import pymssql

from query_builder import build_multiple_insert_query
from statics import all_tables


class DB:
    def __init__(self, cfg, logger):
        self.logger = logger
        self.conn = self.__handle_connection(cfg)

    def __handle_connection(self, cfg):
        try:
            return pymssql.connect(
                server=cfg.db_server,
                user=cfg.db_user,
                password=cfg.db_pass,
                database=cfg.db_name,
            )
        except Exception as e:
            self.logger.error(f"Error at db connection: {e}")
            raise e

    def execute(self, query):
        try:
            cursor = self.conn.cursor()

            cursor.execute(query)
            self.conn.commit()

        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise e

    def execute_with_results(self, query):
        try:
            cursor = self.conn.cursor()

            cursor.execute(query)

            # Fetch and print the results
            res = []
            for row in cursor.fetchall():
                res.append(row)

            return res

        except Exception as e:
            self.logger.error(f"Error: {e}")
            raise e

    def handle_insert_query(self, table: str, data, skip=False):
        self.logger.debug(f"handle_insert_query - table: {table}")
        self.logger.debug(f"handle_insert_query - data: {data.__dict__}")
        insert_query = build_multiple_insert_query(table, data.columns, data.data)
        self.logger.debug(f'execute with insert_query {insert_query}')
        if not skip:
            self.execute(insert_query)

    def find_all_ids(self, limit=200):
        self.logger.debug(f"find_all_ids with limit: {limit}")
        ids_by_table = {}
        for table in all_tables:
            # TODO: optimize * to only id by table (Add pk in Table object)
            res = self.execute_with_results(f"SELECT TOP ({limit}) * FROM {table.name};")
            ids_by_table[table.name] = [row[0] for row in res]
            self.logger.debug(f"res {table.name}: {res}")
        return ids_by_table

    def find_all(self, limit=300):
        self.logger.debug(f"find_all with limit: {limit}")
        res_by_table = {}
        for table in all_tables:
            res = self.execute_with_results(f"SELECT TOP ({limit}) * FROM {table.name};")
            res_by_table[table.name] = [row for row in res]
            self.logger.debug(f"res {table.name}: {res}")
        return res_by_table

    def count_all(self):
        self.logger.debug(f"count all with tables: {[t.name for t in all_tables]}")
        res_by_table = {}
        for table in all_tables:
            res = self.execute_with_results(f"SELECT COUNT(*) as c FROM {table.name};")
            res_by_table[table.name] = res[0][0]
            self.logger.debug(f"res {table.name}: {res}")
        return res_by_table

    def close_connection(self):
        self.conn.close()
