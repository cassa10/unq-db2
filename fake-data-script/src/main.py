import argparse
from config import Config
from db import DB
from logger import Logger
from fake_data_builder import (build_all_fake_data, build_all_fake_data_with_fk)


if __name__ == "__main__":
    cfg = Config(argparse.ArgumentParser())
    logger = Logger(cfg.debug_mode)

    logger.info('Welcome to fake script :D')
    logger.debug(f'cfg: {cfg.__dict__}')

    # get db context
    db = DB(cfg, logger)

    size_rows = cfg.generate_fake_rows
    skipInserts = True

    fake_data = build_all_fake_data(size_rows)
    for table, data in fake_data.items():
        db.handle_insert_query(table, data, skipInserts)

    # Get all ids
    fk_ids = db.find_all_ids()

    # Generate data with FK's
    fake_data_with_fk = build_all_fake_data_with_fk(size_rows, fk_ids)
    logger.debug(f"fk_ids: {fk_ids}")

    for table, data in fake_data_with_fk.items():
        db.handle_insert_query(table, data, skipInserts)

    # Select all tables for debug
    if cfg.debug_mode:
        db.find_all()

    db.close_connection()

    logger.info('Script finish')
