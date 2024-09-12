from collections.abc import Callable
from typing import Dict, List
from datetime import datetime
from faker import Faker
from random import randrange

faker = Faker()

now = datetime.now()


def build_all_fake_data(size: int) -> Dict[str, List[str]]:
    return {
        "biblioteca": build_biblioteca_fake_data(size),
        "socio": build_socio_fake_data(size),
    }


def build_biblioteca_fake_data(size: int) -> [str]:
    return fake_data_builder(
        size,
        lambda: f"(biblioteca_{faker.city()}, {faker.address()})"
    )


def build_socio_fake_data(size: int) -> [str]:
    return fake_data_builder(
        size,
        lambda: f"({randrange(60_000_000)}, {faker.email()}, {faker.phone_number()}" +
                f", {faker.first_name()}, {faker.last_name()}, {faker.date_of_birth()})"
    )


def build_persons_fake_data(size: int) -> [str]:
    return fake_data_builder(
        size,
        lambda: f"({faker.first_name()}, {faker.last_name()}, {now.year - int(faker.year())})"
    )


def fake_data_builder(size: int, fake_data_generator: Callable[[], str]) -> [str]:
    return [fake_data_generator() for _ in range(0, size)]
