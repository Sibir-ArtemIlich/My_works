class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
def go_to(self,i):
    if  i <= self.number_of_floors:
        print(self.name)
        for i in range(1, i+1):
             print(i)
    else:
        print(self.name)
        print("Такого этажа не существует")



jk1 = House('ЖК Эльбрус', 18)
jk2 = House('Домик у моря', 2)
jk3 = House('ЖК Родные просторы', 5)
go_to(jk1,19)
go_to(jk2,2)
go_to(jk3,4)
