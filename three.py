def add_sprinkles(func):
    def wrapper():
        print("*You add sprinkles on the ice cream*")
        func()
        print("*You enjoy the ice cream with sprinkles*")
    return wrapper

@add_sprinkles
def serve_ice_cream():
    print("Here is your ice cream!")

serve_ice_cream()
