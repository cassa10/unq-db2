import argparse
from config import Config
from db_connection import DB
from logger import Logger
from query_builder import build_multiple_insert_query
from fake_data_builder import build_all_fake_data

if __name__ == "__main__":
    cfg = Config(argparse.ArgumentParser())
    logger = Logger(cfg.debug_mode)

    logger.info('Welcome to fake script :D')
    logger.debug(f'server: {cfg.db_server}')

    # get db context
    db = DB(cfg, logger)

    fake_data = build_all_fake_data(5)
    for k, v in fake_data.items():
        logger.debug(f"fake_data[{k}]: {v}")


    # execute query
    insert_query = build_multiple_insert_query(
        'dbo.persons',
        '(firstName, lastName, age)',
        [
            "('Lu3', 'Mordan3', 3)",
            "('Lu4', 'Mordan4', 4)"
        ]
    )
    logger.debug(f'insert_query {insert_query}')
    #db.execute(insert_query)



    logger.debug(db.execute_with_results("SELECT * FROM dbo.persons"))

    db.close_connection()

    logger.info('Script finish')
