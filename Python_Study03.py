


#复制列表
#要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始和终止索引[:]。这让Python创建整个列表的副本


My_Foods = ["pizza","hamberger","vagetables","beef"]
My_Friends_Foods = My_Foods[:]

print(f"My favorite foods are :\n{My_Foods}")

print(f"My friend's favorite foods are:\n{My_Friends_Foods}")

