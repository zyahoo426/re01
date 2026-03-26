


#复制列表
#要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始和终止索引[:]。这让Python创建整个列表的副本


My_Foods = ["pizza","hamberger","vagetables","beef"]
My_Friends_Foods = My_Foods[:]

print(f"My favorite foods are :\n{My_Foods}")

print(f"My friend's favorite foods are:\n{My_Friends_Foods}")

#元组： 列表是可以修改的，而不可变的列表被称为元组。

demensions = (200,50)
print(demensions[0])
print(demensions[1])

#虽然不能修改元组的元素，但是可以给储存元组的变量赋值

demensions = (400,40)
print(demensions[0])
print(demensions[1])


answer = 17
if answer != 42:
    print("That's not the correct  answer! Please try again.")