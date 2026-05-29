# start :- include
# Stop :- Exclude

# marks = [20,30,40,80,90,10,34,55]
# for i in range(len(marks)):
#     print(marks[i],end=" ")


# marks = [20,30,40,80,90,10,34,55]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This is even number :- {marks[i]}")
#     else:
#         print(f"This is odd number :- {marks[i]}")



# marks = [20,30,40,80,90,10,34,55]
# first=marks[0]
# secound=marks[7]

# marks[-1]=first
# marks[0]=secound

# print(marks)

# Wap to find the sum the all element of list

marks = [20, 30, 40, 80]

t = 0

for i in marks:
    t+= i

print("Total Sum is :- ",t) 

# Wap to find the of only even number

mark=[10,20,30,40]
c=0
for i in mark:
    if i % 2==0:
        c+=i
print(c)




# Wap to find the only odd number

mark=[10,25,35,40]
c=0
for i in mark:
    if i%2 != 0:
        c+=i
print(c)



# Wap to find the count of how many int value and how many str in the text
# [70,"aman",50,10,20,"rohan","iq-india"]

m = [70, "aman", 50, 10, 20, "rohan", "iq-india"]

c = 0
s = 0

for i in m:

    if i in [70, 50, 10, 20]:
        c += 1
    else:
        s += 1

print("Integer count =", c)
print("String count =", s)





