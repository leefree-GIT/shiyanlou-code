
# 我们可以捕获任何其他普通异常一样，来捕获这些异常
try:
    raise ValueError("A value happend.")   # raise 抛出的异常类型为except后面指定的异常类型，执行except子句
except ValueError:
    print("ValueError in our code")



