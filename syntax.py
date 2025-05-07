decorator_name
wrapper
decorator_name

def decorator_name(func):
    def wrapper(*args,**kwargs):
        #add a functionality
    return wrapper 

@decorator_name
def function_to_decorate():
    #original function code 
    pass