# str1= "This is python"
# num=0
# for i in str1:
#     if i == " ":
#         num+=1
# print(num)





# print(str1.count(" "))



c=0
a= "this is python"
for i in a:
    if i=="i":
        c+=1
print(c)


str2= "How are you"

c=0

for i in str2:
    if i == "o":
        continue
    else:
        c+=1
print(c)



address= "D-1 267/268 mayur-vihar-phase-3 110092 "
c1=0

for i in address:
    if i in "1234567890":
        c1+=1
print(c1)

address1= "D-1 267/268 mayur-vihar-phase-3 110092"
c1=0

for i in address1:
    if i not in "1234567890":
        c1+=1
print(c1)






