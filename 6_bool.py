v = True
f=False
print(v)
print(f)
print(type(v))
print(type(f))

print(5>3)
print(5<3)

print(bool("Hola"))
print(bool(""))


#True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#False
print(bool(""))
print(bool(0))
print(bool(None))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool({}))

x=1.23
print(isinstance(x,float))