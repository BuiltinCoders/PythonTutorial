'''
iterable = those statments on we can use iter function and '.__next__()' keyword

generator = those statments or commands we can generator result values on the go.

'''

# for i in range(100):
#     print(i)

def gen(n):
    for i in n:
        yield i        # yeild defines the generator values

h = gen('harry')
# h.__iter__()

print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())
print(h.__next__())