from logger import Logger

def get_or_default(atr, default):
    atr_striped = atr.strip() if issubclass(type(atr), str) else atr
    if atr_striped in (None, ''):
        return default
    return atr


class Config:

    def __init__(self, arg_parser):
        logger = Logger(False)

        self.arg_parser = arg_parser

        args = self.load()

        self.debug_mode = args.debug

        self.db_server = get_or_default(args.dbServer, 'localhost:1433')
        self.db_name = get_or_default(args.dbName, 'test')
        self.db_user = get_or_default(args.user, 'sa')
        self.db_pass = get_or_default(args.password, '')

        generate_fake_rows_raw = get_or_default(args.generateFakeRows, '5')
        try:
            self.generate_fake_rows = int(generate_fake_rows_raw)
        except Exception as e:
            self.generate_fake_rows = 5
            logger.error(f"error when load generate_fake_rows: {e}, using default value {self.generate_fake_rows}")

    def load(self):
        self.arg_parser.add_argument("-u", "--user", help="database credential user (default: 'sa')")
        self.arg_parser.add_argument("-p", "--password", help="database credential password")
        self.arg_parser.add_argument("-s", "--dbServer", help="database server with port (default: 'localhost:1433')")
        self.arg_parser.add_argument("-n", "--dbName", help="database name (default: 'test')")

        self.arg_parser.add_argument("-g", "--generateFakeRows", help="generate fake rows (default: 5)")

        # Debug
        self.arg_parser.add_argument("-d", "--debug", action='store_true',
                                     help="Mode debug for watch program input and some debugging info (default: False)")
        return self.arg_parser.parse_args()
