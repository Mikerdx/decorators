def add_sprinkles(function):
    def wrapper():
        print("*You add sprinkles*")
        function()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("Here is your  ice cream")
    
get_ice_cream()