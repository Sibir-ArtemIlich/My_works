def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:     
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
         if first ==0:
            return first + 1
        else:
            return first

result = get_multiplied_digits(402030)
result_1 = get_multiplied_digits(40203)
result_2 = get_multiplied_digits(305070)
print(result)
print()
print(result_1)
print()
print(result_2)
#24

#24

#105
