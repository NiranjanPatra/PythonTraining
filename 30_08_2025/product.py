product = ("Laptop", 50000, "Black" ,'Samsung', "Electronics")
print("The second element = ", product[1])

print("The last two elements = ", product[(len(product) - 2):])

if "Electronics" in product:
    print("Electronics is present in the product")
else:
    print("Electronics is not present in the product")

product_prices = (1000, 1500, 1200, 1100, 900)
print("How many times 1000 occurs? ", product_prices.count(1000))

print("Max price = ", max(product_prices))
print("Min price = ", min(product_prices))

for item in product:
    print("Item = ", item)

product_list = list(product)
product_list[1] = 55000
product = tuple(product_list)
print("Updated products = ", product)

add_item = ("In Stock")
complete_product = product + ("In Stock",)
print("Complete product = ", complete_product)

product_list = list(complete_product)
product_list.remove("Electronics")
product = tuple(product_list)
print("After remove = ",product)

a,b,c,*rest = product
print("a = ", a, "b = ", b, "c = ", c)

nested_product = ((1, "A", 1200), (2, "B", 80000), (3, "C", 400))
second_product = nested_product[1][1]
print("Second product name = ", second_product)
