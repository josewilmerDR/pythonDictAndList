chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_list = []
    for i in chunk_one:
        new_list.append(i)
    for j in chunk_two:
        new_list.append(j)
    return new_list
   
# print(merge_list(chunk_one, chunk_two))
print(merge_list(chunk_one, chunk_two))