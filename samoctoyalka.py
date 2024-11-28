def  print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params(b = 25)
print_params(c = [1,2,3])
values_list = (2, 'трешь', [9,8,7])
values_list_2 = ('Сталин', 1945)
values_dict = {'a' : 99, 'b' : 'Ленин', 'c' : [2,4,6]}
print_params(values_list)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)