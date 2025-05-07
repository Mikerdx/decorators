def log_flavor(func):
    def wrapper(self, *args, **kwargs):
        print(f"📋 Preparing to serve: {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class IceCreamShop:
    @log_flavor
    def serve_vanilla(self):
        print("🍦 Serving vanilla ice cream!")

    @log_flavor
    def serve_chocolate(self):
        print("🍦 Serving chocolate ice cream!")

shop = IceCreamShop()
shop.serve_vanilla()
shop.serve_chocolate()
