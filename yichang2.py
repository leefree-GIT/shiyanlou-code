# 定义清理行为
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world')

# 不管有没有异常发生，finally子句在程序离开try后都一定会被执行。
# 当try语句中发生了未被except捕获的异常，在finally子句执行完后
# 他会被重新抛出。
