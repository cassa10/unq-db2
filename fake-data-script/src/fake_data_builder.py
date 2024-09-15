from collections.abc import Callable
from typing import Dict, List
from datetime import datetime
from faker import Faker
from random import randrange, choice, choices

from query_builder import buildColumnStr
from statics import biblioteca_table, socio_table, libro_table, biblioteca_socio_table, prestamo_table

faker = Faker()
now = datetime.now()


class FakeData:
    def __init__(self, columns: str, data: [str]):
        self.columns = columns
        self.data = data


def build_all_fake_data(size: int) -> Dict[str, FakeData]:
    return {
        biblioteca_table.name: FakeData(
            buildColumnStr(biblioteca_table.columns),
            __build_biblioteca_fake_data(size)
        ),
        socio_table.name: FakeData(
            buildColumnStr(socio_table.columns),
            __build_socio_fake_data(size)
        ),
    }


def build_all_fake_data_with_fk_1_level(size: int, fk_ids: Dict[str, List[int]]) -> Dict[str, FakeData]:
    return {
        libro_table.name: FakeData(
            buildColumnStr(libro_table.columns),
            __build_book_fake_data(size, fk_ids),
        ),
        biblioteca_socio_table.name: FakeData(
            buildColumnStr(biblioteca_socio_table.columns),
            __build_biblioteca_socio_fake_data(size, fk_ids),
        ),
    }


def build_all_fake_data_with_fk_2_level(size: int, fk_ids: Dict[str, List[int]]) -> Dict[str, FakeData]:
    return {
        prestamo_table.name: FakeData(
            buildColumnStr(prestamo_table.columns),
            __build_prestamo_fake_data(size, fk_ids),
        ),
    }


def __build_prestamo_fake_data(size: int, fk_ids: Dict[str, List[int]]):
    libro_ids = fk_ids[libro_table.name]
    socio_ids = fk_ids[socio_table.name]
    if size == 0 or len(socio_ids) == 0 or len(libro_ids) == 0:
        return []

    valid_entries_dict = {}
    for libro_id in libro_ids:
        rdm_size = randrange(len(socio_ids))
        valid_entries_dict[libro_id] = choices(socio_ids, k=rdm_size)

    valid_entries = [(key, value) for key, values in valid_entries_dict.items() for value in values]
    return [f"({fk_libro}, {fk_socio}, '{faker.past_datetime()}', '{faker.future_datetime()}'," +
            f" {choice([1, 0])})" for fk_libro, fk_socio in valid_entries][:size]


def __build_biblioteca_socio_fake_data(size: int, fk_ids: Dict[str, List[int]]):
    biblio_ids = fk_ids[biblioteca_table.name]
    socio_ids = fk_ids[socio_table.name]
    if size == 0 or len(socio_ids) == 0 or len(biblio_ids) == 0:
        return []

    valid_entries_dict = {}
    for biblio_id in biblio_ids:
        rdm_size = randrange(len(socio_ids))
        valid_entries_dict[biblio_id] = choices(socio_ids, k=rdm_size)

    valid_entries = [(key, value) for key, values in valid_entries_dict.items() for value in values]
    return [f"({fk_biblio}, {fk_socio})" for fk_biblio, fk_socio in valid_entries][:size]


def __build_book_fake_data(size: int, fk_ids: Dict[str, List[int]]):
    categorias = ['Terror', 'Fantasia', 'Policial', 'Historia', 'Educativo', 'Novela']
    return __fake_data_builder(
        size,
        lambda: f"('{faker.sentence(15)}', " +
                f" '{faker.name()}, {faker.name()}', " +
                f" {randrange(1, 1_000_000)}, " +
                f" '{choice(categorias)}', " +
                f"{choice(fk_ids[biblioteca_table.name])})"
    )


def __build_biblioteca_fake_data(size: int) -> List[str]:
    return __fake_data_builder(
        size,
        lambda: f"('biblioteca_{faker.city()}', '{faker.address()}')"
    )


def __build_socio_fake_data(size: int) -> List[str]:
    return __fake_data_builder(
        size,
        lambda: f"({randrange(60_000_000)}, '{faker.email()}', '{faker.basic_phone_number()}'" +
                f", '{faker.first_name()}', '{faker.last_name()}', '{faker.date_of_birth()}')"
    )


def __fake_data_builder(size: int, fake_data_generator: Callable[[], str]) -> [str]:
    return [fake_data_generator() for _ in range(0, size)]
