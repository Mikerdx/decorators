def add_menu(cls):
    def menu(self):
        return ["Vanilla", "Chocolate", "Strawberry"]

    cls.menu = menu
    return cls

@add_menu
class IceCreamTruck:
    def sell_ice_cream(self):
        print("🚚 Selling ice cream on the road!")

truck = IceCreamTruck()
print(truck.menu())  # ['Vanilla', 'Chocolate', 'Strawberry']
truck.sell_ice_cream()
