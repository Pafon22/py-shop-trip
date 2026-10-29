from .shop import Shop
from .car import Car


class Customer():
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[float],
        money: int,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def check_distance_to_ride(self, location_shop: list[float]) -> None:
        result = (
            (self.location[0]  - location_shop[0]) ** 2
        + (self.location[1] - location_shop[1]) ** 2
        ) ** 0.5
        return round(result, 2)
    
    def check_price_to_ride(self, shop: Shop, fuel_price: float) -> float:
        result = round((
            self.check_distance_to_ride(shop.location)
            * self.car["fuel_consumption"] / 100 # liters for 1km
            * fuel_price # price for 1l
        ), 2)
        return result


    def ride(self, shop: Shop, fuel_price: float) -> None:
        self.old_location = self.location
        self.location = shop.location
        self.money -= self.check_price_to_ride(shop.location, fuel_price)
        print(f"{self.old_location} -> {self.location}")

    def back(self) -> None:
        temporary_location = self.location
        self.location = self.old_location
        self.old_location = temporary_location
        print(f"{self.old_location} -> {self.location}")

    def check_price_to_buy_products(self, shop: Shop) -> float:
        products_price = 0
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                products_price += (quantity * shop.products[product])
        return round(products_price, 2)

    def buy_products(self, shop: Shop) -> None:
        self.money -= self.check_price_to_buy_products(shop)


    def trip_price(self, shop: Shop, fuel_price: float) -> Shop:
        print(f"{self.name}'s trip to the"
        result = (
            self.check_price_to_buy_products(shop)
            + self.check_price_to_ride(shop, fuel_price) * 2
        )

    def to_do_the_trip(self, shops: list[Shop], fuel_price: float) -> float:
        cheapest_shop = sorted(
            shops,
            key=lambda shop: self.trip_price(shop, FUEL_PRICE)
        )[0]

        print(f"{self.name} has {self.money} dollars.")
        print(
            f"{self.name} trip to the {shop.name} "
            
        )
        print(
            f"{self.name}'s trip to the {shop.name} costs {self.trip_price(shop, fuel_price)}"
        )
