
## In python este preferat snake_case in loc de camelCase
o_lista = [22, 33, 44, "hello"]
print(o_lista, type(o_lista))
print("Lungimea listei", len(o_lista))


print("Primul element al listei", o_lista[0] )
print("Ultimul element al listei", o_lista[2] )

print("Ultimul element al listei", o_lista[3])  # IndexError: list index out of range


print("Ultimul element al listei cu index -1: ", o_lista[-1] )
print("Primul element al listei cu index -1: ", o_lista[-3] )

print("Ultimul element al listei", o_lista[-4])  # IndexError: list index out of range
