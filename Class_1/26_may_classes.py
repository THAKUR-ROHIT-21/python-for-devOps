# Data Structure
# Data structure used to store data effeciently and make faster process
# For operation like read and write
# 1. list  :- list()
# 2. string :- str()
# 3.Dictionary :- dict()
# 4.set : set()
# 5.tuple :- tuple()

# list :- list is a data structure in python used to store multiple data in of different types in one variable.

# list :- list can deffine by using squre [] and data inside known as element.
# list can be hetrogenous and homogenous.
# list are mutable (changeable).
# List support indexting , sliceing and follow ordering sequence.
# index start from :- 0 [length-1]
# length start from :- 1

# 1.creation of list , 
# 2.Updation of list, 
# 3.Slicdeing of list ,  
# 4.Traversing , 
# 5.inbuild method
# 6.Test
# 7.Assignment



# marks_10th= [20,55,50,80,90] # under the list the name of data is element
# # print("Before Update :",marks_10th)
# # marks_10th[-1]=marks_10th[0]+marks_10th[4]
# i=2
# print(marks_10th[-1])


# 3.Slicdeing of list

# marks = [20,30,40,80,90,10,34,55]
# [start-0:stop-1:step-1]    # in sliceing index start stop and step using this colun [:::]

# sub_list=marks[1:6]
# print(sub_list)

# sub_list=marks[0:6]
# print(sub_list)

# sub_list=marks[0:6:2] # where [(0) is start value] , [(6) is stop value], [(2) is step value]
# print(sub_list)

# sub_list=marks[::-1] #  Reverse value
# print(sub_list)

# sub_list=marks[0:6:-1]
# print(sub_list)


# 4.Traversing

# marks = [20,30,40,80,90,10,34,55]
# for i in range(len(marks)):
#     print(marks[i],end=" ")


# Even or Odd 


# marks = [20,30,40,80,90,10,34,55]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This is even number :- {marks[i]}")
#     else:
#         print(f"This is odd number :- {marks[i]}")

# without range

# marks = [20,30,40,80,90,10,34,55]
# t=0

# for i in marks:
#     t+=i
# print(t)





marks = [20,30,40,80,90,10,34,55]
sub_list=marks[2::-1]
print(sub_list)























































