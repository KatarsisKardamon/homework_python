from mailing import Mailing

to_address = 456789, 'Tomsk', 'Lenin', 23, 3
from_address = 46649, 'Novosibirsk', 'Bolshaya', 231, 23
cost = 21
track = '434'

random_mailing = Mailing(to_address, from_address, cost, track)

print(random_mailing)
