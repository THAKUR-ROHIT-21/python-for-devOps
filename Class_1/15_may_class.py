# WAP to print to all tha total sam even number from 1 to 50


# num1 = 1

# total = 0

# while num1 <= 15:
#     if num1 % 2 == 0:
#         print(num1)
#         total += num1   
        
#     num1 += 1

# print("Sum of all even numbers =", total)


# WAP to check the give string by user is "palindrone" or palindrome 

# str1= input("Enter your string name :- ")
# str2= str1
# rev=""
# i=len(str1)-1

# while i>=0:
#     rev=rev+str1[i]
#     i-=1
# if str2 ==rev:
#     print("palindrone")
# else:
#     print("Not palindrome")



# WAP to reverce the digit : 1234 

n = 1234
r = 0

while n > 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10

print(f"Reversed number = {r}")

