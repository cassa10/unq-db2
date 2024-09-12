import pymssql

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
            print(f"Error: {e}")

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
            print(f"Error: {e}")

    def close_connection(self):
        self.conn.close()
