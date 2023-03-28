my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def maxInteger(list):
    aux = 0
    for i in list:
        if i > aux:
            aux = i
    return aux

print(maxInteger(my_list))
# #Forma rapida de resolver el problema, no validad por el test.
# my_list.sort()
# longer_number = my_list[len(my_list)-1]
# print(longer_number)