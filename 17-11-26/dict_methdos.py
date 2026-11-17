product = {
    "code":"1",
    "name":"printer"
}
# print(product)
# product.update({"qty":1})
# product.update({"code": "101"})
# print(product)
# print(product.keys())
# print(product.values())
# print(product.items())
# x = product.get("code")
# print(x)
# product.pop("qty")
# product.popitem()
# print(product)
product2 = product.copy()
print(product2)
product2["qty"] = 5
print(product)
print(product2)