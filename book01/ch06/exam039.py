# sum()

num_list = [x for x in range(1, 11)]
print(sum(num_list))

num_list = [x for x in range(1, 11)]
print(sum(num_list, 100))

num_list = [1, 2, 'h']
print(sum(num_list)) # TypeError

num_list = [1, 2, 3.14]
print(sum(num_list)) # 부동소수도 가능


num_list = [1, 2, 3.14, 5j, True]
print(sum(num_list)) # numeric 타입 가능: int, float, complex, bool
# bool은 int의 서브 타입.




