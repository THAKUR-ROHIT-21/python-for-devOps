

def add(text,ch):
    c = 0
    for i in text:
        if i == ch:
            c += 1
    return c
res = add("hello","l")
print(res)

