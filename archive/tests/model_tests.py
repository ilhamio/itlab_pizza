from decimal import Decimal
from unittest import TestCase

from archive.models.archive_order import ArchiveOrder


class ArchiveOrderModelTests(TestCase):

    def setUp(self) -> None:
        ArchiveOrder.objects.create(name_in_queue='ilham', cost=Decimal(500), place=12, comment='Лук не добавлять!',
                                    json_of_items={'Маргарита маленькая': 2})
        ArchiveOrder.objects.create(name_in_queue='Николай', cost=Decimal(700), place=10,
                                    json_of_items={'Пицца ветчина с сыром': 3})

    def check_getter(self):
        ilham = ArchiveOrder.objects.get(id=1)
        nik = ArchiveOrder.objects.get(id=2)

        self.assertIs(ilham.get)
