

###########################################列表简介##########################################

bycicles = ['trik','cannodale','cosmoswork','redline','specialized']    #方括号表示列表

print(bycicles)
print(bycicles[0])              
print(bycicles[-1])                  #用-1访问最后一个元素

print("\n")
motocycles = ['\tyamaha','honda','suzuki']
print(motocycles[0])

  #可直接给对应元素赋值
motocycles[0] = 'ducati'          
print(motocycles)


 #.append() 可以在列表中添加元素
print(motocycles)
motocycles.append('bmw')            


#insert(x,'***')可在任意位置添加新元素
print("\n")
motocycles.insert(1,'benz')
print(motocycles)

#del 可删除对应位置的元素  
print("\n")
del motocycles[0]
print(motocycles)
 
# pop()可弹出最后的元素并能继续使用
print("\n")
poped_motocycles = motocycles.pop()
print(motocycles)
print(poped_motocycles)


#  remove()可根据值来删除元素,只删除第一个指定的值，如果列表中有多个需要删除的值，就需要使用循环来确保每个值都删除
print("\n")
print(bycicles)
bycicles.remove('trik')
print(bycicles)
bycicles.remove('cannodale')
print(bycicles)


#sort()对列表进行永久排序    利用(reverse=Ture)可翻转顺序   
print("\n")
cars = ['audi','bmw','lixiang','weilai','xiaopeng','tesla']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#sorted()对列表进行临时排序  利用(reverse=True)可翻转顺序   
cars = ['audi','bmw','lixiang','weilai','xiaopeng','tesla']
print("\nHere's the orignal list:")
print(cars)
print("\nHere's the sorted list:")
print(sorted(cars))
print("\nHere's the orignal list AGAIN:")
print(cars)
print("\nHere's the reverse sorted list:")
print(sorted(cars,reverse=True))


#而reverse()可倒着打印列表
print("\n")
cars.reverse()
print(cars)

#len()获取列表长度
print("\n")
print(len(cars))