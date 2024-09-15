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

    # TODO: Handle exceptions and log error successfully

    db = DB(cfg, logger)

    # Log all data exist in db previous execute script
    logger.info(f"previous script - count all tables {db.count_all()}")


    size_rows = cfg.generate_fake_rows
    skipInserts = False

    fake_data = build_all_fake_data(size_rows)
    for table_name, data in fake_data.items():
        db.handle_insert_query(table_name, data, skipInserts)

    logger.info(f"success create fake_data with size_rows: {size_rows}")
    # TODO: Refactor every fk level to a method and use some data struct to iterate (List of list)

    # Get all ids for level 1
    fk_ids = db.find_all_ids()
    logger.debug(f"fk_ids for level 1: {fk_ids}")

    # Generate data with FK's 1 level
    fake_data_with_fk_1_level = build_all_fake_data_with_fk_1_level(size_rows, fk_ids)

    for table_name, data in fake_data_with_fk_1_level.items():
        db.handle_insert_query(table_name, data, skipInserts)

    logger.info(f"success create fake_data_with_fk_1_level with size_rows: {size_rows}")

    # Get all ids for level 2
    fk_ids = db.find_all_ids()
    logger.debug(f"fk_ids for level 2: {fk_ids}")

    # Generate data with FK's 2 level
    fake_data_with_fk_2_level = build_all_fake_data_with_fk_2_level(size_rows, fk_ids)
    for table_name, data in fake_data_with_fk_2_level.items():
        db.handle_insert_query(table_name, data, skipInserts)

    logger.info(f"success create fake_data_with_fk_2_level with size_rows: {size_rows}")

    # Log all data exist in db as result of script
    logger.info(f"after script executed - count all tables {db.count_all()}")

    db.close_connection()

    logger.info(f'Script finish succesfully at {time.time() - start_time}s')
