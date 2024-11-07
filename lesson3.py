x = int(input("Введите х:"))
y = int(input("Введите y:"))
if y == 0:
    quit("На ноль делить нельзя")
z = x/y
a = x//y
c = z-a
print("result c:"+str(c))
print("result z:"+str(z))
