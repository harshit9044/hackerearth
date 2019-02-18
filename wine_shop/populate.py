import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_shop.settings')

import django
django.setup()
from random import randint

import random

from wine.models import Wine

from faker import Faker

fakegen = Faker()

def populate(N=1000):
        fake_country = fakegen.country()
        fake_desc = fakegen.text()
        fake_designation = fakegen.name()
        fake_points = randint(1,99)
        fake_price = randint(100,500)
        fake_provience = fakegen.name()
        fake_region_1 = fakegen.address()
        fake_region_2 = fakegen.address()
        fake_variety = fakegen.text()
        fake_winery = fakegen.address()

        wines = Wine.objects.get_or_create(country=fake_country, description=fake_desc,
                                           designation=fake_designation, points=fake_points,
                                            price=fake_price, province=fake_provience,
                                                region_1=fake_region_1, region_2=fake_region_2,
                                                variety=fake_variety, winery=fake_winery)


if __name__ == '__main__':
    print("Strt")
    for i in range(1000):
        populate(1000)
    print ("complete")

