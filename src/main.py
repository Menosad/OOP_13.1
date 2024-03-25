from src.classes import Product, Category, NewClass

prod1 = Product('Ноги', 'средство передвижения', 999, 2)
prod2 = Product('Руки', 'средство управления', 666, 2)
prod3 = Product('Голова', 'средство мысления', 5000, 1)

cat = Category('Человек', 'части тела', [prod1, prod2, prod3])

test = NewClass(cat, 2)

for i in test:
    print(i)