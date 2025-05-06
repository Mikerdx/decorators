def add_sprinkles(function):
    def wrapper(*args,**kwargs):
        print("*You add sprinkles*")
        function(*args,**kwargs)
    return wrapper
    
def add_fudge(function):
    def wrapper(*args,**kwargs):
        print("*You add fudge*")
        function(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")
    
get_ice_cream("chocolate")