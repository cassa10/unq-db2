from collections.abc import Callable
from typing import Dict, List
from datetime import datetime
from faker import Faker
from random import randrange

faker = Faker()

now = datetime.now()


class FakeData:
    def __init__(self, columns: str, data: [str]):
        self.columns = columns
        self.data = data


def build_all_fake_data(size: int) -> Dict[str, FakeData]:
    return {
        "dbo.biblioteca": FakeData(
            buildColumnStr(["nombre", "direccion"]),
            build_biblioteca_fake_data(size)
        ),
        "dbo.socio": FakeData(
            buildColumnStr(["dni", "email", "telefono", "nombre", "apellido", "fechaNacimiento"]),
            build_socio_fake_data(size)
        ),
    }


def build_biblioteca_fake_data(size: int) -> List[str]:
    return fake_data_builder(
        size,
        lambda: f"('biblioteca_{faker.city()}', '{faker.address()}')"
    )


def build_socio_fake_data(size: int) -> List[str]:
    return fake_data_builder(
        size,
        lambda: f"({randrange(60_000_000)}, '{faker.email()}', '{faker.basic_phone_number()}'" +
                f", '{faker.first_name()}', '{faker.last_name()}', '{faker.date_of_birth()}')"
    )


def fake_data_builder(size: int, fake_data_generator: Callable[[], str]) -> [str]:
    return [fake_data_generator() for _ in range(0, size)]

def buildColumnStr(columns: [str]):
    return f"({', '.join(columns)})"
