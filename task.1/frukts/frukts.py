class Praduct:
    COUNT = 0

    def __init__(self, name, price, barcode):
        self.name = name
        self.price = price
        self.barcode = barcode

class Fruit(Praduct):
    def __init__(self, name, price, barcode ,**kwargs):
        super().__init__(name, price, barcode)
        self.barcode = barcode
        self.fruit_data = kwargs



class Vegetebls(Praduct):
    def __init__(self, name, price, barcode, **kwargs):
        super().__init__(name, price, barcode)
        self.barcode = barcode
        self.vegetebls_data = kwargs


class Drink(Praduct):
    def __init__(self, name, price, barcode, **kwargs):
        super().__init__(name, price, barcode)
        self.barcode = barcode
        self.drink_data = kwargs


PRATUCT_TYPES = {
    1: Fruit,
    2: Vegetebls,
    3:Drink,

}

products = []


while Praduct.COUNT < 4:
    praduct_type = int(input(
        f"Selest product type:\n"
        f"1: {PRATUCT_TYPES.get(1).__name__}\n"
        f"2: {PRATUCT_TYPES.get(2).__name__}\n"
        f"3: {PRATUCT_TYPES.get(3).__name__}\n"

    ))
    if praduct_type not in PRATUCT_TYPES.keys():
        print("Invalid product type!")
        continue
    ChildProduct = PRATUCT_TYPES.get(praduct_type)
    name = input("Enter product name: ")
    price = input("Enter product price:")
    barcode = input("Enter product barcode:")
    extra_data = {}
    obj = ChildProduct(name, price, barcode ,**extra_data)
    products.append(obj)
    print("Products count", Praduct.COUNT)
print(products)
