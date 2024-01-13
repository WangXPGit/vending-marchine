menu = {
    "披萨" : 300,
    "爆米花" : 200,
    "薯条" : 90,
    "洋芋片" : 60,
    "软面包条" : 120,
    "苏打水" : 60,
    "柠檬水" : 90
}

print("菜单")
print("---------------")

cart = []
total = 0
for item, price in menu.items():
    print(f"{item}: {price}")

print("")

while True:
    food = input("请输入一个菜单项目(输入 q 结束)")
    if food == "q":
        break
    elif menu.get(food) is None:
        print(f"没有这个商品 {food}")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food, end=" ")

print(f"总共： {total}")