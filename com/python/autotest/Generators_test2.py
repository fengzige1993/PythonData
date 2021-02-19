"""
python三大神器之【生成器】（generators）
"""
"""
生成器也是一种迭代器，
但是你只能对其迭代一次。
这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。
你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。
大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值。这里有个生成器函数的简单例子：
"""
#
def generator_function():
    for i in range(10):
        yield i

for item  in generator_function():
    print(item)
"""
这个案例并不是非常实用。生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。
译者注：这样做会消耗大量资源
---------
许多Python 2里的标准库函数都会返回列表，而Python 3都修改成了返回生成器，因为生成器占用更少的资源。
下面是一个计算斐波那契数列的生成器：
"""
#
def fibon1(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
for x in fibon1(1):
    print(x)
#
# """
# 用这种方式，我们可以不用担心它会使用大量资源。然而，之前如果我们这样来实现的话：
# """
def fibon2(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
"""
这也许会在计算很大的输入参数时，用尽所有的资源。
我们已经讨论过生成器使用一次迭代，但我们并没有测试过。
在测试前你需要再知道一个Python内置函数：next()。
它允许我们获取一个序列的下一个元素。那我们来验证下我们的理解：
"""
def generator_function():
      for i in range(3):
          yield i

gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#output:StopIteration

"""
我们可以看到，在yield掉所有的值后，next()触发了一个StopIteration的异常。
基本上这个异常告诉我们，所有的值都已经被yield完了。
你也许会奇怪，为什么我们在使用for循环时没有这个异常呢？啊哈，答案很简单。
for循环会自动捕捉到这个异常并停止调用next()。你知不知道Python中一些内置数据类型也支持迭代哦？
"""

my_string = "Yasoob"
next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator

"""
好吧，这不是我们预期的。
这个异常说那个str对象不是一个迭代器。
对，就是这样！它是一个可迭代对象，而不是一个迭代器。
这意味着它支持迭代，但我们不能直接对其进行迭代操作。
那我们怎样才能对它实施迭代呢？是时候学习下另一个内置函数，
iter。它将根据一个可迭代对象返回一个迭代器对象。这里是我们如何使用它：
"""
my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))
# Output: 'Y'

my_string1 = "hufeng"
my_iter1 = iter(my_string1)
print(next(my_iter1))