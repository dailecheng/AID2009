# dict01 = {1: "a", 2: "b"}
# print(dict01)
# print(str(dict01))
# def fun(n):
#     n['key'] = 10000
#
#
# a = {'key': 10}
# fun(a)
#
# print(a)
"""过桥"""

# import random
#
# while True:
#     # a岸
#     a = [1, 3, 6, 8, 12]
#     # b岸
#     b = []
#     # 速度
#     SPEED = 0
#     # 流程
#     step = []
#
#     while True:
#         # 随机获取两个a中的元素
#         x = random.sample(a, 2)
#         # 将元素放入b中
#         b.extend(x)
#         # 从a中删除元素
#         a.remove(x[0])
#         a.remove(x[1])
#         step.append(x)  # 将随机组合添加到列表
#         step.append(max(x))  # 将随机组合的过河时间也添加到列表
#         if not a:
#             break
#
#         # 从b中随机找一个到a
#         y = random.sample(b, 1)
#         a.extend(y)
#         b.remove(y[0])
#         step.append(y[0])  # 记录 返回的时间
#         step.append('||')
#
#     # print(step)
#     for i in step:
#         if type(i) == int:
#             SPEED += i
#     if SPEED <= 30:
#         break
# print(step)
"""找排序列表中缺失的数"""


# def find_num(list_target):
#     if list_target[-1] == len(list_target) - 1:
#         return len(list_target)
#     for i in range(len(list_target)):
#         if i != list_target[i]:
#             return i


# print(find_num([0,1,2,3,5,6,7]))
# print(find_num([0, 2]))

