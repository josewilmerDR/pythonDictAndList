allNumbers = [23,12,35,5,3,2,3,54,3,21,534,23,42,1]


# def filter_function(items):
#     newList = []
#     for i in items:
#         if i > 10:
#             newList.append(i)
#     return newList

# print(filter_function(allNumbers))

greater_than = list(filter(lambda i : i > 10, allNumbers))
print(greater_than)