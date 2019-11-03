def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decor
def num():
    return 5

print(num())

'''resultfun = decor(num)
print(resultfun())'''

'''def inner():
        result = num()
        return result*2
print(inner())'''