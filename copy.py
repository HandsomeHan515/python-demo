import copy

a = [1, 2, 3, 4, [1, 2]]  # 原始对象

b = a  # 赋值，传对象的引用

c = copy.copy(a)

d = copy.deepcopy(a)

c.append(5)
c[4].append('c')

print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)
