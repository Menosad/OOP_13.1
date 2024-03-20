from src import classes

prod1 = classes.Product.from_string('xiaomi-smartphone-15000-2')
print(prod1.price)
print(prod1.get_price)
prod1.get_price = 10000
print(prod1.get_price)
