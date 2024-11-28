def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
result_1 = get_multiplied_digits(1824)
result_2 = get_multiplied_digits(30507)
print(result)
print()
print(result_1)
print()
print(result_2)