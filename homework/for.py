#输出15以内的奇数

#输出15以内3的倍数

print("15以内奇数")
for i in range(1,15,2):
	print(i)

print("15以内3的倍数(第一种方式)")
for i in range(3,15,3):
	print(i)

print("15以内3的倍数(第二种方式)")
for i in range(3,15):
    if (i%3 == 0):
    	print(i)
	