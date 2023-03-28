my_list = [3344,34334,454543,342534,4563456,3445,23455,234,262,2335,
43323,4356,345,4545,452,345,434,36,345,4334,5454,345,4352,23,365,345,47,63,
425,6578759,768,834,754,35,32,445,453456,56,7536867,3884526,4234,35353245,53244523,
566785,7547,743,4324,523472634,26665,63432,54645,32,453625,7568,5669576,754,64356,542644,
35,243,371,3251,351223,13231243,734,856,56,53,234342,56,545343]

#Your code here:
big_number = 999999999999999

for number in my_list:
    if number < big_number:
        big_number = number
    

print(big_number)

#SOLUCION ALCANSADA; RESUELVE EL PROBLEMA PERO NO LA VALIDAD EL TEST
# def min_number(list):
#     big_number = 99999999999999
#     for i in list:
#         if i < big_number:
#             big_number = i
#     return big_number

# print(min_number(my_list))
