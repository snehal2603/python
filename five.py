# #DATA StRUCTURES:-list,set,dictionary,Tuple
# #list
# # a=[1,2,3,4,5]
# # for i in a:
# #     print(i,end=" ")
# # a=[1,2,3,4,5]
# # a[0]=0
# # print(a)
# # a=[1,2,3,4,5]
# # a.append(10)
# # print(a)
# # a.insert(0,0)
# # print(a)
# # a.extend([10,12,13])
# # print(a)
# # a.remove(10)
# # print(a)
# # a.pop(5)
# # print(a)
# # Print positive and negative elements of an List?
# # l = [10, -1, 2, 4, -9, -7]
# # print("Positive numbers:")
# # for i in l:
# #     if i > 0:
# #         print(i, end=" ")
# # print("\nNegative numbers:")
# # for i in l:
# #     if i<0:
# #         print(i,end=" ")
# # 6 Mean of List elements?
# # l=[1,2,3,4]
# # a=len(l)
# # sum=0
# # for i in l:
# #     sum+=i
# #     mean=sum/a
# # print('mean',mean)    
# # # 6 Find the greatest element and print its index too?
# # l = [1, 2, 3, 4, 5]
# # greatest = l[0]
# # index = 0
# # for i in range(1, len(l)):
# #     if l[i] > greatest:
# #         greatest = l[i]
# #         index = i
# # print(f"greatest element is {greatest} and index is {index}")

# # 6 Find the second greatest element?
# l = [10, 5, 8, 20, 15]
# first = second = l[0]
# for i in range(1, len(l)):
#     if l[i] > first:
#         second = first
#         first = l[i]
#     elif l[i] > second:
#         second = l[i]
# print(f"second greatest element is {second}")

# # 6 Check if List is sorted or not?
# l = [1, 2, 9, 4, 5]
# for i in range(1, len(l)):
#     if l[i] < l[i - 1]:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")
# tuple:
# t=(1,2,3,4)
# print(t.index(3))  
# # this .index finds the first occurence of the number 3 in tuple 
# print(t.count(2))
# # .count finds how many times does the number 2 has occured in the tuple .
# now comes the SETS 
# set={12,13,14,56,78}
# set.add(34)
# # set.remove(55) gives an error if not
# print(set)
# set.discard(55) doesnot gives an error 
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)
# a={12,13,14,15}
# b={13,14,16,17}
# print(a|b) union
# print(a-b) from a which are not in b
# print(a&b) intersection
# print(a^b) from all but not common
#Dictionary
# # d={"name":"Snehal","age":21}
# # print(d["name"])
# # for i in d:
# #     print(i,":",d[i])
# help(dict)
#  Write a Python script to merge two Python dictionaries?
# d1={1:1,2:2,3:3,4:4}
# d2={2:3,3:4,4:5,5:6}
# print(d1|d2)

# Y Write a Python program to sum all the values in a dictionary?
# d1={1:1,2:2,3:3,4:5}
# sum=0
# for i in d1:
#     sum+=d1[i]
# print(sum)

# Y Count the frequency of each element
# d1={1:1,2:2,3:3,4:4,6:1}
# count=int(input("enter the no to find out :"))
# freq=0
# for i in d1:
#     if count==d1[i]:
#         freq+=1
# print(count,freq)    
# Y Write a Python program to combine two dictionary by adding
# values for common keys
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 40}

d3 = d1.copy()

for key in d2:
    if key in d3:
        d3[key] = d3[key] + d2[key]
    else:
        d3[key] = d2[key]

print(d3)