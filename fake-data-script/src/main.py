import argparse
import time
from config import Config
from db import DB
from logger import Logger
from fake_data_builder import (build_all_fake_data, build_all_fake_data_with_fk_1_level,
                               build_all_fake_data_with_fk_2_level)

if __name__ == "__main__":
    start_time = time.time()
    cfg = Config(argparse.ArgumentParser())
    logger = Logger(cfg.debug_mode)

    logger.info('Welcome to fake script :D')
    logger.debug(f'cfg: {cfg.__dict__}')

    # TODO: Handle exceptions and log error succesfully

    db = DB(cfg, logger)

    size_rows = cfg.generate_fake_rows
    skipInserts = True

    fake_data = build_all_fake_data(size_rows)
    for table_name, data in fake_data.items():
        db.handle_insert_query(table_name, data, skipInserts)

    # TODO: Refactor every fk level to a method

    # Get all ids for level 1
    fk_ids = db.find_all_ids()
    logger.debug(f"fk_ids for level 1: {fk_ids}")

    # Generate data with FK's 1 level
    fake_data_with_fk_1_level = build_all_fake_data_with_fk_1_level(size_rows, fk_ids)

    for table_name, data in fake_data_with_fk_1_level.items():
        db.handle_insert_query(table_name, data, skipInserts)

    # Get all ids for level 2
    fk_ids = db.find_all_ids()
    logger.debug(f"fk_ids for level 2: {fk_ids}")

    # Generate data with FK's 2 level
    fake_data_with_fk_2_level = build_all_fake_data_with_fk_2_level(size_rows, fk_ids)
    for table_name, data in fake_data_with_fk_2_level.items():
        db.handle_insert_query(table_name, data, skipInserts)

    # Select all tables for debug
    if cfg.debug_mode:
        db.find_all()

    db.close_connection()

    logger.info(f'Script finish succesfully - {time.time() - start_time}s -')
