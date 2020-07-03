lst = [1,2,3,4,5]
def square(num):
    "返回所给数字的平方"
    return num * num

print(list(map(square, lst)))
