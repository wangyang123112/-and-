
import re
import json



text_str = "我喜欢吃鸡吃鸡真的超级好玩我超级喜欢它的"

a = 0
b = 1
list1 = []
while a < len(text_str) -1:
    key = text_str[a]
    value = text_str[b]
    # print(key,value)
    a += 1
    b += 1
    dict1 = {}
    dict1[key] = value
    list1.append(dict1)
#
# for item in list:
#     result =
#l1 = ['b','c','d','b','c','a','a']
l2 = []
l3 = []
for i, val in enumerate(list1):
    if not val in l2:
        l2.append(val)
    else:
        key = list(val)[0]
        value = list(val.values())[0]
        evolution_left = {}
        evolution_right = {}
        evolution_left[list(list1[i-1])[0]] = key + value
        evolution_right[key + value] = list(list1[i+1].values())[0]
        l3.append(evolution_left)
        l3.append(evolution_right)

print(l3)
# for f, item in enumerate(l2):
#     key = item.keys()
#     print(key)