my_list = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]

def my_function(numbers):
    new_list = []
    for i in range(len(my_list)):
    #The magic go here:
        if my_list[i] == 1:
            print(my_list[i])
            new_list.append(my_list[i])
        elif my_list[i] == 0:
            print(my_list[i])
            new_list.append("Yahoo")
    return new_list
print(my_function(my_list))


