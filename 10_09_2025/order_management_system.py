class ProductSearch:
    def search_product(self,name=None, category=None, price=None, range=None):
        if name is not None and category is not None and price is not None and range is not None:
            print(f"name: {name}")
            print(f"category: {category}")
            print(f"price: {price}")
            print(f"range: {range}")
        elif name is not None and category is not None and price is not None:
            print(f"name: {name}")
            print(f"category: {category}")
            print(f"price: {price}")
        elif name is not None and category is not None:
            print(f"name: {name}")
            print(f"category: {category}")
        elif name is not None:
            print(f"name: {name}")
        else:
            print("Product detals not found")

print("PRoduct search:")
prod = ProductSearch()
print("*" * 50)
prod.search_product("Soap")
print("*" * 50)
prod.search_product("Soap", "A")
print("*" * 50)
prod.search_product("Soap", "B", "1000 Rs")
print("*" * 50)
prod.search_product("Soap", "B", "1000 Rs", "500 to 2000")
print("*" * 50)

class Cart:
    def add_product(self,name1=None,quantity1=None,name2=None,quantity2=None):
        if name1 is not None and quantity1 is not None and name2 is not None and quantity2 is not None:
            print(f"name: {name1}, quantity: {quantity1}, name: {name2}, quantity: {quantity2}")
        elif name1 is not None and quantity1 is not None:
            print(f"name: {name1}, quantity: {quantity1}")
        else:
            print("Product is not found")

#print("PRoduct search:")
cart = Cart()
cart.add_product("Ä","100","B","200")
print("*" * 50)
cart.add_product("C","50")
print("*" * 50)

class Discount:
    def check_discount(self,flat_discount=None,per_discount=None,buy_one_get_on=None):
        if flat_discount is not None:
            print("Flat discount: {flat_discount}")
        elif per_discount is not None:
            print("Percentage discount: {per_discount}")
        elif buy_one_get_on is not None:
            print("Another discount: {buy_one_get_on}")
        else:
            print("No discount")

discount = Discount()
discount.check_discount("30%")
print("*" * 50)
discount.check_discount(None, "10%")
print("*" * 50)
discount.check_discount(None, "Buy 1 Get 1")
print("*" * 50)

class Payment:
    def pay(self):
        print("Basic payement")

class CreditCardPayment:
    def pay(self):
        print("Credit card payment")

class UPIPayment:
    def pay(self):
        print("UPI card payment")

class CODPayment:
    def pay(self):
        print("COD card payment")

payments = [Payment(), CreditCardPayment(), UPIPayment(), CODPayment()]
for payment in payments:
    payment.pay()
