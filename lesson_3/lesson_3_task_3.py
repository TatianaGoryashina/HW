from address import Address
from mailing import Mailing

to_address = Address("101000", "Москва", "Тверская", "10", "5")
from_address = Address("104000", "Санкт-Петербург",
                       "Невский проспект", "20", "8")

mailing = Mailing(to_address, from_address, 150.75, "TRK123456")

print(
    f"Отправление {mailing.track} из {mailing.from_address} "
    f"в {mailing.to_address}. Стоимость {mailing.cost} рублей."
)
