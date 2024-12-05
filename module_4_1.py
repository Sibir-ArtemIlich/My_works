import fake_math
from fake_math import divide as div_tru
from true_math import divide as div_fals
rez1 = div_tru(5,9)
rez3 = div_tru(3, 0)
rez2 = div_fals(7, 0)
rez4 = div_fals(4, 8)
print(rez1)
print(rez2)
print(rez3)
print(rez4)
