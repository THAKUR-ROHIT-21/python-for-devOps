# while loops:
    #initializer
    #condition
    #increament / decreament

# i=1

# while i<=10:
#     print(i)
#     i+=1



# write a program 10 to 20 even number

# start = 10
# end= 20

# while start<=end:
#     if start%2==0:
#         print(start)
#     start+=1




# WAP to print factorial
# WAP to print prime number 1 to 15.
# WAP to sum of the indices of string :- "python"



# WAP to print prime numbers

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

while start <= end:

    num = start
    i = 2
    is_prime = True

    if num <= 1:
        is_prime = False

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num)

    start += 1

# WAP to find the sum of indices of a string using while loop

str1 = input("Enter a String :- ")

l = len(str1)
sum1 = 0
i = 0

while i < l:
    sum1 += i
    i += 1

print("Sum of indices =", sum1)


# WAP to print factorial using while loop

var2 = int(input("Enter Your Number :- "))

fact = 1
i = 1

while i <= var2:
    fact = fact * i
    i += 1

print("Factorial =", fact)
