immutable_var = (1, 3, "troya", [0,2,4])
print(immutable_var)
#immutable_var[3] = 9
#print(immutable_var)
mutable_list = list(immutable_var)
print(mutable_list)
mutable_list[2] = 5
print(mutable_list)