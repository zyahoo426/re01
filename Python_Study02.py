

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!\n")
          

# for cat in cats:
# for dog in dogs:
# for item in list_of_items:



#range()  创建数值列表


for value in range(1,5):
    print(value)

#创建数字列表
numbers = list(range(1,6))
print(numbers)



#输出乘方

squares = []
for value in range(1,11):
    # square = value **2
    # squares.append(square)
    squares.append(value **2)
    squares.append(value **3)
print(squares)

#v0.1