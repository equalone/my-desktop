# 字符串反转输出
# strs="hello"
# print(strs[::-1])


# 阶乘的递归写法
# def a(n):
#     if n!=1:
#         return n * a(n-1)
#     else :return n
# print(a(5))

# 句子字符串输出最长单词的长度
# m=0
# strs="The quick brown fox jumped over the lazy dog"
# for i in strs.split(' '):
#     if m<len(i):
#         m=len(i)
# print(m)


# 请返回一个数组，该数组由参数中每个子数组中的最大数字组成。 为简单起见，给出的数组总会包含 4 个子数组。
# lis=[[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]
# arr=[]
# for i in lis:
#     arr.append(max(tuple(i)))
# print(arr)

# 检查字符串（第一个参数 str）是否以给定的目标字符串（第二个参数 target）结束。
# str1='any'
# str2='all any'
# print(len(str2)-len(str1))
# print(str2[4:])
# def a(str,target):
#     return str2[len(str)-len(target):]==target
# print(a(str2,str1))
# import re
# 正则法
# def a(str,target):
#     pattern=target+"$"
#     if re.findall(pattern,str):
#         return True
#     else :return False
# print(a(str2,str1))
# print(re.search(str1+'$',str2,re.I))

# 将一个给定的字符串 str（第一个参数）重复输出 num（第二个参数）次。 如果 num 不是正数，返回空字符串
# def a(str,num):
#     if num<=0:
#         print('')
#     else :
#         for i in range(num):
#             print(str)
# a("hello",3)


# 如果传入的字符串（第一个参数）的长度大于传入的值（第二个参数），请在这个位置截断它， 并在后面加上 ...，然后返回结果
#
# def a(str1,num):
#  if len(str1)>=num:
#  return str1
#  else :return str1[:num]+'...'
# a("A-tisket a-tasket A green and yellow basket", 8)

# 将传入的字符串中，每个单词的第一个字母变成大写并返回。 注意除首字母外，其余的字符都应是小写的


# c=[]
# def a(st):
#      b=st.split(' ')
#      for i in b:
#          c.append(i.lower().title())
#      return ' '.join(c)
# print(a("I'm a little tea pot"))


# 从数组中移除所有假值
# b=[]
# def a(lis):
#     for i in lis:
#         if bool(i)==True:
#             b.append(i)
#     return b
# print(a([7, "ate", "", False, 9]))

# 找出元素在排序后数组中的索引
# def a(lis,n):
#     lis.append(n)
#     lis.sort()
#     return lis.index(1.5)
# print(a([1,2,3,4], 1.5))


# 编写一个函数，该函数将一个数组（第一个参数）拆分成若干长度为 size（第二个参数）的子数组，并将它们作为二维数组返回
# def a(lis, n):
#     c = []
#     while len(lis) > 0:
#         c.append(lis[0:n])
#         del lis[0:n]
#     return c
# print(a([0, 1, 2, 3, 4, 5, 6], 3))

#打印pygame内置字体
# import pygame
# a=pygame.font.get_fonts()
# for i in a:
#     if i=='freesansbold':

#         print(i)