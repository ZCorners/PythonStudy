# coding=utf-8
# 整数背包问题


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return 'name:' + self.name + '--value:' + str(self.value) + '--weight:' + str(self.weight)


# guitar = Item('guitar', 1, 1500)
# sound = Item('sound', 4, 3000)
# laptop = Item('laptop', 3, 2000)
# iphone = Item('iphone', 1, 2000)
# goods = [guitar, sound, laptop, iphone]
water = Item('water', 3, 10)
book = Item('book', 1, 3)
food = Item('food', 2, 9)
jacket = Item('jacket', 2, 5)
camera = Item('camera', 1, 6)
goods = [water, book, food, jacket, camera]

row = len(goods)
column = 6  # 背包容量，1为间隔划分单元格

cell = [[0 for i in range(column)] for j in range(row)]
for i in range(row):
    ii = i + 1
    item = goods[i]
    for j in range(column):
        jj = j + 1
        if ii == 1:
            if item.weight <= jj:
                cell[i][j] = item.value
        else:
            # 涉及单元格操作的时候需要将ii, jj往前挪一格
            tmp = jj - item.weight
            if tmp > 0:
                cell[i][j] = max(cell[i - 1][j], item.value + cell[i - 1][jj - item.weight - 1])
            elif tmp == 0:
                cell[i][j] = max(cell[i - 1][j], item.value)
            else:
                cell[i][j] = cell[i - 1][j]

print cell
