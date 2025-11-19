from smartphone import Smartphone

catalog = [
        Smartphone('iPhone', '16 Pro/Pro Max', '89501234567'),
        Smartphone('SUMSUNG', 'Galaxy S25 Ultra', '89831234567'),
        Smartphone('Xiaomi', '15 Ultra', '89141234567'),
        Smartphone('Honor', 'Magic 7 Pro', '891021234567'),
        Smartphone('Xiaomi', 'OnePlus 13', '890221234567')
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model} . '
          f'{smartphone.phone_number}')
