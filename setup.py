#!/usr/bin/env python3
from models import db, Dish, Restaurant, Category
# from app import create_app
def setup():
    db.create_all()

    dish1 = Dish(name="Seafood wok", restaurant_id="1", category_id="1", ratings="5")
    category1 = Category(name="Chinese")
    restaurant1 = Restaurant(name="Fashion Wok", city="Foster City", state="CA", address="test address", website="www.google.com")

    db.session.add(dish1, category1, restaurant1)
    db.session.commit()
    print("Hello again")

if __name__ == '__main__':
    setup()