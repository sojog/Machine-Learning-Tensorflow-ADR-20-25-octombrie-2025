

x = 10
y = 99
print("x = ", x, " y = ", y)

## unpacking (stanga) - packing (dreapta)
x, y = y, x
print("x = ", x, " y = ", y)

## packing - nu sunt obligatorii ()
a = y, x
print(a, type(a))

## unpacking
m, n = a 
print("m = ", m, " n = ", n)