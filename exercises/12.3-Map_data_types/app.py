list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
        new_list = []
        for i in items:
                new_list.append(type(i))
        return new_list

                

print(type_list(list_Strings))
# new_list = list(map(type_list, list_Strings))
# print(new_list)