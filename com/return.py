def plus(val1, val2):
    return val1+val2

def print_hello(p1, p2):
    print("hello ", p1, p2)

result_hello = print_hello(10, 20)
result_plus  = plus(10,20)

print("plus : ", result_plus)
print("hello : ", result_hello) #none 나옴. 리턴값이 없어서..