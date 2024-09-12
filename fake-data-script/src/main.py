import argparse
from config import Config
from db_connection import DB
from logger import Logger
from query_builder import build_multiple_insert_query
from fake_data_builder import build_all_fake_data
from fake_data_builder import FakeData


def handle_insert_query(logger, db, table, data: FakeData):
    logger.debug(f"handle_insert_query - table: {table}")
    logger.debug(f"handle_insert_query - data: {data.__dict__}")
    insert_query = build_multiple_insert_query(
        table,
        data.columns,
        data.data
    )
    logger.debug(f'execute with insert_query {insert_query}')
    db.execute(insert_query)


if __name__ == "__main__":
    cfg = Config(argparse.ArgumentParser())
    logger = Logger(cfg.debug_mode)

    logger.info('Welcome to fake script :D')
    logger.debug(f'cfg: {cfg.__dict__}')

    # get db context
    db = DB(cfg, logger)

    fake_data = build_all_fake_data(cfg.generate_fake_rows)
    for table, data in fake_data.items():
        handle_insert_query(logger, db, table, data)

    # Get all table data
    limit = 200
    for table in fake_data.keys():
        res = db.execute_with_results(f"SELECT TOP ({limit}) * FROM {table};")
        logger.debug(f"res {table}: {res}")

    db.close_connection()

    logger.info('Script finish')
