def add_sprinkles(function):
    def wrapper(): #is a function that takes another function as an argurment,adds some functionality to it and then returns a new function
        print("*You add sprinkles*")
        function()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("Here is your  ice cream")
    
get_ice_cream()