from __future__ import print_function

# x = int(input("Please input an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print("Single")
# else:
#     print("More")


a = ['cat', 'window', 'defenestrate']
for x in a:
    print(x, len(x))

for x in a[:]:  # 若想在循环体内修改你正迭代的序列, 制造整个列表的切片复本
    if len(x) > 6:
        a.insert(0, x)

# print(a)


# def f(b, L=[]):  #  调用中会累积参数值
#     L.append(b)
#     return L
# def f(b, L=None):  # 不想让参数值被后来的调用共享
#     if L is None:
#         L = []
#     L.append(b)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))


# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we'5-re all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])
#
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

a.append("ppppp")

print(a)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in [0, 1, 2]:
    for row in mat:
        print(row[i], end="")
    print()

