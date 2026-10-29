import json
from .classes.customer import Customer
from .classes.shop import Shop

def shop_trip():
    with open("app/config.json", "r") as config:
        data = json.load(config)
        FUEL_PRICE = data["FUEL_PRICE"]
        customers = [Customer(**customer_dict) for customer_dict in data["customers"]]
        shops = [Shop(**shop_dict) for shop_dict in data["shops"]]

    for customer_dict in customers:
        cheapest_shop = sorted(
            shops,
            key=lambda shop: customer_dict.trip_price(shop, FUEL_PRICE)
        )[0]
        
shop_trip()